# Sobre o Projeto: Detecção de Pessoas com YOLOv8 e Visualização Gráfica

## Objetivo

Desenvolver uma aplicação capaz de processar um vídeo, detectar pessoas frame a frame utilizando a rede neural YOLOv8 pré-treinada e apresentar os resultados de forma estruturada e visual.

---

## Abordagem Técnica

1. **Detecção com YOLOv8:**  
Foi utilizada a versão `yolov8n.pt` da rede YOLOv8, adequada para bom desempenho em máquinas com CPU. O modelo realiza a detecção de pessoas (classe 0 do dataset COCO).

2. **Processamento de Vídeo com OpenCV:**  
O código lê o vídeo de entrada frame a frame, aplica as detecções e desenha as caixas delimitadoras (bounding boxes) nas pessoas identificadas.

3. **Geração de Saídas em JSON:**  
- **`history.json`**: Contagem total de pessoas detectadas em cada frame ao longo do vídeo.  
- **`alerts.json`**: Lista apenas os frames onde a quantidade de pessoas atinge ou supera o limiar definido pelo usuário (`alert_threshold`).

4. **Geração do Vídeo de Saída:**  
O vídeo de saída (`output_with_detections.mp4`) contém todos os frames processados com as detecções visíveis (caixas nas pessoas detectadas).

5. **Interface Gráfica (GUI) com Tkinter e Matplotlib:**  
A aplicação abre uma interface que exibe:  
- A reprodução do vídeo de saída com as detecções.  
- Um gráfico (Frame ID vs. Número de Pessoas), gerado com Matplotlib, apresentando a quantidade de pessoas ao longo do tempo.

---

## Justificativa das Escolhas Tecnológicas

- **YOLOv8:** Escolhido por ser uma das arquiteturas de detecção de objetos mais rápidas e precisas da atualidade, com boa eficiência mesmo em máquinas com recursos limitados (como apenas CPU).

- **OpenCV:** Biblioteca consolidada e eficiente para processamento de vídeo e manipulação de imagens em Python.

- **Tkinter:** Framework leve, integrado ao Python, ideal para construção de interfaces gráficas simples e eficazes.

- **Matplotlib:** Biblioteca robusta para visualização de dados em forma de gráficos, com boa integração com Tkinter.

---

## Conclusão

A solução final atende ao objetivo proposto: realizar detecção de pessoas em vídeo, gerar estatísticas analíticas e apresentar os resultados de maneira visual e interativa para o usuário final.