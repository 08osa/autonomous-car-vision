# Autonomous Car with Computer Vision

Low-cost, modular prototype of a self-driving car for education: a **Raspberry Pi 3** with a USB webcam does real-time lane detection and basic traffic-sign recognition with image processing, and drives the wheel motors through an L298N H-bridge.

## What is in this repository
- `hardware/` - Fritzing wiring schematic
- `media/` - photos of the built car and test-run videos
- `src/` - computer-vision helpers and experiments:
  - `util.py` - `get_limit()` computes HSV lower/upper bounds for a BGR colour (used for colour-based detection)
  - `main.py` - MediaPipe face-detection experiment (`models/blaze_face_short_range.tflite`)

The full project report and slides, and the long control-course demo video, are not published here (they contain personal data / are too large).
The car's driving code is not part of this repository.

## Run the experiments
```bash
pip install -r requirements.txt
python src/main.py path/to/image.jpg
```
