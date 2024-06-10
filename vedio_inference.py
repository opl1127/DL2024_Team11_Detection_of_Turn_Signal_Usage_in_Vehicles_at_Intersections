from ultralytics import YOLO
import cv2
import os

# 加載訓練好的模型
model = YOLO(
    'path/to/ultralytics/runs/detect/yolo_custom_model/weights/best.pt')

# 打開視頻文件
video_path = 'path/to/your/mp4'
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print(f"Error: Cannot open video file {video_path}")
    exit()

# 獲取視頻的幀率和幀大小
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 定義視頻寫入器
output_path = 'path/to/your/output_video.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # 使用模型進行推理
    results = model(frame)

    # 取得帶有檢測結果的圖像
    annotated_frame = results[0].plot()

    # 將結果寫入視頻文件
    out.write(annotated_frame)

    # 如果你想在窗口中顯示結果，取消以下註釋
    # cv2.imshow('YOLOv8 Inference', annotated_frame)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

# 釋放資源
cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Processed video saved at: {output_path}")
