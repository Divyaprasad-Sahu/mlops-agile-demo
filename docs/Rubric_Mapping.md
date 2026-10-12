# Rubric Evidence Matrix

Each category has weight 20%, with four points possible. This matrix targets
the Excellent criteria; the evaluator determines the final score.

| Category | Evidence prepared | Verification |
|---|---|---|
| Git Command Usage | Separate repository, staged changes, meaningful commits, branch, history, remote and push transcript | Read actual command output and compare commit IDs |
| GitHub Code Management | Structured source, dataset, tests, docs, requirements and workflow; reviewed feature PR | Inspect public repository and PR diff |
| Python Project Organisation | Runnable Iris training/prediction, data provenance, saved model, metrics and setup instructions | Reproduce setup, training and prediction |
| Automated Testing Workflow | pytest data, accuracy, input, reproducibility and persistence checks; JUnit artifact | Local test output and successful Actions test job |
| CI/CD Demonstration | Code change triggers PR tests; merged main triggers dependent model delivery | PR and main run links plus delivery artifact |

Actual completion status, metrics and links are recorded in
`docs/evidence/Results.md`. A configured workflow alone is not evidence of a
successful online run.
