import priceCalculator as PriceCalculator

class SpecialDiscountPriceCalculator(PriceCalculator):
    def calculate_price(self, product, quantity):
        if product.available_units >= quantity:
            discounted_quantity = quantity - (quantity // 3)
            return product.unit_price * discounted_quantity
        else:
            return -1  # Indica que no hay suficientes unidades disponibles