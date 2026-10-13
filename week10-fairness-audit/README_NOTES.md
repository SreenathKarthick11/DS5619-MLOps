# Lab 10 : Fairness and Robustness Audit

## Overview

This lab implements a **class-based performance disparity audit** and an **adversarial robustness check** for a vehicle detector.

> This file captures the main implementation steps and results from the lab.

---

## Implementation

The implementation contains seven functions across `fairness_audit.py` and `adversarial.py`.

### `compute_iou`

* Converts bounding boxes from `[x, y, w, h]` to corner coordinates.
* Calculates intersection and union areas.
* Returns the IoU score, handling zero union safely.

### `match_ground_truth`

* Compares each ground-truth box with all detections.
* Uses the IoU threshold to determine whether a box was detected.
* Returns a Boolean list indicating which ground-truth boxes were found.

### `audit_by_category`

* Loads COCO annotations and groups them by image and category.
* Runs the detector once per image and matches ground-truth boxes.
* Calculates total boxes, detected boxes, and recall for each category.

### `find_underperforming_categories`

* Identifies categories whose recall is below the specified threshold.
* Sorts the results from lowest recall to highest.
* Returns category names and their recall values.

### `perturb_image`

* Lowers red-channel values and raises green and blue values by `eps`.
* Clamps pixel values to the range `[0, 255]`.
* Returns a new RGB image without modifying the original.

### `audit_under_attack`

* Runs the category audit at multiple perturbation budgets.
* Uses the image transformation argument to perturb images before detection.
* Stores per-category recall results for each epsilon value.

### `find_most_fragile`

* Calculates recall drop between clean images and attacked images.
* Ranks categories by the largest recall decrease.
* Uses alphabetical order to break ties and returns the top k categories.

---

## Pipeline Results

Ran the pipeline using:

```bash
python3 src/run_pipeline.py
```

The clean audit flagged two categories below the 90% recall threshold:

```text
Bicycle      = 62.5% (10/16)
Two-wheeler  = 85.7% (12/14)
```

At `eps = 20`, the most fragile categories were:

```text
Bicycle = 38 percentage-point recall drop
Bus     = 36 percentage-point recall drop
Truck   = 31 percentage-point recall drop
```

The lowest-recall categories at the same budget were Bicycle (25%), Two-wheeler (64%), and Bus (64%).

The pipeline generated [fairness_report.json](fairness_report.json).

---

## Verification

Ran the test suite using:

```bash
pytest tests/ -q
```

```text
13 passed in 5.35s
```

> [!NOTE]
> See [NOTES.md](NOTES.md) for the student ID, interpretation of flagged categories, fairness considerations, attack analysis, and discussion of SHAP/LIME limitations and possible mitigations.

---