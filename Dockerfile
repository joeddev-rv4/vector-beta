# Usa una imagen oficial de Python
FROM python:3.13.5

# Setea el directorio de trabajo
WORKDIR /vector-beta

# Copia los archivos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expón el puerto que usará Uvicorn
EXPOSE 8000

# Comando para producción con Gunicorn (opcional)
# CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--bind", "0.0.0.0:8000"]

# Comando para desarrollo
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
