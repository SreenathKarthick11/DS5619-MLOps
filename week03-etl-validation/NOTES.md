# NOTES.md — Week 3: ETL and Data Validation

**Student ID used with `generate_for_student.py`:**
- student_id: 112301042
- seed: 466663220


## Quarantine count vs. the 7 known injected problems

There were **6 quarantined rows out of 600 transactions**, leaving **594 clean transactions**. This does not match the **7 known injected problems** exactly because some rows violate more than one expectation. In particular, rows **209 and 237** each violate both the `not_null` and `positive` expectations, so the 8 total expectation violations correspond to only 6 distinct problematic rows. Thus, the quarantine count is **6**, while the validation report records **8 violations across the expectations**.

### Table overview

| Expectation              | Violations | Affected Rows       |
| ------------------------ | ---------- | ------------------- |
| `expect_column_not_null` |          3 | 209, 237, 234       |
| `expect_column_positive` |          3 | 209, 237, 493       |
| `expect_column_in_set`   |          1 | 361                 |
| `expect_column_unique`   |          1 | 254                 |
| **Total**                |      **8** | **6 distinct rows** |

