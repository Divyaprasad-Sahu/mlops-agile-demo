"""Safely unpack the downloaded workflow package and verify its model."""
from io import BytesIO
import json
from pathlib import Path
import subprocess
import sys
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
target = ROOT / "reports/downloaded_delivery"
target.mkdir(parents=True, exist_ok=True)
with ZipFile(ROOT / "reports/github_delivery_artifact.zip") as outer:
    package = outer.read("iris-delivery.zip")
with ZipFile(BytesIO(package)) as archive:
    for name in archive.namelist():
        resolved = (target / name).resolve()
        if not resolved.is_relative_to(target.resolve()):
            raise SystemExit("Unsafe archive path")
    archive.extractall(target)
prediction = subprocess.run([sys.executable, "-m", "src.iris_demo", "predict", "5.1", "3.5", "1.4", "0.2"],
                            cwd=target, capture_output=True, text=True, check=True)
assert "Prediction: setosa" in prediction.stdout
metrics = json.loads((target / "models/metrics.json").read_text())
assert metrics["accuracy"] >= 0.95
result = {"artifact_prediction": prediction.stdout.strip(), "artifact_accuracy": metrics["accuracy"],
          "required_files_present": all((target / name).is_file() for name in
              ("src/iris_demo.py", "README.md", "models/iris_model.joblib", "models/metrics.json", "data/iris.csv"))}
assert result["required_files_present"]
(ROOT / "docs/evidence/delivery_verification.json").write_text(json.dumps(result, indent=2))
file = ROOT / "docs/evidence/github_evidence.json"
evidence = json.loads(file.read_text())
evidence["artifact_verified"] = "Downloaded and extracted; included model predicts setosa; metrics and source checked"
file.write_text(json.dumps(evidence, indent=2))
print(json.dumps(result, indent=2))
