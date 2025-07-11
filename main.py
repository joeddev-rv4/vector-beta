from fastapi import FastAPI
from core.config import settings
from api.v1.routes import router as api_v1_router
import uvicorn
import logging

# Configurar logging globalmente
logging.basicConfig(
    level=logging.DEBUG,  # DEBUG para capturar más detalles
    format="%(asctime)s %(levelname)s: %(name)s: %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S.%fZ",
    handlers=[
        logging.StreamHandler()  # Mostrar en consola
    ]
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="vector-beta",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.include_router(api_v1_router, prefix="/api/v1")

@app.on_event("startup")
async def startup():
    print("Starting app!")

@app.on_event("shutdown")
async def shutdown():
    print("App cerrando ...")

logger.info("Aplicación FastAPI iniciada")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)