# NOTES.md — Week 6: Containerize and Serve a Detector

**Student ID used with `generate_for_student.py`:**
<!-- paste the --student-id value you used -->
Student_id : 112301042

## Built image size

> [!QUESTION] QUESTION
> What image size did `docker images` report for week6-detector?

The size of the docker image for week6-detector is **157 MB**.

```bash
$ docker images
REPOSITORY       TAG       IMAGE ID       CREATED          SIZE
week6-detector   latest    9093f58208a7   16 minutes ago   157MB
```

## Swapping in a real checkpoint

> [!QUESTION] QUESTION
 What's the single biggest thing you'd change about this Dockerfile if
`src/mock_detector.py` were swapped for a real torch-based checkpoint?
(Think about what that does to build time and image size.) 

