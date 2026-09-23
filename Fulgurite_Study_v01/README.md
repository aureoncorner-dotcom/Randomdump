# Fulgurite first analysis — v0.1

CC0 · Anonymous · 8 September 2026.

Start with **Fulgurite_First_Results.md**.

This package contains an executed gas-archive design calculation, a replay of published phosphorus-summary arithmetic, a focused laboratory handoff, and snapshots of the two project documents used. It contains no new specimen measurements. All gas-model numbers are labeled illustrative assumptions.

Run the standard-library calculation:

```bash
python run_analysis.py
```

Run independent solver verification and regenerate the figure:

```bash
python run_analysis.py --verify --plot
```

The second command requires SciPy, NumPy and Matplotlib. No network or credentials are used by the analysis.

The included MANIFEST.sha256 covers all package files except itself. To check it where `sha256sum` is available:

```bash
sha256sum -c MANIFEST.sha256
```

Running the analysis may replace result files, which will then differ from the original manifest. Inputs and source snapshots are not modified by the runner.
