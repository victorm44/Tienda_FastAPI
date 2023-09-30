from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import product, cart
from database import init_db, close_db

app = FastAPI()

# Configuración de la base de datos
app.add_event_handler("startup", init_db)
app.add_event_handler("shutdown", close_db)

# Configuración para permitir solicitudes desde cualquier origen (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Agregar rutas desde módulos de enrutador
app.include_router(product.router)
app.include_router(cart.router)
