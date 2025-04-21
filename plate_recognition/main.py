from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n.yaml')  # Load a pretrained YOLOv8n model

# Use the model
results = model.train(data='config.yaml', epochs=1)