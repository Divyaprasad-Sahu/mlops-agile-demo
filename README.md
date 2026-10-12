# Agile and Scrum MLOps Experiment

An individual lab simulation by **Divyaprasad Sahu**. The project applies Agile
and Scrum to a reproducible Iris Decision Tree classifier, verifies it with
pytest, and delivers the accepted increment through GitHub Actions.

## Quick start

Use Python 3.11 or 3.12. From this repository's root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
python -m src.iris_demo train
python -m src.iris_demo predict 5.1 3.5 1.4 0.2
python -m pytest -q --junitxml=reports/junit.xml
python tools/package_delivery.py
```

On Linux/macOS activate with `source .venv/bin/activate`. If PowerShell activation
is restricted, call `.\.venv\Scripts\python.exe` directly instead of changing
system policy. `python src/iris_demo.py train` also works.

Feature order is **sepal length, sepal width, petal length, petal width**, all in
centimetres. Training uses the scikit-learn bundled dataset, 120 training rows,
30 held-out test rows, and seed 42 for the split and classifier. The training
command rejects accuracy below 95% and writes:

- `models/iris_model.joblib`: trained model and feature/class labels.
- `models/metrics.json`: measured accuracy, classification report, and data audit.
- `models/confusion_matrix.csv`: actual classes as rows, predicted classes as columns.
- `data/iris.csv`: inspectable dataset export.

No missing values need imputation in this dataset. Duplicate rows are reported
and retained to reproduce the assignment's original split. A small single
hold-out evaluation demonstrates the lab; it is not a production performance claim.

## Project organisation

```text
MLOps_Agile_Demo/
  .github/workflows/ci.yml   Automated tests and main-branch delivery
  data/                     Iris data and provenance
  src/                      Training and prediction code
  models/                   Generated model and evaluation files
  tests/                    Acceptance and invalid-input tests
  tools/                    ZIP packaging and report generation helpers
  docs/                     Scrum records, report, demo guide, evidence
  requirements.txt          Pinned ML dependencies
  requirements-dev.txt      Testing dependency
  pytest.ini                Test discovery configuration
  README.md                 Setup and usage
```

## Scrum and experiment documentation

- [Product backlog](docs/Product_Backlog.md)
- [Roles and ceremonies](docs/Scrum_Records.md)
- [Demonstration and viva guide](docs/Demonstration_Guide.md)
- [Rubric evidence](docs/Rubric_Mapping.md)

All ceremonies are explicitly labelled as an individual simulation. Technical
outputs and GitHub evidence are actual executions, recorded separately.

## Continuous integration and delivery

Every push and pull request runs the test job under Python 3.11. A successful
`main` run starts the dependent delivery job. Failed tests prevent model
delivery. Pull requests test changes without producing delivery artifacts.

Open the successful run under **Actions → Iris CI and delivery**. Download
`iris-delivery-<commit SHA>`, then extract the enclosed `iris-delivery.zip`.
Install `requirements.txt` in a fresh environment and run prediction using the
included model. Downloadable tested software is the CD mechanism for this lab.
Artifacts expire after 90 days; rerun the workflow to recreate them.

Load only trusted joblib files. Generated binaries, environments, caches, and
local test reports are excluded from Git; workflow artifacts deliver them.

## References

- Assignment: Experiment 1 Agile and Scrum Demo, supplied course handout.
- [The Scrum Guide](https://scrumguides.org/scrum-guide.html)
- [scikit-learn Iris dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html)
- [GitHub Actions documentation](https://docs.github.com/en/actions)

The handout lists ML Engineer, Data Engineer, and Tester as project roles.
Within Scrum, these are specialisations of Developers alongside the Product
Owner and Scrum Master accountabilities.
