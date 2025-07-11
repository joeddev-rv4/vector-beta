from core.config import settings
from openai import OpenAI
import logging

logger = logging.getLogger(__name__)

async def vector_chunk(chunk_str: str) -> list[float]:
    #Usa la api de OpenaIA para vectorizar cada chunk, puede ser un utils
    try:
        logger.info("========>    Inicio de procesamiento de data ")
        key = settings.OPENAI_API_KEY
        client = OpenAI(api_key=key)
        response = client.embeddings.create(
            model="text-embedding-ada-002",
            input=chunk_str
        )
        embedding = response.data[0].embedding
        
        return embedding
    except Exception as e:
        logger.error("====XXXX====>    Error para procesar data con OpenAI Error: " + e)
        return e
        
    