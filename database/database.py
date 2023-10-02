from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI
from models.Product import Product

app = FastAPI()

MONGODB_URL = "mongodb+srv://victor:vic123456@cluster0.cu54xkq.mongodb.net/?retryWrites=true&w=majority"  # Cambia la URL según tu configuración
client = AsyncIOMotorClient(MONGODB_URL)
db = client.my_database  # Cambia "my_database" al nombre de tu base de datos

def init_db():
    # Inicializar la conexión a la base de datos al arrancar la aplicación
    app.state.db = db

def close_db():
    # Cerrar la conexión a la base de datos al apagar la aplicación
    app.state.db.client.close()

async def get_product_catalog(db):
    product_data = await db["productos"].find({})  # Ajusta la consulta según tu base de datos
    product_catalog = {}
    for product in product_data:
        product_sku = product["sku"]
        product_catalog[product_sku] = Product(
            sku=product["sku"],
            name=product["nombre"],
            description=product["descripcion"],
            available_units=product["unidades_disponibles"],
            unit_price=product["precio"]
        )
    return product_catalog


