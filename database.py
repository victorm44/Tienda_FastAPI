from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI

app = FastAPI()

MONGODB_URL = "mongodb://localhost:27017"  # Cambia la URL según tu configuración
client = AsyncIOMotorClient(MONGODB_URL)
db = client.my_database  # Cambia "my_database" al nombre de tu base de datos

def init_db():
    # Inicializar la conexión a la base de datos al arrancar la aplicación
    app.state.db = db

def close_db():
    # Cerrar la conexión a la base de datos al apagar la aplicación
    app.state.db.client.close()

