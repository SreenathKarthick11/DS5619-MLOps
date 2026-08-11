# NOTES.md — Week 2: Config-Driven Data Pipelines

**Student ID used with `generate_for_student.py`:**

> student_id: 112301042 \
> seed: 843794033


## What was hardcoded, and what would switching it have required?


In the original `pipeline_hardcoded.py`, several configuration values were hardcoded directly in the source code:

* `INPUT_PATH = "data/v1/transactions.csv"`
* `HIGH_VALUE_THRESHOLD = 5000`
* `OUTPUT_PATH = "data/v1/report_hardcoded.json"`

The input format was also effectively hardcoded to CSV because the program always used `load_csv()` and `csv.DictReader`.
Hence the pipeline can only process CSV files.

To change the threshold, or any of the other hardcoded values, one would have to modify the source code directly and re-run the script. This is not ideal for maintainability or flexibility.

Switching from CSV to JSON would require changes to the loading logic because CSV and JSON represent the transaction data differently. In the CSV version, `is_fraud` is read as a string such as `"True"` or `"False"`, so the original code uses `.lower() == "true"` to determine whether a transaction is fraudulent. In JSON, the corresponding value is a boolean `true` or `false`, which is loaded by Python as `True` or `False`. Therefore, the JSON version needs to check the boolean value directly rather than calling `.lower()`.

The refactored pipeline moves the input path, input format, threshold, and output path into the YAML configuration. It also supports both CSV and JSON parsing and handles their different representations of the `is_fraud` field. As a result, changing the threshold, switching between CSV and JSON, or changing the input/output paths can be done through the configuration file without modifying the pipeline code.
