# yolov5_model.py
import torch

class YOLOv5Model:
    def __init__(self, model_path='yolov5s.pt'):
        self.model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path)

    def detect(self, image):
        results = self.model(image)
        return results.pandas().xyxy[0]  # Returns detection results as a DataFrame
