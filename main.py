from fastapi import FastAPI
from core.config import settings
from api.v1.routes import router as api_v1_router
import uvicorn

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

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)