from core.config import settings
from openai import OpenAI

async def vector_chunk(chunk_str: str) -> list[float]:
    #Usa la api de OpenaIA para vectorizar cada chunk, puede ser un utils
    key = settings.OPENAI_API_KEY
    client = OpenAI(api_key=key)
    response = client.embeddings.create(
        model="text-embedding-ada-002",
        input=chunk_str
    )
    embedding = response.data[0].embedding
    
    return embedding