# Individual Scrum Simulation

This is a compressed educational simulation of a one-week Sprint. One student,
Divyaprasad Sahu, assumes all five handout roles. The day-by-day records below
are simulated ceremony records, not claims that five people met over five
calendar days. Git history and test/Actions evidence record actual execution.

## Roles and responsibilities

| Handout role | Student | Responsibility and output |
|---|---|---|
| Product Owner | Divyaprasad Sahu | Set the 95% acceptance goal, order backlog, accept completed increment |
| Scrum Master | Divyaprasad Sahu | Facilitate planning, daily discussion, review and retrospective; track blockers |
| ML Engineer | Divyaprasad Sahu | Choose Decision Tree, fix seed, train and persist model |
| Data Engineer | Divyaprasad Sahu | Load, audit, export and split Iris data |
| Tester | Divyaprasad Sahu | Check data contracts, accuracy, invalid inputs, saved-model predictions and workflow results |

Scrum defines Product Owner, Scrum Master, and Developers accountabilities.
ML Engineer, Data Engineer, and Tester are the assignment's specialisations
within Developers. Daily Scrum is a Developers event; all-role updates below
are included to follow the course simulation format.

## Sprint planning

Duration: one week (five simulated working days). Goal: build and deliver the
first working, reproducible Iris ML model. All six backlog stories are selected
because the lab increment must include source, model, results and documentation.

| Task | Story | Estimate | Role | Dependency |
|---|---|---|---|---|
| Prepare workspace and dependencies | Support | 20 min | Scrum Master | None |
| Load and export dataset | US1 | 20 min | Data Engineer | Workspace |
| Audit and prepare features | US2 | 30 min | Data Engineer | US1 |
| Train Decision Tree | US3 | 30 min | ML Engineer | US2 |
| Evaluate and automate tests | US4 | 45 min | Tester | US3 |
| Save and verify model | US5 | 20 min | ML Engineer | US3 |
| Git and Actions setup | Support | 45 min | Scrum Master | Tests |
| Report and demonstration | US6 | 60 min | Product Owner | Results |

Total estimated effort: 270 minutes, distributed across the simulated week.
These are planning estimates; they are not measured time sheets.

## Daily Scrum records

| Day | Yesterday | Today | Blockers and response |
|---|---|---|---|
| 1 | Product goal and roles identified | Create workspace and prioritise backlog | Check Python/Git access before work starts |
| 2 | Workspace and requirements prepared | Data Engineer audits Iris; ML Engineer trains baseline | Missing libraries: install pinned dependencies |
| 3 | Dataset and classifier prepared | Tester evaluates accuracy; ML Engineer saves model | Test/data issues: investigate before acceptance |
| 4 | Model tests and persistence checked | Scrum Master connects Actions; Developers propose code change | GitHub authentication or workflow errors: inspect logs |
| 5 | Pipeline and increment prepared | Product Owner reviews evidence; document retrospective | Any failed checks keep acceptance pending |

Role-level day 3 updates follow the handout's three-question format:

| Role | Yesterday | Today | Blockers |
|---|---|---|---|
| Product Owner | Requirements and acceptance criteria set | Review backlog against acceptance evidence | None in the simulation |
| Scrum Master | Sprint tasks and dependencies agreed | Facilitate updates and remove environment blockers | Resolve installation/authentication issues |
| ML Engineer | Decision Tree algorithm selected | Train with fixed seed and save the model | Wait for validated data |
| Data Engineer | Iris dataset loaded | Validate measurements and split data | Resolve missing dependencies |
| Tester | Test cases prepared | Evaluate held-out results and run automated tests | Wait for trained model |

## Sprint review

Demonstrate training, measured accuracy, a prediction, pytest results, a reviewed
code change, and the successful main-branch delivery artifact. Compare every
story with its acceptance criterion. The final evidence record contains the
actual numbers and online completion status.

Increment checklist:

- [ ] Iris dataset loaded, validated, and exported.
- [ ] Decision Tree trained reproducibly on the specified split.
- [ ] At least 95% held-out accuracy measured and saved.
- [ ] Saved model reloads and predicts correctly.
- [ ] Automated tests pass locally and in Actions.
- [ ] Code change reviewed and passing PR merged.
- [ ] Main delivery artifact available and verified.
- [ ] Documentation and report complete.

The completed checklist is recorded in `docs/evidence/Results.md`.

## Sprint retrospective

What went well: a small dataset, fixed seed, clear story criteria and focused
tests make the increment easy to reproduce and review. Splitting data before
training prevents direct training on the evaluation rows.

What could cause delays: missing packages, network restrictions, GitHub access,
and report-rendering dependencies. A model script without persistence or tests
would also leave acceptance evidence incomplete.

Improvement actions for the next Sprint:

| Action | Owner role | Verification |
|---|---|---|
| Check tools and install dependencies before planning | Scrum Master | Fresh setup succeeds |
| Add tests alongside each story | Tester | CI checks each proposed change |
| Keep model configuration reproducible | ML Engineer | Repeated metrics/predictions agree |
| Review evidence before accepting work | Product Owner | Links and artifacts match the accepted commit |

Potential next-Sprint backlog: compare algorithms using cross-validation and
add an input interface. Neither is claimed as delivered in this Sprint.
