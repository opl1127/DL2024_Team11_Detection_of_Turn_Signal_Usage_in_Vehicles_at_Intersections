from ultralytics import YOLO

# 加載預訓練模型
model = YOLO('yolov8n.pt')  # 這會自動下載並加載YOLOv8 nano模型

# 開始訓練
model.train(data='data.yaml', epochs=50, imgsz=640,
            batch=16, name='yolo_custom_model')
