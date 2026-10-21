# Lab 11: Model Compression Benchmark

## Overview

This lab implements **magnitude-based pruning** and **INT8 quantization** to study model compression for a linear classifier representing a vehicle detector's classification head.

> This file captures the main implementation steps and results from the lab.

---

## Implementation

The implementation contains five functions in `compression.py`.

### `model_size_bytes`

* Calculates dense model storage using the number of weights and bytes per weight.
* Supports comparing representations such as FP32 and INT8.

### `prune_weights`

* Ranks weights by their absolute magnitude.
* Sets the specified fraction of smallest-magnitude weights to zero.
* Returns a new list without modifying the original weights.

### `sparse_coo_size_bytes`

* Counts nonzero weights in the pruned model.
* Calculates storage using the combined cost of each value and its index.
* Demonstrates how sparse storage can reduce model size compared with dense storage.

### `quantize_int8`

* Applies symmetric linear quantization using a scale of `max(abs(weights)) / 127`.
* Rounds and clamps quantized values to the range `[-127, 127]`.
* Handles all-zero weights without division by zero.

### `benchmark_model`

* Measures model size and classification accuracy against the evaluation dataset.
* Measures average inference latency across repeated passes.
* Returns the results for comparing compression techniques.

---

## Pipeline Results

Ran the pipeline using:

```bash
python src/run_pipeline.py
```

The pipeline generated [compression_report.json](compression_report.json).

---

## Verification

Ran the test suite using:

```bash
pytest tests/ -q
```

All tests passed.

> [!NOTE]
> See [NOTES.md](NOTES.md) for the student ID used to generate the dataset, the dense-versus-sparse storage comparison, and the interpretation of the sparsity experiment.

---
