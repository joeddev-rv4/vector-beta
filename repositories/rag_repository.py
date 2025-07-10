from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from utils.db_utils import return_data, return_date
from models.rag_model import FAQResponse

async def get_embedding_data(db, embedding: list[float]):
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