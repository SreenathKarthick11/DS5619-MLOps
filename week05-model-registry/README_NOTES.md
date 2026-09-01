# Lab 5 - Model Registry Governance

## Overview

This lab implements a small local model registry to demonstrate **model versioning, model cards, governance gates, model promotion, and production tracking**.

> This file captures the steps of implementation and the main results from the lab.

## Implementation of Task

### Setup

Followed the instructions in the [README](README.md) for the initial configuration of the lab.

Generated the two model candidates using my student ID as specified in the README.

* Student ID: `112301042`
* Candidate A: F1 = `0.518`
* Candidate B: F1 = `0.932`

Candidate A does not meet the production F1 threshold of `0.70`, while Candidate B does.

### Model Registration

Implemented `register_model()` to register each trained model as a separate version in the registry.

The implementation:

* Creates a new version such as `v1`, `v2`, etc.
* Does not overwrite an existing model version.
* Copies the model data into `model.json`.
* Stores the model metrics and other metadata in `manifest.json`.
* Initially sets the model stage to `"None"`.
* Records the creation time.

This allows each registered model to be tracked separately in the registry.

### Model Card

Implemented `generate_model_card()` to create a model card for a registered model.

The model card requires the following fields:

* `intended_use`
* `training_data`
* `limitations`
* `ethical_considerations`

The implementation checks that:

* Required fields are present.
* Fields are not empty.
* Fields do not contain `"TODO"`.

The metrics are also taken from the model's existing `manifest.json` and included in the model card.

For this fraud detection model, the model card describes that the model is based on an **amount threshold** and also mentions its limitation of not considering multiple smaller transactions together.

### Model Promotion and Governance Gate

Implemented `promote_model()` to control the movement of models between stages.

A model can be promoted to **Staging** without the production checks.

However, promotion to **Production** requires both:

1. A valid `model_card.json` must exist.
2. The model's F1 score must be at least `0.70`.

The function raises a `GovernanceError` when either condition is not satisfied.

This makes the production requirements an actual gate in the code rather than just a documented rule.

### Production Model Handling

When a new model is promoted to Production, the previous Production model is automatically moved to `"Archived"`.

This ensures that there is only one model marked as Production at a time.

The promotion is also recorded in the model's `history`, including:

* Previous stage
* New stage
* Time of promotion

This provides a simple audit trail of model stage changes.

### Production Lookup

Implemented `get_production_model()` to find the model version that is currently in Production.

The function scans the registered versions and returns the manifest of the version whose stage is `"Production"`.

If no model is currently in Production, it returns `None`.

This provides a direct way to answer which model is currently deployed without relying on external records or memory.


>[!Note]
The questions regarding the Production promotion result, handling stale feature data, and handling a larger number of model candidates are answered separately in [NOTES.md](NOTES.md).


## Verification

The self-check can be run with:

```bash
pytest tests/ -q
```

The complete pipeline can be run with:

```bash
python src/run_pipeline.py
```

The pipeline produces the model registry and `registry_summary.json`, showing which model is currently in Production. So in our case it would be `candidate B`.
