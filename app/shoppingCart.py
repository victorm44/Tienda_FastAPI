from app.price_calculator_engine import calculate_product_price
from typing import Dict
from models.Product import Product
from database.database import get_product_catalog 

class ShoppingCart:
    def __init__(self):
        # Inicializar el carrito de compras como un diccionario donde la clave es el SKU del producto y el valor es la cantidad
        self.cart = {}

    def add_item(self, product_sku, quantity):
        # Agregar un producto al carrito
        if product_sku in self.cart:
            # Si el producto ya está en el carrito, aumentar la cantidad
            self.cart[product_sku] += quantity
        else:
            # Si el producto no está en el carrito, agregarlo con la cantidad especificada
            self.cart[product_sku] = quantity

    def remove_item(self, product_sku):
        # Eliminar un producto del carrito
        if product_sku in self.cart:
            # Si el producto está en el carrito, eliminarlo
            del self.cart[product_sku]

    async def calculate_total(self):
        total = 0
        product_catalog = await get_product_catalog()  # Obtén el catálogo de productos desde la base de datos
        # Itera sobre los productos en el carrito y calcula el total en función del catálogo de productos
        for product_sku, quantity in self.cart.items():
            if product_sku in product_catalog:
                product = product_catalog[product_sku]
                total += calculate_product_price(product, quantity)  # Utiliza la función de cálculo de precio
        return total


