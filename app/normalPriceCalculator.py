import priceCalculator as PriceCalculator

class NormalPriceCalculator(PriceCalculator):
    def calculate_price(self, product, quantity):
        if product.available_units >= quantity:
            return product.unit_price * quantity
        else:
            return -1  # Indica que no hay suficientes unidades disponibles