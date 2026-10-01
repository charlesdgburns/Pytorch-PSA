"""Execute notebook checks with reference answers; leave exercises unchanged."""
from pathlib import Path
import json
import os

os.environ.setdefault("MPLBACKEND", "Agg")
root = Path(__file__).resolve().parents[1]
notebook = json.loads((root / "notebooks/01_batched_dc_power_flow.ipynb").read_text())
reference = {}
exec((root / "solutions/reference.py").read_text(), reference)
namespace = {"__name__": "__main__"}
for index, cell in enumerate(notebook["cells"]):
    if cell["cell_type"] != "code":
        continue
    source = cell["source"]
    if isinstance(source, list):
        source = "".join(source)
    exercise = cell["metadata"].get("exercise")
    if exercise:
        source = reference["SOLUTIONS"][exercise]
    try:
        exec(compile(source, f"notebook-cell-{index}", "exec"), namespace)
    except Exception as error:
        raise RuntimeError(f"Notebook cell {index} failed") from error
print("All reference exercises and notebook checks passed.")
