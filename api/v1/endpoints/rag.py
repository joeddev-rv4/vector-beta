from fastapi import APIRouter, Depends
from db.dependencies import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from models.rag_model import Item, FAQResponse
from services.rag_service import start_rag_proc
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from typing import List

router = APIRouter()

@router.post("/process-data", response_model=List[FAQResponse])
async def rag_proc(
    payload: Item,
    db: AsyncSession = Depends(get_db)
):
    try:
        result = await start_rag_proc(payload.message, db)
        
        return result
    except Exception as e:
        print(e)
        return JSONResponse(
            status_code=400,
            content={"success": False, "error": str(e)}
        )