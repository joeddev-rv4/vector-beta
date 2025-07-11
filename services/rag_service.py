from repositories.rag_repository import get_embedding_data
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from db.dependencies import get_db
from utils.embedding_utils import vector_chunk
import logging

logger = logging.getLogger(__name__)



async def start_rag_proc(message: str, db: AsyncSession):
    #proceso de rag que devuelve un prompt para poder hacer la consulta
    #al agente.
    logger.info("========>    Inicio de embedding. Message: " + message)
    embedding_message = await vector_chunk(message)
    result = await get_embedding_data(db, embedding_message)
    return(result)