# Demonstration and Viva Guide

## Five minute demonstration

1. Show the repository structure and explain the six backlog stories.
2. Describe how one student simulates the five handout roles and a one-week Sprint.
3. Run `python -m src.iris_demo train`; show measured accuracy and saved files.
4. Run `python -m src.iris_demo predict 5.1 3.5 1.4 0.2`; explain centimetres and feature order.
5. Run `python -m pytest -q`; explain the accuracy and model reload tests.
6. Show `git log --oneline --graph --all` and the demonstration PR's actual code diff.
7. Open the PR Actions run and show successful tests and skipped delivery.
8. Open the merged main run; show both successful jobs and download the delivery artifact.
9. Explain review, retrospective, and the rubric evidence matrix.

## Git commands and purpose

```powershell
git init -b main
git status
git add .
git commit -m "feat: add reproducible Iris classifier"
git log --oneline --graph --all
git diff
git switch -c feat/prediction-confidence
git add src tests README.md
git commit -m "feat: report confidence with Iris predictions"
git remote add origin https://github.com/Divyaprasad-Sahu/mlops-agile-demo.git
git push -u origin main
git push -u origin feat/prediction-confidence
git switch main
git pull --ff-only
```

These are explanatory examples. `docs/evidence/git_commands.txt` records actual
local commands and output, including commit IDs and publishing results.
The submission also includes a readable snapshot in
`docs/evidence/Git_Command_Transcript.md`.

## Viva questions

**What is Agile?** Iterative development with frequent feedback, working
increments, collaboration, and adaptation to changing needs.

**What is Scrum?** A framework using a Product Owner, Scrum Master and
Developers, a Product Backlog, Sprint Backlog and Increment, and timeboxed
events to inspect and adapt progress toward goals.

**Product Backlog versus Sprint Backlog?** The first orders product work; the
second contains the Sprint Goal, selected work and the Developers' plan.

**Review versus retrospective?** The review inspects the increment and future
product direction; the retrospective improves the team's effectiveness.

**Why split the dataset?** Train on one subset and estimate performance on
unseen rows. This lab holds out 20%; evaluation data does not fit the model.

**Why seed 42?** A fixed random state reproduces the lab split and classifier.
The number itself has no special predictive meaning.

**How is accuracy calculated?** Correct predictions divided by total test
examples. The confusion matrix also shows which classes were confused.

**Why automate tests?** They repeat acceptance checks whenever code changes
and identify regressions before the increment is delivered.

**What connects CI to CD here?** The `deliver` job needs the successful `test`
job and runs only on main, packaging the source, instructions and trained model.

**Is this a deployed API?** The deliverable is downloadable software, not a
hosted prediction service.

**What would improve the ML evaluation?** Cross-validation and independent
data would give stronger evidence than one small fixed hold-out split.
