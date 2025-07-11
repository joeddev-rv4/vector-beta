from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from utils.db_utils import return_data, return_date
from models.rag_model import FAQResponse
import logging

logger = logging.getLogger(__name__)

async def get_embedding_data(db, embedding: list[float]):
    try:
        logger.error("========>  INICIA Consulta Postgres")  
        vector_str = "[" + ",".join(str(x) for x in embedding) + "]"
        result = await db.execute(text("""
            SELECT
                category,
                chunk
            FROM lared_vectors.faqs
            ORDER BY embedding <-> :embedding ::vector
            LIMIT 5
        """),{
            "embedding": vector_str
        })
        await db.commit()
        rows = result.mappings().all()
        return [FAQResponse(**row) for row in rows]
    except Exception as e:
        logger.error("====XXXX====>    Error para procesar data CONSULTA POSTGRES Error: " + str(e))
        return e