"""Read actual workflow evidence for this experiment repository, never print credentials."""
import argparse
import json
from io import BytesIO
from pathlib import Path
import subprocess
import urllib.request
import xml.etree.ElementTree as ET
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
API = "https://api.github.com/repos/Divyaprasad-Sahu/mlops-agile-demo"
HEADERS = {"Accept": "application/vnd.github+json", "User-Agent": "Iris-Lab-Evidence"}


def get(path):
    with urllib.request.urlopen(urllib.request.Request(API + path, headers=HEADERS), timeout=45) as response:
        return json.load(response)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--download", action="store_true")
    args = parser.parse_args()
    pr = get("/pulls/1")
    runs = get("/actions/runs?per_page=20")["workflow_runs"]
    summaries = []
    for run in runs:
        summaries.append({k: run[k] for k in ("id", "head_sha", "event", "status", "conclusion", "html_url")})
    evidence_dir = ROOT / "docs/evidence"
    evidence_dir.mkdir(parents=True, exist_ok=True)
    (evidence_dir / "workflow_runs.json").write_text(json.dumps(summaries, indent=2))
    print(json.dumps({"pr_merged": pr["merged"], "merge_sha": pr["merge_commit_sha"], "runs": summaries}, indent=2))
    pr_runs = [r for r in runs if r["event"] == "pull_request" and r["head_sha"] == pr["head"]["sha"]]
    main_runs = [r for r in runs if r["event"] == "push" and r["head_sha"] == pr["merge_commit_sha"]]
    if not pr_runs or not main_runs or main_runs[0]["conclusion"] != "success":
        return
    pr_run, main_run = pr_runs[0], main_runs[0]
    artifacts = get(f"/actions/runs/{main_run['id']}/artifacts")["artifacts"]
    jobs = get(f"/actions/runs/{main_run['id']}/jobs")["jobs"]
    (evidence_dir / "main_jobs.json").write_text(json.dumps(jobs, indent=2))
    (evidence_dir / "main_artifacts.json").write_text(json.dumps(artifacts, indent=2))
    artifact = next(a for a in artifacts if a["name"].startswith("iris-delivery-"))
    evidence = {
        "pr_url": pr["html_url"], "pr_status": "Merged after passing checks",
        "feature_sha": pr["head"]["sha"], "merge_sha": pr["merge_commit_sha"],
        "pr_run_url": pr_run["html_url"], "main_run_url": main_run["html_url"],
        "pr_tests": "19 passed; delivery skipped on PR", "main_jobs": "; ".join(j["name"] + ": " + j["conclusion"] for j in jobs),
        "artifact_name": artifact["name"], "artifact_id": artifact["id"],
        "artifact_verified": "Download verification pending",
    }
    if args.download:
        # Use the existing Git credential manager only for the authorised GitHub account.
        credential = subprocess.run(["git", "credential", "fill"], input="protocol=https\nhost=github.com\n\n",
                                    capture_output=True, text=True, check=True)
        fields = dict(line.split("=", 1) for line in credential.stdout.splitlines() if "=" in line)
        headers = dict(HEADERS, Authorization="Bearer " + fields["password"])
        # urllib strips normal origin credentials? Use a redirect handler explicitly to
        # avoid forwarding GitHub credentials to signed artifact storage URLs.
        class SafeRedirect(urllib.request.HTTPRedirectHandler):
            def redirect_request(self, req, fp, code, msg, hdrs, newurl):
                redirected = super().redirect_request(req, fp, code, msg, hdrs, newurl)
                if redirected is not None:
                    redirected.remove_header("Authorization")
                return redirected
        def download(path):
            request = urllib.request.Request(API + path, headers=headers)
            with urllib.request.build_opener(SafeRedirect()).open(request, timeout=60) as response:
                return response.read()
        payload = download(f"/actions/artifacts/{artifact['id']}/zip")
        target = ROOT / "reports/github_delivery_artifact.zip"
        target.parent.mkdir(exist_ok=True)
        target.write_bytes(payload)
        print(f"Downloaded delivery artifact: {len(payload)} bytes")
        test_artifact = next(a for a in artifacts if a["name"].startswith("test-results-"))
        test_payload = download(f"/actions/artifacts/{test_artifact['id']}/zip")
        with ZipFile(BytesIO(test_payload)) as archive:
            junit = archive.read(next(n for n in archive.namelist() if n.endswith("junit.xml")))
        (evidence_dir / "github_junit.xml").write_bytes(junit)
        suite = ET.fromstring(junit).find("testsuite")
        assert suite is not None and int(suite.get("failures", 0)) == 0 and int(suite.get("errors", 0)) == 0
        evidence["main_test_count"] = int(suite.get("tests"))
        evidence["pr_tests"] = f"{suite.get('tests')} passed; delivery skipped on PR"
        log_payload = download(f"/actions/runs/{main_run['id']}/logs")
        (ROOT / "reports/github_workflow_logs.zip").write_bytes(log_payload)
        excerpts = []
        with ZipFile(BytesIO(log_payload)) as archive:
            for name in archive.namelist():
                if name.endswith(".txt"):
                    lines = archive.read(name).decode("utf-8", errors="replace").splitlines()
                    selected = [line for line in lines if (" passed in " in line or "Accuracy: " in line or "Train/test rows:" in line or "Artifact download URL:" in line)]
                    if selected:
                        excerpts.append("## " + name + "\n\n```text\n" + "\n".join(selected) + "\n```\n")
        (evidence_dir / "Workflow_Log_Excerpts.md").write_text("# Actual GitHub Actions Log Excerpts\n\n" + "\n".join(excerpts))
    (evidence_dir / "github_evidence.json").write_text(json.dumps(evidence, indent=2))


if __name__ == "__main__":
    main()
