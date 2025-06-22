# Detecção de Pessoas em Vídeo com YOLOv8 e Visualização Gráfica

Este projeto processa um vídeo de entrada para detectar pessoas utilizando a rede neural YOLOv8 pré-treinada. Ele gera:

- Um vídeo de saída com as detecções desenhadas.
- Dois arquivos JSON com estatísticas sobre a detecção.
- Uma interface gráfica (GUI) exibindo o vídeo e um gráfico de número de pessoas por frame.


## Requisitos

* Python **3.8 ou superior**
* Pacotes Python listados no arquivo `requirements.txt`

### Criar um ambiente virtual (recomendado)

Para isolar as dependências do projeto, recomenda-se criar e ativar um ambiente virtual:

```bash
# Criar o ambiente virtual
python3 -m venv venv
```

Ativação do ambiente virtual:

```bash
# No Windows:
venv\Scripts\activate

# No Linux/Mac:
source venv/bin/activate
```

### Instalar as dependências

Após ativar o ambiente virtual, instale os pacotes necessários:

```bash
pip install -r requirements.txt
```

---

## Como executar o programa

### Etapa 1: Rodar a detecção com YOLOv8

```bash
python3 main.py --input_video ./videos/people-walking.mp4 --alert_threshold 2
```

Esse comando irá processar o vídeo de entrada e gerar:

* Um vídeo de saída com as detecções (`output_yolo/output_with_detections.mp4`)
* Arquivos JSON com o histórico de detecções

---

### Etapa 2: Visualizar o vídeo com o gráfico de detecções por frame

```bash
python3 generate_graphics.py --history_json output_yolo/history.json --video_path output_yolo/output_with_detections.mp4
```
