import cv2
import argparse
import json
import os
from ultralytics import YOLO
import tkinter as tk
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

WINDOW_NAME = "YOLO detection"

#carrega o modelo YOLOv8 pré-treinado
model = YOLO('yolov8n.pt')

parser = argparse.ArgumentParser('YOLO detection')
parser.add_argument('--output_folder', type=str, help='Pasta para saída YOLO', default='./output_yolo')
parser.add_argument('--input_video', type=str, help='Vídeo de entrada', default=None)
parser.add_argument('--alert_threshold', type=int, help='Limite de pessoas para alerta', default=None)

args = parser.parse_args()

#verifica se os parâmetros obrigatórios foram passados
if args.input_video is None or args.alert_threshold is None:
    parser.print_help()
    exit(1)

#limiar de alerta (alerta se >= 2 pessoas no frame)
alert_threshold = args.alert_threshold

#caminhos
input_video_path = args.input_video
output_directory = args.output_folder
os.makedirs(output_directory, exist_ok=True)

output_video_path = os.path.join(output_directory, 'output_with_detections.mp4') 
output_history_path = os.path.join(output_directory, 'history.json')
output_alerts_path = os.path.join(output_directory, 'alerts.json')

cap = cv2.VideoCapture(input_video_path)
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_size = (width, height)

#videoWriter para saída em MP4
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video_path, fourcc, fps, frame_size)

history = []
alerts = []

frame_id = 0


while True:
    ret, frame = cap.read()
    if not ret:
        break

    #detecção com YOLOv8
    results = model.predict(frame, conf=0.5, verbose=False)
    person_count = 0

    for result in results:
        boxes = result.boxes
        for box in boxes:
            cls_id = int(box.cls[0].item())
            confidence = float(box.conf[0].item())
            x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())

            if cls_id == 0:
                person_count += 1

                #bounding box no frame
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                label = f'Person: {confidence:.2f}'
                cv2.putText(frame, label, (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    #salva no history.json
    history.append({
        "id": frame_id,
        "count": person_count
    })

    #se for um frame que bate o alerta
    if person_count >= alert_threshold:
        alerts.append({
            "id": frame_id,
            "count": person_count
        })

    #mostra o frame()
    cv2.imshow(WINDOW_NAME, frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    #grava o frame no vídeo de saída
    out.write(frame)

    frame_id += 1

#salva os JSONs
with open(output_history_path, 'w') as f:
    json.dump(history, f, indent=4)

with open(output_alerts_path, 'w') as f:
    json.dump(alerts, f, indent=4)

#finalização
cap.release()
out.release()
cv2.destroyAllWindows()

print("Processamento finalizado!")
print(f"Vídeo salvo como: {output_video_path}")
print(f"History salvo como: {output_history_path}")
print(f"Alerts salvo como: {output_alerts_path}")
