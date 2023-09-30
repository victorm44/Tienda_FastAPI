class Product:
    def __init__(self, sku, name, description, available_units, unit_price):
        self.sku = sku
        self.name = name
        self.description = description
        self.available_units = available_units
        self.unit_price = unit_price

    def __str__(self):
        return f"{self.name} (SKU: {self.sku})"

    def to_dict(self):
        return {
            "sku": self.sku,
            "name": self.name,
            "description": self.description,
            "available_units": self.available_units,
            "unit_price": self.unit_price
        }
