# Perform Experiment 1 in VS Code

The experiment is a local Python project. VS Code is the editor and terminal
used to demonstrate it; GitHub shares the code and runs its CI/CD workflow.
The original executions were run locally through a command-line terminal.
This guide and the included tasks provide the corresponding VS Code workflow.

## Open the local project

1. In VS Code select **File → Open Folder** and choose `MLOps_Agile_Demo`.
2. In Explorer show `src`, `data`, `models`, `tests`, `docs` and `.github`.
3. Open `src/iris_demo.py`. Press **Ctrl+G**, enter `34`, and show the training function.
4. Open `docs/Product_Backlog.md` and `docs/Scrum_Records.md` for the Scrum components.

The local environment is already installed on the authoring machine. On a new
machine, use Python 3.11 or 3.12 in **Terminal → New Terminal**:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
```

The Windows task definitions call the environment's Python directly, so no
PowerShell activation-policy change is needed. Python editor features and Test
Explorer require the Microsoft Python extension; the terminal tasks do not.

## Run inside VS Code

Choose **Terminal → Run Task** and select:

| Task | What to show |
|---|---|
| Experiment 1: Train Iris model | Accuracy 1.0000, train/test rows 120/30, saved model outputs |
| Experiment 1: Predict sample flower | setosa and the explicitly labelled leaf probability |
| Experiment 1: Run automated tests | 19 passing tests and the JUnit report |
| Experiment 1: Show Git history | Meaningful local commits and the demonstration PR merge |

Alternatively, run these commands in the VS Code integrated terminal:

```powershell
.\.venv\Scripts\python.exe -m src.iris_demo train
.\.venv\Scripts\python.exe -m src.iris_demo predict 5.1 3.5 1.4 0.2
.\.venv\Scripts\python.exe -m pytest -q --junitxml=reports/junit.xml
git status
git log --oneline --graph --all
```

## Capture genuine VS Code screenshots for submission

Capture the editor with Explorer and the training code visible; the integrated
terminal with measured accuracy and prediction output; and the test file with
the 19-passed terminal result. Screenshots should show your actual executions.
The report's code excerpts are selectable copies of project source, not claims
of captured VS Code screens.

Use the public GitHub repository and Actions run separately to demonstrate
sharing, pull-request checks and automatic delivery after a code change.
