from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from database.database import app
from models.Product import Product


from app.shoppingCart import ShoppingCart


router = APIRouter()

# Crear una instancia de ShoppingCart
shopping_cart = ShoppingCart()

@router.post("/add_to_cart/{product_sku}/{quantity}")
def add_to_cart(product_sku: str, quantity: int):
    shopping_cart.add_item(product_sku, quantity)
    return {"message": f"{quantity} unidades de {product_sku} agregadas al carrito"}

@router.delete("/remove_from_cart/{product_sku}")
def remove_from_cart(product_sku: str):
    shopping_cart.remove_item(product_sku)
    return {"message": f"{product_sku} eliminado del carrito"}

@router.get("/cart_total")
def get_cart_total():
    total = shopping_cart.calculate_total()
    return {"total": total}

