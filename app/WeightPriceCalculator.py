import priceCalculator as PriceCalculator

class WeightPriceCalculator(PriceCalculator):
    def calculate_price(self, product, quantity_in_grams):
        if product.available_units >= quantity_in_grams:
            return (product.unit_price / 1000) * quantity_in_grams
        else:
            return -1  # Indica que no hay suficientes unidades disponibles

