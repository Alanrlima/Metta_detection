# Detecção de Pessoas em Vídeo com YOLOv8 e Visualização Gráfica

Este projeto processa um vídeo de entrada para detectar pessoas utilizando a rede neural YOLOv8 pré-treinada. Ele gera:

- Um vídeo de saída com as detecções desenhadas.
- Dois arquivos JSON com estatísticas sobre a detecção.
- Uma interface gráfica (GUI) exibindo o vídeo e um gráfico de número de pessoas por frame.


## Requisitos

- Python 3.x
- Pacotes Python:

```bash
pip install -r requirements.txt
```

### Rodar programa

Para rodar o código de dectecção YOLO, use o seginte comando:


```bash
python3 main.py --input_video people-walking.mp4 --alert_threshold 2
python3 generate_graphics.py --history_json output_yolo/history.json --video_path output_yolo/output_with_detections.mp4
```