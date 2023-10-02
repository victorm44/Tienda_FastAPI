from fastapi import APIRouter
from typing import Dict
from models.Product import Product
from app.price_calculator_engine import calculate_product_price
from database.database import app
from typing import Dict, List


router = APIRouter()

# Define la estructura del carrito de compras
class ShoppingCart:
    def __init__(self):
        # Inicializa el carrito de compras como un diccionario donde la clave es el SKU del producto y el valor es la cantidad
        self.cart = {}

    def add_item(self, product_sku, quantity):
        # Agregar un producto al carrito
        if product_sku in self.cart:
            # Si el producto ya está en el carrito, aumenta la cantidad
            self.cart[product_sku] += quantity
        else:
            # Si el producto no está en el carrito, agrégalo con la cantidad especificada
            self.cart[product_sku] = quantity

    def remove_item(self, product_sku):
        # Elimina un producto del carrito
        if product_sku in self.cart:
            # Si el producto está en el carrito, elimínalo
            del self.cart[product_sku]

    def calculate_total(self, product_catalog: Dict[str, Product]):
        # Calcula el total de la compra en el carrito
        total = 0
        for product_sku, quantity in self.cart.items():
            if product_sku in product_catalog:
                product = product_catalog[product_sku]
                total += calculate_product_price(product, quantity)  # Usar el método de cálculo de precio de la instancia
        return total

# Crea una instancia del carrito de compras
shopping_cart = ShoppingCart()

# Define una ruta para agregar un producto al carrito
@router.post("/add_to_cart")
def add_to_cart(product_sku: str, quantity: int):
    shopping_cart.add_item(product_sku, quantity)
    return {"message": "Producto agregado al carrito"}

# Define una ruta para eliminar un producto del carrito
@router.post("/remove_from_cart")
def remove_from_cart(product_sku: str):
    shopping_cart.remove_item(product_sku)
    return {"message": "Producto eliminado del carrito"}

# Define una ruta para calcular el total de la compra en el carrito
@router.get("/calculate_cart_total")
def calculate_cart_total(product_catalog: Dict[str, Product]):
    total = shopping_cart.calculate_total(product_catalog)  # Calcula el total usando el catálogo de productos
    return {"total": total}

# Esta función obtendrá todos los productos desde la base de datos
async def get_all_products():
    db = app.state.db
    products_collection = db["productos"]
    products_data = await products_collection.find({}).to_list(length=None)
    products = [Product(**product) for product in products_data]
    return products

# Define una ruta para obtener todos los productos
@router.get("/get_all_products", response_model=List[Product])
async def get_all_products_route():
    products = await get_all_products()
    return products