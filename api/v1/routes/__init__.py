from fastapi import APIRouter
from api.v1.endpoints import users
from api.v1.endpoints import embeddings
from api.v1.endpoints import rag

router = APIRouter()

router.include_router(users.router, prefix="/users", tags=["Users"])
router.include_router(embeddings.router, prefix="/embd", tags=["Embeddings"])
router.include_router(rag.router, prefix="/rag", tags=["Rags"])
