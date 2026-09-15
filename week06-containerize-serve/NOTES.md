# NOTES.md — Week 6: Containerize and Serve a Detector

**Student ID used with `generate_for_student.py`:**
<!-- paste the --student-id value you used -->
student_id: 112301042
seed: 2894764793

## Built image size

> [!QUESTION]
 What image size did `docker images` report for week6-detector?

The size of the docker image for week6-detector is **157 MB**.

```bash
$ docker images
REPOSITORY       TAG       IMAGE ID       CREATED          SIZE
week6-detector   latest    9093f58208a7   16 minutes ago   157MB
```

## Swapping in a real checkpoint

> [!QUESTION]
 What's the single biggest thing you'd change about this Dockerfile if
`src/mock_detector.py` were swapped for a real torch-based checkpoint?
(Think about what that does to build time and image size.)

I would use a smaller, inference-focused PyTorch base image (or otherwise separate the heavy PyTorch/model dependencies from the lightweight API image).
A real torch-based checkpoint would make the current python:3.13-slim image much larger and significantly increase Docker build time because of the PyTorch and related dependencies.