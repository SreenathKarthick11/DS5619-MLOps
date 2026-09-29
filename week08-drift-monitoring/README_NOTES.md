# Lab 8 : Drift and Observability Monitoring

## Overview

This lab implements **ML drift monitoring** for the vehicle detection application using **confidence-score distributions and Population Stability Index (PSI)**.

> This file captures the main implementation steps and results from the lab.

---

## Implementation

The implementation contains four functions:

### Confidence Score Extraction

* Loads every `.jpg` image from the camera directory.
* Runs the provided `mock_detector`.
* Collects the confidence score of every detection.
* Returns all confidence scores as a flat list.

Images are processed in sorted order to ensure deterministic results.

### Population Stability Index

* Divides confidence scores in `[0, 1]` into equal-width bins.
* Computes the proportion of scores in each bin.
* Applies the `1e-4` minimum proportion to avoid zero divisions and `log(0)`.
* Computes PSI using the reference and live distributions.

### Drift Classification

use the given PSI thresholds:

```text
PSI < 0.10       -> none
0.10 <= PSI < 0.25 -> moderate
PSI >= 0.25      -> significant
```

### Score Summary

Implemented which reports:

* count
* mean
* standard deviation
* minimum
* maximum

The single-value case is handled by returning `std = 0.0`.

---

## Pipeline Results

Ran the pipeline using:

```bash
python3 src/run_pipeline.py
```

The calculated PSI was:

```text
PSI = 0.1189
drift level = moderate
```

The report was written to:

```text
drift_report.json
```

The moderate drift is expected because the two camera conditions were deliberately generated with different visual statistics.

---

## Verification

Ran the test suite using:

```bash
pytest tests/ -q
```

---

