"""Face-detection experiment with MediaPipe (first step of a face-blur pipeline).

Usage: python src/main.py path/to/image.jpg
"""
import sys

import cv2
import mediapipe as mp


def detect_faces(image_path: str):
    img_bgr = cv2.imread(image_path)
    if img_bgr is None:
        raise FileNotFoundError(f"Could not read image: {image_path}")

    mp_face_detection = mp.solutions.face_detection
    with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as detector:
        # MediaPipe expects RGB, OpenCV loads BGR
        result = detector.process(cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB))
    return result.detections


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    print(detect_faces(sys.argv[1]))
    # TODO: blur the detected regions and save the output image
