"""Assemble a self-contained experiment delivery ZIP after tests have passed."""
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parents[1]


def main():
    required = [ROOT / "models" / name for name in
                ("iris_model.joblib", "metrics.json", "confusion_matrix.csv")]
    for file in required:
        if not file.is_file():
            raise SystemExit(f"Missing training output: {file}")
    (ROOT / "dist").mkdir(exist_ok=True)
    target = ROOT / "dist" / "iris-delivery.zip"
    files = required + [ROOT / name for name in
                        ("README.md", "requirements.txt", "requirements-dev.txt", "pytest.ini", ".gitignore", "models/README.md")]
    for folder in ("src", "data", "tests", "docs", "tools", ".github", ".vscode"):
        files.extend(p for p in (ROOT / folder).rglob("*")
                     if p.is_file() and "__pycache__" not in p.parts and not p.name.startswith("~$")
                     and p.name not in ("Experiment_1_Agile_and_Scrum_Report.docx", "Experiment_1_Agile_and_Scrum_Report_Revised.docx")
                     and p.suffix in (".py", ".ps1", ".md", ".csv", ".json", ".docx", ".yml", ".xml", ".txt"))
    with ZipFile(target, "w", ZIP_DEFLATED) as archive:
        for file in sorted(set(files)):
            archive.write(file, file.relative_to(ROOT).as_posix())
    print(f"Delivery ZIP: {target}")


if __name__ == "__main__":
    main()
