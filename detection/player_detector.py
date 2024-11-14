# player_detector.py
from detection.yolov5_model import YOLOv5Model

class PlayerDetector:
    def __init__(self, model_path):
        self.model = YOLOv5Model(model_path)

    def detect_players(self, image):
        detections = self.model.detect(image)
        players = detections[detections['class'] == 'player']
        return players[['xmin', 'ymin', 'xmax', 'ymax', 'team', 'number']]
