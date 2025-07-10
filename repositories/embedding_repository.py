from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from utils.db_utils import return_data, return_date


async def get_all_users(db: AsyncSession):
    users = await db.execute(text(
        "SELECT * FROM lared_vectors.users"
    ))
    data = await return_data(users)
    return data

async def create_embedding(db,embedding: list[float], category: str, chunk: str ):
    created_at = await return_date()
    embedding_str = f"[{', '.join(map(str, embedding))}]"
    result = await db.execute(text(f"""
        INSERT INTO lared_vectors.faqs(
            embedding,
            category,
            created_at,
            chunk
        )
        VALUES(
            :embedding,
            :category,
            :created_at,
            :chunk
        )
    """),{
        "embedding": embedding_str,
        "category": category,
        "created_at": created_at,
        "chunk": chunk
    })
    await db.commit()
    return result