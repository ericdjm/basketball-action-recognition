# basketball_detector.py
from ultralytics import YOLO

class BasketballDetector:
    def __init__(self, model_path='yolov8n.pt'):
        # Load YOLOv8 model
        self.model = YOLO(model_path)

    def detect_basketball(self, image):
        results = self.model(image)  # Run YOLOv8 on the image
        basketball = []
        for detection in results[0].boxes:
            if detection.cls == 'basketball':  # Ensure it's a basketball class
                basketball.append({
                    'bbox': detection.xyxy,
                    'confidence': detection.conf,
                    'class': detection.cls
                })
        return basketball
