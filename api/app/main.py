from fastapi import FastAPI
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import Response

app = FastAPI(title="BibleRAG API (skeleton)")

REQUESTS = Counter("api_requests_total", "Total API requests received")

@app.get("/healthz")
def health():
    return {"status": "ok"}

@app.get("/metrics")
def metrics():
    # Endpoint para Prometheus
    REQUESTS.inc()  # Cuenta cada hit a las métricas también
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

@app.get("/query")
def query(q: str = ""):
    REQUESTS.inc()
    return {
        "query": q,
        "answer": "RAG aún no implementado, esto es el esqueleto."
    }
