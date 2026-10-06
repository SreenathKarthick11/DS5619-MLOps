# Lab 9 : Orchestrated Batch Scoring

## Overview

This lab implements a **small local DAG orchestrator** for batch vehicle scoring. It demonstrates **task dependency management, topological execution, task-level retries, and shared context between tasks**.

> This file captures the main implementation steps and results from the lab.

---

## Implementation

The implementation contains three functions:

### Topological Order

* Computes the dependency count for every task.
* Uses **Kahn's algorithm** to determine a valid execution order.
* Detects missing dependencies and dependency cycles by raising `ValueError`.

### Task Retry

* Runs the task function using the provided context.
* Retries a failed task up to `max_retries` additional times.
* Uses `time.sleep` between retry attempts.
* Returns the number of attempts taken when the task succeeds.
* Re-raises the last exception if all retry attempts fail.

### DAG Execution

* Computes the task execution order using `topological_order`.
* Passes the **same context dictionary** to every task so that downstream tasks can access upstream results.
* Records the status and number of attempts for every successful task.
* Stops execution when a task fails after all retries are exhausted.

---

## Pipeline Results

Ran the pipeline using:

```bash
python3 src/run_pipeline.py
```

The `notify` task failed on its first two attempts and succeeded on the third attempt:

```text
Notify attempts = 3
Status = success
```

The `load` task still succeeds because `load` and `notify` are independent branches that both depend only on `score`.

The run summary was written to [dag_run_summary.json](dag_run_summary.json) and the batch scoring report was written to [batch_report.json](batch_report.json)

---
## Verification

Ran the test suite using:

```bash
pytest tests/ -q
```

> [!NOTE]
> The answer to the question in README written in [NOTES.md](NOTES.md).

---
