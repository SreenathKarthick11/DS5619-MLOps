# Lab 7 - CI/CD Integration Testing

## Overview

This lab implements CI/CD and integration testing for the vehicle detection application using **GitHub Actions**.

> This file captures the main implementation steps and results from the lab.

---

## Implementation

First the inital setup as mentioned in the [README](README.pdf).


### CI Workflow

First, completed the TODOs in:

```text
week07-cicd/.github/workflows/ci.yml
```

The workflow contains three jobs:

* **lint** - runs `flake8 src`.
* **unit-test** - runs `pytest -q`.
* **integration-test** - runs the Docker-based integration test.

The integration test uses:

```
needs: ["lint", "unit-test"]
```

so it only runs after linting and unit tests pass.

### Integration Test

Completed:

```text
week07-cicd/scripts/integration_test.sh
```

The script:

* Builds the Docker image.
* Runs the container.
* Waits for the `/health` endpoint.
* Tests `/detect` using the generated fixture image.
* Checks for `"detections"` in the response.
* Cleans up the container.



### GitHub Actions

The original workflow was inside:

```text
week07-cicd/.github/workflows/ci.yml
```

Since GitHub Actions only detects workflows from the repository's root `.github/workflows/` directory, I copied the workflow to:

```text
.github/workflows/week7-ci.yml
```

and added:

```yaml
defaults:
  run:
    working-directory: week07-cicd
```

This allows the root workflow to run the Week 7 CI commands from the correct directory.

> [!NOTE]
> The answer to the question in README written in [NOTES.md](NOTES.md).

---

## Verification

Tested the integration script locally using:

```bash
chmod +x scripts/integration_test.sh
./scripts/integration_test.sh
```
> [!NOTE]
> Test the Github Action is written in [CI Verfication](week07-cicd/CI_VERIFICATION.md).

The CI pipeline then runs the lint, unit-test, and integration-test jobs through GitHub Actions.

---