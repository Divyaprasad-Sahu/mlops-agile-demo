"""Windows adapter: native Word PDF export, then canonical render_docx rasterization.

Run with the bundled Python runtime. LibreOffice is not bundled on this host.
The adapter leaves the managed renderer unchanged and uses its page image logic.
"""
import importlib.util
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
skill = Path.home() / ".codex/plugins/cache/openai-primary-runtime/documents/26.1011.11113/skills/documents"
runtime = Path(sys.executable).parent
dependencies = runtime.parent
spec = importlib.util.spec_from_file_location("canonical_renderer", skill / "render_docx.py")
renderer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(renderer)
poppler = dependencies / "native/poppler/Library/bin"
if not poppler.exists():
    poppler = dependencies / "native/poppler/bin"
os.environ["PATH"] = str(poppler) + os.pathsep + os.environ["PATH"]


def word_pdf(doc_path, user_profile, convert_tmp_dir, stem, verbose):
    output = str(Path(convert_tmp_dir) / (stem + ".pdf"))
    shell = dependencies / "native/powershell/pwsh.exe"
    result = subprocess.run([str(shell), "-NoProfile", "-File", str(ROOT / "tools/render_word.ps1"),
                             "-InputPath", doc_path, "-OutputPath", output], capture_output=True, text=True)
    if result.returncode:
        return "", result.stdout + result.stderr
    return output, result.stdout


renderer.convert_to_pdf = word_pdf
sys.argv = [str(skill / "render_docx.py"), *sys.argv[1:]]
renderer.main()
