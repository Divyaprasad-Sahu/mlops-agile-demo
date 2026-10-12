"""Preserve actual local command output as readable submission evidence."""
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
folder = ROOT / "docs/evidence"
initial = """# Git Command Execution Evidence

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
"""
raw = (folder / "git_commands.txt").read_text(encoding="utf-8-sig")
pull = (folder / "pull_output.txt").read_text(encoding="utf-8-sig")
(folder / "Git_Command_Transcript.md").write_text(initial + raw + "\n```\n\n## Fast forward after GitHub merge\n\n```text\n> git pull --ff-only\n" + pull + "\n```\n", encoding="utf-8")
clean = "# Independent Clean Environment Verification\n\nThe actual downloaded GitHub increment was installed in a second isolated environment.\n\n"
for label, filename in (("Acceptance tests", "clean_environment_tests.txt"), ("Included model prediction", "clean_environment_prediction.txt"), ("Fresh training", "clean_environment_training.txt")):
    clean += "## " + label + "\n\n```text\n" + (ROOT / "reports" / filename).read_text(encoding="utf-8-sig") + "\n```\n\n"
(folder / "Clean_Environment_Verification.md").write_text(clean, encoding="utf-8")
print("Git transcript and clean environment output preserved")
