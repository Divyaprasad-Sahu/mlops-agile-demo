# Product Backlog

Product goal: classify Iris flowers with at least 95% accuracy on the fixed
held-out split and deliver reproducible, tested source and model outputs.

| ID | User story from the handout | Priority | Acceptance criteria | Responsible role |
|---|---|---|---|---|
| US1 | Download Iris Dataset | High | Load the bundled dataset and export 150 rows, four features, and three labelled classes | Data Engineer |
| US2 | Clean Dataset | High | Check shape, missing/nonfinite values, positive measurements, and labels; document duplicates without altering the reference split | Data Engineer |
| US3 | Train Decision Tree Model | High | Train on 120 rows with seed 42 and reproduce predictions | ML Engineer |
| US4 | Evaluate Accuracy | Medium | Evaluate only the 30 held-out rows, achieve at least 95%, and save the confusion matrix and classification report | Tester |
| US5 | Save Model | Medium | Save and reload the model with identical predictions; include it in delivery | ML Engineer |
| US6 | Prepare Documentation | Low | Provide installation, execution, Scrum records, evidence, and a lab report | Product Owner |

High-priority tasks come first because evaluation and delivery depend on valid
data and a working classifier. Lower priority does not mean optional: every
story must meet its acceptance criteria before the increment is accepted.

Additional rubric tasks: initialise and use Git, publish clear commit history,
automate tests, and demonstrate a passing code change and dependent delivery.

Definition of Done: story criteria met; tests pass; code is reviewed through a
pull request; documentation is updated; main-branch delivery succeeds; evidence
links are recorded. Story completion is confirmed in the final review using
technical results rather than assumed from this planning table.
