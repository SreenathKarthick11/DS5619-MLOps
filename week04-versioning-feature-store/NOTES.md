# NOTES.md — Week 4: Versioning, Feature Store & Lineage

**Student ID used with `generate_for_student.py`:**

> student_id: 112301042
> seed: 831418785


## v1 vs. v2 manifest comparison

* **v1** has `amount` and `country`.
* **v2** replaces these with `amount_minor_units` and `country_code`, and adds `device_fingerprint`.
* The content hashes are different, confirming they are different raw versions.
* v1 has **500 rows**, while v2 has **125 rows**.
* The `version_id` and `source_path` also differ.

Here are the link to the `manifest.json` of the raw versions
- [v1 manifest.json](.feature_store/raw_versions/v1/manifest.json)
- [v2 manifest.json](.feature_store/raw_versions/v2/manifest.json)


## Why treat amount_minor_units differently from amount?

`amount` in v1 is already represented in the normal currency unit, while `amount_minor_units` in v2 represents the amount in **minor units (cents)**. For example, `100.0` in v1 corresponds to `10000` minor units in v2.

Therefore, `build_features()` divides `amount_minor_units` by **100** before performing aggregation. This ensures that `avg_amount` and `max_amount` are calculated using the **same scale** in both versions. Without this conversion, v2 amounts would be 100 times larger, causing the generated features to be incorrect and making v1 and v2 feature values **not comparable**.


