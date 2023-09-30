
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        # Verificar si el producto ya está en el carrito
        for item in self.items:
            if item["product"] == product:
                item["quantity"] += quantity
                return
        # Si el producto no está en el carrito, agregarlo
        self.items.append({"product": product, "quantity": quantity})

    def remove_item(self, product):
        # Remover un producto del carrito
        self.items = [item for item in self.items if item["product"] != product]

    def calculate_total(self):
        # Calcular el total de la compra en el carrito
        total = 0
        for item in self.items:
            product = item["product"]
            quantity = item["quantity"]
            total += product.unit_price * quantity
        return total
