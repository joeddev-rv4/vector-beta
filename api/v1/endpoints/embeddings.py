from fastapi import APIRouter, Depends
from db.dependencies import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from models.embeddings_model import OuterArrayData
from services.embedding_service import start_embedding
from fastapi import HTTPException
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/create_lot")
async def chunks_development(
    payload: OuterArrayData,
    db: AsyncSession = Depends(get_db)
):
    try:
        response = await start_embedding(payload.data, db)
        return {
            "success": response["success"]
        }
    except Exception as e:
        print(e)
        return JSONResponse(
            status_code=400,
            content={"success": False, "error": str(e)}
        )