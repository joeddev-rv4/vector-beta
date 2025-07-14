from sqlalchemy import text
from models.rag_model import FAQResponse
import logging

logger = logging.getLogger(__name__)

async def get_embedding_data(db, embedding: list[float]):
    try:
        logger.info("========>  INICIA Consulta Postgres")  
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
        rows = result.mappings().all()
        return [FAQResponse(**row) for row in rows]
    except Exception as e:
        logger.error("====XXXX====>    Error para procesar data CONSULTA POSTGRES Error: " + str(e))
        return e