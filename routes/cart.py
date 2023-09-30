from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from database import app
from models import Product
from shopping_cart import ShoppingCart

router = APIRouter()

# Inicializar el carrito de compras
shopping_cart = ShoppingCart()

# Definir rutas y controladores relacionados con el carrito de compras aquí
