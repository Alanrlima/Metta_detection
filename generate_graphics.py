import cv2
import json
import argparse
import tkinter as tk
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


parser = argparse.ArgumentParser('YOLO GUI')

parser.add_argument('--video_path', type=str, help='Caminho para o vídeo de saída', default='output_with_detections.mp4')
parser.add_argument('--history_json', type=str, help='Caminho para o history.json', default='history.json')

args = parser.parse_args()

with open(args.history_json, 'r') as f:
    history_data = json.load(f)

frame_ids = [frame['id'] for frame in history_data]
person_counts = [frame['count'] for frame in history_data]


root = tk.Tk()
root.title("Visualização: Detecção de Pessoas")

#frame para o vídeo
video_label = tk.Label(root)
video_label.pack()

#cria o gráfico Matplotlib
fig, ax = plt.subplots(figsize=(6, 3))
ax.plot(frame_ids, person_counts, marker='o')
ax.set_xlabel('Frame ID')
ax.set_ylabel('Número de Pessoas')
ax.set_title('Pessoas por Frame')
ax.grid(True)

#coloca o gráfico na GUI
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack()


cap = cv2.VideoCapture(args.video_path)

def update_frame():
    ret, frame = cap.read()
    if ret:
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame_rgb)
        imgtk = ImageTk.PhotoImage(image=img)
        video_label.imgtk = imgtk
        video_label.configure(image=imgtk)
        root.after(30, update_frame)
    else:
        cap.release()

update_frame()
root.mainloop()