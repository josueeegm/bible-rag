FROM python:3.11-slim

WORKDIR /work

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Creamos las carpetas donde montaremos los PDFs y salida
RUN mkdir -p /pdfs /output

# Variables que recibiremos desde el Job (AKS)
ENV DOC_INTELLIGENCE_ENDPOINT=""
ENV DOC_INTELLIGENCE_KEY=""

CMD ["python", "main.py"]
