# player_detector.py
from ultralytics import YOLO

class PlayerDetector:
    def __init__(self, model_path='yolov8n.pt'):
        # Load YOLOv8 model
        self.model = YOLO(model_path)

    def detect_players(self, image):
        results = self.model(image)  # Run YOLOv8 on the image
        players = []
        for detection in results[0].boxes:
            if detection.cls == 'player':  # Ensure it's a player class
                players.append({
                    'bbox': detection.xyxy,  # Bounding box coordinates
                    'confidence': detection.conf,  # Confidence score
                    'class': detection.cls  # Class label (player)
                })
        return players
