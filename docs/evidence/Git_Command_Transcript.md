# Git Command Execution Evidence

## Initial repository creation

The following output was captured during the initial setup command on
12 October 2026, before the automatic command logger was added.

```text
> git init -b main MLOps_Agile_Demo
Initialized empty Git repository in C:/Users/Divyaprasad Sahu/Desktop/AI assistant/MLOps_Agile_Demo/.git/
> git -C MLOps_Agile_Demo add .
> git -C MLOps_Agile_Demo commit -m 'chore: initialise organised Iris MLOps experiment'
[main (root-commit) 6967c0a] chore: initialise organised Iris MLOps experiment
 7 files changed, 33 insertions(+)
```

## Automatically captured command transcript

This transcript includes the first restricted-network push failure followed by
the successful authorised push. Empty output from staging commands is normal.

```text

> git status
On branch main
Untracked files:
  (use "git add <file>..." to include in what will be committed)
	tools/git_evidence.ps1

nothing added to commit but untracked files present (use "git add" to track)

Exit code: 0

> git log --oneline --graph --all
* 8b458fc docs: record Scrum simulation setup and measured Iris results
* d8c0ad7 ci: test every change and deliver accepted main increments
* 456cb07 test: verify data accuracy prediction and saved model roundtrip
* 862d998 feat: train validate and persist reproducible Iris classifier
* 6967c0a chore: initialise organised Iris MLOps experiment

Exit code: 0

> git push -u origin main
fatal: unable to access 'https://github.com/Divyaprasad-Sahu/mlops-agile-demo.git/': getaddrinfo() thread failed to start

Exit code: 128

> git push -u origin main
branch 'main' set up to track 'origin/main'.
To https://github.com/Divyaprasad-Sahu/mlops-agile-demo.git
 * [new branch]      main -> main

Exit code: 0

> git switch -c feat/prediction-confidence
Switched to a new branch 'feat/prediction-confidence'

Exit code: 0

> git diff --stat
warning: in the working copy of 'README.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'src/iris_demo.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'tests/test_iris_demo.py', LF will be replaced by CRLF the next time Git touches it
 README.md               |  5 +++++
 src/iris_demo.py        | 19 +++++++++++++++----
 tests/test_iris_demo.py | 12 +++++++++++-
 3 files changed, 31 insertions(+), 5 deletions(-)

Exit code: 0

> git add src tests README.md tools/git_evidence.ps1
warning: in the working copy of 'README.md', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'src/iris_demo.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'tests/test_iris_demo.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'tools/git_evidence.ps1', LF will be replaced by CRLF the next time Git touches it

Exit code: 0

> git commit -m feat: report leaf probability with Iris predictions
[feat/prediction-confidence 68d5dc6] feat: report leaf probability with Iris predictions
 4 files changed, 43 insertions(+), 5 deletions(-)
 create mode 100644 tools/git_evidence.ps1

Exit code: 0

> git push -u origin feat/prediction-confidence
remote: 
remote: Create a pull request for 'feat/prediction-confidence' on GitHub by visiting:        
remote:      https://github.com/Divyaprasad-Sahu/mlops-agile-demo/pull/new/feat/prediction-confidence        
remote: 
branch 'feat/prediction-confidence' set up to track 'origin/feat/prediction-confidence'.
To https://github.com/Divyaprasad-Sahu/mlops-agile-demo.git
 * [new branch]      feat/prediction-confidence -> feat/prediction-confidence

Exit code: 0

> git switch main
M	tools/package_delivery.py
Your branch is up to date with 'origin/main'.
Switched to branch 'main'

Exit code: 0

> git log --oneline --graph --all
*   90f694c Merge pull request #1 from Divyaprasad-Sahu/feat/prediction-confidence
|\  
| * 68d5dc6 feat: report leaf probability with Iris predictions
|/  
* 8b458fc docs: record Scrum simulation setup and measured Iris results
* d8c0ad7 ci: test every change and deliver accepted main increments
* 456cb07 test: verify data accuracy prediction and saved model roundtrip
* 862d998 feat: train validate and persist reproducible Iris classifier
* 6967c0a chore: initialise organised Iris MLOps experiment

Exit code: 0

```

## Fast forward after GitHub merge

```text
> git pull --ff-only
From https://github.com/Divyaprasad-Sahu/mlops-agile-demo
   8b458fc..90f694c  main       -> origin/main
Updating 8b458fc..90f694c
Fast-forward
 README.md               |  5 +++++
 src/iris_demo.py        | 19 +++++++++++++++----
 tests/test_iris_demo.py | 12 +++++++++++-
 tools/git_evidence.ps1  | 12 ++++++++++++
 4 files changed, 43 insertions(+), 5 deletions(-)
 create mode 100644 tools/git_evidence.ps1

```
