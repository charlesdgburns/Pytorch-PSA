# Pytorch-PSA

A practical first project in batched power-system analysis with PyTorch.

**Start here:** [the tutorial notebook](notebooks/01_batched_dc_power_flow.ipynb).

Eight exercises develop DC network equations, batched scenarios, factorisation reuse, sequential storage simulation, forward-mode sensitivities, outage screening, and performance comparisons. Mathematical explanations and physical validation checks accompany each exercise.

## Run locally

Python 3.10 or newer is recommended.

```bash
git clone https://github.com/charlesdgburns/Pytorch-PSA.git
cd Pytorch-PSA
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
```

On Windows activate with `.venv\Scripts\activate`.
For a specific CUDA configuration, follow the installation selector at https://pytorch.org/get-started/locally/ before installing remaining requirements.

## Exercises and reference answers

Run cells in order, filling in each exercise. Placeholders intentionally stop execution.

If you need a reference answer, replace the corresponding exercise cell with:

```python
from pathlib import Path
exec(Path("../solutions/reference.py").read_text())
exec(SOLUTIONS["matrices"])
```

Choose the matching key: `matrices`, `power_flow`, `cached_solver`, `rollout`, `flow_jvp`, `rollout_jvp`, `outages`, or `benchmark`. The notebook assumes its working directory is `notebooks/`. Adjust the path if you launch it from elsewhere.

To validate all reference answers and notebook checks without completing the exercises:

```bash
python scripts/validate_notebook.py
```

This substitutes answers in memory; the exercise notebook stays unchanged.

## Scope

Synthetic five-bus grid; lossless DC power flow; ideal storage; fixed-injection single-line outage screening. Educational examples, not an operational security assessment.

The five-bus benchmark demonstrates batching but cannot establish GPU performance on large sparse transmission networks. Forward-mode AD dual tensors are distinct from constrained-optimisation multipliers.
