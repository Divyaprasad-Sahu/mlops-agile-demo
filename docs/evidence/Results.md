# Verified Experiment Results

Experiment performed on 12 October 2026. Scrum ceremonies are an individual
simulation; these technical results are actual executions.

## Model and tests

- Dataset: 150 rows, four features, three classes, 50 rows per class.
- Data audit: zero missing values; one duplicate row retained to match the handout.
- Training/test split: 120/30 rows, test size 0.2, random state 42.
- Decision Tree random state: 42.
- Held-out accuracy: 1.0 (100%); acceptance requirement 95% met.
- Confusion matrix: `[[10, 0, 0], [0, 9, 0], [0, 0, 11]]`.
- Local tests: 19 passed. GitHub JUnit report confirms 19 tests with zero errors or failures.
- Example prediction: `5.1 3.5 1.4 0.2` gives setosa, leaf probability 100%.
- Downloaded GitHub model: extracted and used successfully for the same prediction.
- Independent second environment: installed dependencies, ran all 19 tests,
  predicted with the delivered model and retrained successfully. See
  `Clean_Environment_Verification.md` for captured output.

## Actual GitHub demonstration

- [Public repository](https://github.com/Divyaprasad-Sahu/mlops-agile-demo)
- [Merged demonstration PR 1](https://github.com/Divyaprasad-Sahu/mlops-agile-demo/pull/1)
- Feature commit: `68d5dc6b64f6119a8af1dc68ec12c76b3c680c1f`.
- Merge commit: `90f694c5009514606ec884c1c2e9b056394f50b5`.
- [Passing PR workflow](https://github.com/Divyaprasad-Sahu/mlops-agile-demo/actions/runs/38260990034): validation successful; delivery skipped.
- [Passing merged main workflow](https://github.com/Divyaprasad-Sahu/mlops-agile-demo/actions/runs/38261476545): validation and delivery both successful.
- Delivered artifact: `iris-delivery-90f694c5009514606ec884c1c2e9b056394f50b5`, artifact ID `11752004464`.

Machine-readable evidence is retained in `github_evidence.json`,
`main_jobs.json`, `main_artifacts.json` and `github_junit.xml`.
`Workflow_Log_Excerpts.md` contains actual test and training output from the cloud run.

## Sprint increment acceptance

- [x] Iris dataset loaded, validated, and exported.
- [x] Decision Tree trained reproducibly on the specified split.
- [x] At least 95% held-out accuracy measured and saved.
- [x] Saved model reloads and predicts correctly.
- [x] Automated tests pass locally and in Actions.
- [x] Code change reviewed and passing PR merged.
- [x] Main delivery artifact available and verified.
- [x] Scrum documentation and report prepared; final report visually inspected before submission.

## Evaluation limits

The fixed small hold-out split follows the course handout. It does not establish
production performance on new real-world data. Leaf probability is not calibrated
confidence. Future work can use cross-validation and independent data.
