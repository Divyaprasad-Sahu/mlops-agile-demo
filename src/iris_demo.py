"""Train and use a deterministic Iris classifier without import side effects."""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import joblib
import numpy as np
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

ROOT = Path(__file__).resolve().parents[1]
SEED = 42
MIN_ACCURACY = 0.95


def validate_dataset(X, y):
    X, y = np.asarray(X), np.asarray(y)
    if X.ndim != 2 or X.shape[1] != 4 or len(X) != len(y):
        raise ValueError("Expected four features per row and one target per row.")
    if y.ndim != 1 or len(X) < 5:
        raise ValueError("Expected a nonempty one-dimensional target array.")
    if not np.isfinite(X).all() or (X <= 0).any():
        raise ValueError("Measurements must be finite and positive.")
    if not np.isin(y, [0, 1, 2]).all() or len(np.unique(y)) != 3:
        raise ValueError("Expected all three Iris target classes: 0, 1, 2.")
    return X, y


def train_model():
    iris = load_iris()
    X, y = validate_dataset(iris.data, iris.target)
    # Match the supplied experiment's split; fix the classifier seed as well.
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=SEED
    )
    model = DecisionTreeClassifier(random_state=SEED)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    metrics = {
        "accuracy": float(accuracy_score(y_test, predictions)),
        "minimum_accuracy": MIN_ACCURACY,
        "random_state": SEED,
        "train_rows": len(X_train),
        "test_rows": len(X_test),
        "feature_names": list(iris.feature_names),
        "target_names": list(iris.target_names),
        "confusion_matrix": confusion_matrix(y_test, predictions, labels=[0, 1, 2]).tolist(),
        "classification_report": classification_report(
            y_test, predictions, labels=[0, 1, 2],
            target_names=iris.target_names, output_dict=True, zero_division=0
        ),
        "missing_values": int(np.isnan(X).sum()),
        "duplicate_rows": int(len(X) - len(np.unique(np.column_stack([X, y]), axis=0))),
    }
    # Retain duplicates to reproduce the supplied dataset and split.
    bundle = {"model": model, "target_names": list(iris.target_names),
              "feature_names": list(iris.feature_names)}
    return bundle, metrics


def prediction_details(bundle, measurements):
    values = np.asarray(measurements, dtype=float)
    if values.shape != (4,) or not np.isfinite(values).all() or (values <= 0).any():
        raise ValueError("Supply exactly four finite, positive measurements in centimetres.")
    model = bundle["model"]
    row = values.reshape(1, 4)
    probabilities = model.predict_proba(row)[0]
    position = int(np.argmax(probabilities))
    class_id = int(model.classes_[position])
    return {"species": bundle["target_names"][class_id],
            "leaf_probability": float(probabilities[position])}


def predict_species(bundle, measurements):
    return prediction_details(bundle, measurements)["species"]


def save_training_outputs(bundle, metrics, output_dir, data_dir):
    output_dir, data_dir = Path(output_dir), Path(data_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    data_dir.mkdir(parents=True, exist_ok=True)
    joblib.dump(bundle, output_dir / "iris_model.joblib")
    (output_dir / "metrics.json").write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    with (output_dir / "confusion_matrix.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["actual / predicted", *metrics["target_names"]])
        writer.writerows(zip(metrics["target_names"], metrics["confusion_matrix"]))
    iris = load_iris()
    with (data_dir / "iris.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([*iris.feature_names, "target", "species"])
        for features, target in zip(iris.data, iris.target):
            writer.writerow([*features, int(target), iris.target_names[target]])


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    train = commands.add_parser("train", help="Train, evaluate, and save the classifier")
    train.add_argument("--output-dir", type=Path, default=ROOT / "models")
    train.add_argument("--data-dir", type=Path, default=ROOT / "data")
    predict = commands.add_parser("predict", help="Predict from four measurements in cm")
    predict.add_argument("measurements", nargs=4, type=float,
                         metavar=("SEPAL_LENGTH", "SEPAL_WIDTH", "PETAL_LENGTH", "PETAL_WIDTH"))
    predict.add_argument("--model", type=Path, default=ROOT / "models" / "iris_model.joblib")
    args = parser.parse_args(argv)
    try:
        if args.command == "train":
            bundle, metrics = train_model()
            if metrics["accuracy"] < MIN_ACCURACY:
                raise ValueError("Accuracy did not meet the 95% acceptance criterion.")
            save_training_outputs(bundle, metrics, args.output_dir, args.data_dir)
            print(f"Accuracy: {metrics['accuracy']:.4f} ({metrics['accuracy']:.2%})")
            print(f"Train/test rows: {metrics['train_rows']}/{metrics['test_rows']}")
            print(f"Model and evaluation files: {args.output_dir.resolve()}")
        else:
            details = prediction_details(joblib.load(args.model), args.measurements)
            print(f"Prediction: {details['species']}")
            print(f"Leaf probability: {details['leaf_probability']:.2%} (not calibrated confidence)")
    except (ValueError, FileNotFoundError) as exc:
        parser.exit(1, f"Error: {exc}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
