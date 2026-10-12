import importlib
import json
import subprocess
import sys

import joblib
import numpy as np
import pytest
from sklearn.datasets import load_iris

from src.iris_demo import (predict_species, save_training_outputs, train_model,
                           validate_dataset)


def test_dataset_contract():
    iris = load_iris()
    X, y = validate_dataset(iris.data, iris.target)
    assert X.shape == (150, 4)
    assert np.bincount(y).tolist() == [50, 50, 50]


@pytest.mark.parametrize("fault", ["nan", "negative", "shape", "class", "targets"])
def test_invalid_dataset_is_rejected(fault):
    iris = load_iris()
    X, y = iris.data.copy(), iris.target.copy()
    if fault == "nan":
        X[0, 0] = np.nan
    elif fault == "negative":
        X[0, 0] = -1
    elif fault == "shape":
        X = X[:, :3]
    elif fault == "class":
        y[0] = 8
    else:
        y = y[:-1]
    with pytest.raises(ValueError):
        validate_dataset(X, y)


def test_training_is_reproducible_and_meets_acceptance():
    first, metrics = train_model()
    second, repeated = train_model()
    assert metrics == repeated
    assert metrics["accuracy"] >= 0.95
    assert metrics["train_rows"] == 120 and metrics["test_rows"] == 30
    assert sum(map(sum, metrics["confusion_matrix"])) == 30
    np.testing.assert_array_equal(first["model"].predict(load_iris().data),
                                  second["model"].predict(load_iris().data))


@pytest.mark.parametrize("values,expected", [
    ([5.1, 3.5, 1.4, 0.2], "setosa"),
    ([7.0, 3.2, 4.7, 1.4], "versicolor"),
    ([6.3, 3.3, 6.0, 2.5], "virginica"),
])
def test_known_predictions(values, expected):
    bundle, _ = train_model()
    assert predict_species(bundle, values) == expected


@pytest.mark.parametrize("values", [[1, 2], [1, 2, 3, 0],
                                   [1, 2, 3, float("inf")], [1, 2, 3, -1]])
def test_prediction_rejects_invalid_measurements(values):
    bundle, _ = train_model()
    with pytest.raises(ValueError):
        predict_species(bundle, values)


def test_saved_model_and_reports_roundtrip(tmp_path):
    bundle, metrics = train_model()
    output, data = tmp_path / "models", tmp_path / "data"
    save_training_outputs(bundle, metrics, output, data)
    loaded = joblib.load(output / "iris_model.joblib")
    np.testing.assert_array_equal(bundle["model"].predict(load_iris().data),
                                  loaded["model"].predict(load_iris().data))
    assert json.loads((output / "metrics.json").read_text()) == metrics
    assert len((data / "iris.csv").read_text().splitlines()) == 151
    assert len((output / "confusion_matrix.csv").read_text().splitlines()) == 4


def test_import_does_not_train(monkeypatch):
    import sklearn.tree
    import src.iris_demo as module

    def forbidden(*args, **kwargs):
        raise AssertionError("Import must not train a model")

    monkeypatch.setattr(sklearn.tree.DecisionTreeClassifier, "fit", forbidden)
    importlib.reload(module)


def test_cli_train_and_predict(tmp_path):
    model_dir = tmp_path / "models"
    result = subprocess.run([sys.executable, "-m", "src.iris_demo", "train",
                             "--output-dir", str(model_dir), "--data-dir", str(tmp_path / "data")],
                            capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    assert "Accuracy:" in result.stdout
    predicted = subprocess.run([sys.executable, "-m", "src.iris_demo", "predict",
                               "5.1", "3.5", "1.4", "0.2", "--model",
                               str(model_dir / "iris_model.joblib")], capture_output=True, text=True)
    assert predicted.returncode == 0, predicted.stderr
    assert "setosa" in predicted.stdout


def test_cli_missing_model_has_helpful_error(tmp_path):
    result = subprocess.run([sys.executable, "-m", "src.iris_demo", "predict",
                             "5.1", "3.5", "1.4", "0.2", "--model", str(tmp_path / "absent.joblib")],
                            capture_output=True, text=True)
    assert result.returncode == 1
    assert "Error:" in result.stderr
