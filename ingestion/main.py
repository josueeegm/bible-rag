import os
import time
import requests
from pathlib import Path

# =====================================
# Configuración (usando variables de entorno)
# =====================================

ENDPOINT = os.getenv("DOC_INTELLIGENCE_ENDPOINT")
KEY = os.getenv("DOC_INTELLIGENCE_KEY")

PDF_FOLDER = "/pdfs"        # carpeta donde irán los PDFs
OUTPUT_PATH = "/output/combined.txt"  # archivo donde guardaremos el texto final

# =====================================
# Función: procesar un PDF con Document Intelligence
# =====================================
def process_pdf(pdf_path):
    print(f"Procesando PDF: {pdf_path}")

    url = f"{ENDPOINT}/documentModels/prebuilt-read:analyze?api-version=2024-02-29-preview"

    with open(pdf_path, "rb") as f:
        file_bytes = f.read()

    headers = {
        "Ocp-Apim-Subscription-Key": KEY,
        "Content-Type": "application/pdf"
    }

    response = requests.post(url, headers=headers, data=file_bytes)

    if response.status_code != 200:
        print(f"Error analizando PDF: {response.text}")
        return ""

    result = response.json()
    content = result.get("content", "")
    
    print(f"Texto extraído ({len(content)} caracteres)")
    return content


# =====================================
# MAIN
# =====================================
def main():
    print("==== INGESTION JOB INICIADO ====")

    if not ENDPOINT or not KEY:
        print("ERROR: Falta DOC_INTELLIGENCE_ENDPOINT o DOC_INTELLIGENCE_KEY")
        return

    pdf_files = list(Path(PDF_FOLDER).glob("*.pdf"))

    if not pdf_files:
        print(f"No se encontraron PDFs en {PDF_FOLDER}")
        return

    full_text = ""

    for pdf in pdf_files:
        extracted = process_pdf(pdf)
        full_text += extracted + "\n\n"

    # Guardar el texto combinado
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(full_text)

    print(f"Texto combinado guardado en: {OUTPUT_PATH}")
    print("==== INGESTION JOB FINALIZADO ====")


if __name__ == "__main__":
    main()
