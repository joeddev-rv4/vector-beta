from fastapi import APIRouter, Depends
from models.embeddings_model import OuterArrayData, Item
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from db.dependencies import get_db
from core.config import settings
from openai import OpenAI
from repositories.embedding_repository import create_embedding
from utils.embedding_utils import vector_chunk

async def create_embedding_db(db, chunk_description: str, chunk_vector: str, category: str):
    #Crea vector en la BD
    vector_insert = await create_embedding(db, chunk_vector, category, chunk_description)
    return vector_insert

async def embedding_process(db,item: Item, model: str):
    #Recibe un solo chunk para procesarlo:
    #   - Crea el vector con vector_chunk
    #   - Recibe el vector y lo crea en la BD
    vector = await vector_chunk(item)
    await create_embedding_db(db, item, vector, model)
    
async def start_embedding(data: OuterArrayData, db: AsyncSession):
    #log inicio_embedding/ cantidad de chunks creados/fecha de creación
    #Recibe json de listado de n chunks para ingresar y vectorizar, hace el
    #recorrido por todo el json y envía cada chunk a embedding_process para su
    #procesado. Envía log de control
    
    chunk_count = 0
    for item in data:
        await embedding_process(db,item.description, item.model)
        chunk_count+=1
    return {"chunk_count":chunk_count, "success": True}
    
    
