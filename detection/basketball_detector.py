# basketball_detector.py
from detection.yolov5_model import YOLOv5Model

class BasketballDetector:
    def __init__(self, model_path):
        self.model = YOLOv5Model(model_path)

    def detect_basketball(self, image):
        detections = self.model.detect(image)
        basketball = detections[detections['class'] == 'basketball']
        return basketball[['xmin', 'ymin', 'xmax', 'ymax']]
