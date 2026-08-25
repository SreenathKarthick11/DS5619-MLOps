# Lab 4 - Versioning, Feature Store & Lineage

## Overview

This lab implements a small, local feature store to demonstrate **data versioning, feature groups, schema evolution, and data lineage**.

> This file, captures the steps of implementation in the lab.

## Implementation of Task

### Setup

Followed the instructions of the [README](README.md) for the intial configiuration of the lab work.


### Raw Data Versioning

Implemented hash-based versioning for the transaction data.

* Computes a **hash** of the input CSV.
* Assigns incremental versions (`v1`, `v2`, ...).
* Stores metadata in `manifest.json`.
* Re-snapshotting identical data returns the existing version, hence **idempotent**.
* Records the source path, hash, columns, row count, and creation time.

### Building a feature store

Implemented card-level transaction aggregation for both schema versions.

For each `card_id`, the following features are generated:

* `txn_count`
* `avg_amount`
* `max_amount`
* `pct_card_present`
* `event_time`

The implementation handles the v1 -> v2 schema change by converting:

```text
amount_minor_units / 100
```

to obtain the same monetary unit as the v1 `amount` field. This keeps the generated features comparable across versions.

### Feature Group Versioning

Implemented feature group registration for `card_activity`.

Each registration creates a new version instead of overwriting an existing one.

Each version contains:

* `features.json` : generated feature rows
* `manifest.json` : feature group metadata and lineage information

### Data Lineage

Implemented lineage lookup that connects a feature group version back to the exact raw data version used to create it.


The resulting lineage is written to `lineage_report.json`.

## Versioning Result

The pipeline successfully maintains separate versions for the two schema revisions.

| data          | v1               | v2               |
|---------------|------------------|------------------|
| Raw           | 500 transactions | 125 transactions |
| Card activity | 367 transactions | 117 transactions |

> [!note]
 The feature row count is smaller because `build_features()` produces **one row per distinct `card_id`**, rather than one row per transaction.

## Verifcation

The self-check can be run with:

```bash
pytest  -q
```

And the complete pipeline can be run with:

```bash
python3 src/run_pipeline.py
```
