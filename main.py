from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import cart
from database.database import init_db, close_db
from routes import test
from app.price_calculator_engine import calculate_product_price
from database.database import init_db, close_db, get_product_catalog


app = FastAPI()

# Configuración de la base de datos
app.add_event_handler("startup", init_db)
app.add_event_handler("shutdown", close_db)
app.dependency_overrides[get_product_catalog] = get_product_catalog

# Configuración para permitir solicitudes desde cualquier origen (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Agregar rutas desde módulos de enrutador
app.include_router(test.router)
app.include_router(cart.router)
