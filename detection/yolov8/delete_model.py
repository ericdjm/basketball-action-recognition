from ultralytics import YOLO
import torch
import gc
import os

# Load the model
model_path = 'yolov8n.pt'
model = YOLO(model_path)
print("Model loaded into memory")

# Perform any operations with the model here
# For example: results = model('path/to/image.jpg')

# Delete the model from memory
del model
torch.cuda.empty_cache()
gc.collect()
print("Model deleted from memory")

# Delete the model file from disk
if os.path.exists(model_path):
    os.remove(model_path)
    print(f"File {model_path} has been deleted from disk.")
else:
    print(f"File {model_path} does not exist.")
