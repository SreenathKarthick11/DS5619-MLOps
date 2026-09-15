# Lab 6 - Containerize and Serve a Detector

## Overview

This lab implements and containerizes a small **vehicle detection inference API** using Flask and Docker.


> This file captures the steps of implementation and the main results from the lab.

---
## Implementation of Task

### Setup

Followed the instructions in the [README](README.pdf) for the initial configuration of the lab.

Generated the personalized CCTV fixture images using my student ID.

The lab uses `mock_detector.py` as a lightweight stand-in for a real vehicle detection checkpoint.

### Image Upload Handling

Implemented `load_image_from_upload()` to convert an uploaded file into a PIL Image.

The implementation:

* Reads the uploaded file using `file_storage.read()`.
* Opens the image using `Image.open()`.
* Converts the image to RGB using `.convert("RGB")`.

This ensures that uploaded images are converted into the RGB format expected by the detector.

### Detector Inference

Implemented `run_detection()` to run the detector on the uploaded image.

The implementation:

* Calls `det.detect(image)` to obtain the detections.
* Calculates the number of detections.
* Converts the detections into COCO-style annotation dictionaries using `det.detections_to_coco()`.
* Uses `image_id=0` because the API processes one image per request.

The resulting response contains the detection count and a list of detections.

### `/detect` Endpoint

Implemented the `/detect` POST route to connect the uploaded image to the detector.

The implementation:

* Checks whether a file exists under the key `"image"`.
* Returns a `400` response if the file is missing.
* Loads the image using `load_image_from_upload()`.
* Runs the detector using `run_detection()`.
* Returns the result as JSON.

This completes the inference API required by the lab.

### Docker Implementation

Completed the Dockerfile using the official `python:3.13-slim` base image.

The implementation:

* Copies and installs the dependencies from `requirements.txt`.
* Copies the `src/` directory into the image.
* Exposes port `8080`.
* Starts the Flask application using `python3 src/app.py`.


> [!NOTE]
> The answer to the question in README written in [NOTES.md](NOTES.md).

---

## Verification

The Flask application can be tested locally using:

```bash
python src/app.py
```

The Docker image can be built using:

```bash
docker build -t week6-detector .
```

The container can be started using:

```bash
docker run --rm -p 8080:8080 week6-detector
```

The `/health` and `/detect` endpoints were successfully tested against the running container.
