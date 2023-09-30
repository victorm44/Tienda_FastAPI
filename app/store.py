class Store:
    def __init__(self):
        self.products = []

    def load_products(self, products):
        # Cargar una lista de productos en la tienda
        self.products.extend(products)

    def buy_product(self, product, quantity):
        for item in self.products:
            if item["product"] == product:
                if item["quantity"] >= quantity:
                    item["quantity"] -= quantity
                    return True
                else:
                    return False  # No hay suficientes unidades disponibles
        return False  # El producto no se encontró en la tienda

    def get_product(self, sku):
        for item in self.products:
            if item["product"].sku == sku:
                return item["product"]
        return None  # El producto no se encontró en la tienda
