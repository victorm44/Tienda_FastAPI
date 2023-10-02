from abc import ABC, abstractmethod

class PriceCalculator(ABC):
    @abstractmethod
    def calculate_price(self, product, quantity):
        pass

class NormalPriceCalculator(PriceCalculator):
    def calculate_price(self, product, quantity):
        if product.available_units >= quantity:
            return product.unit_price * quantity
        else:
            return -1  # Indica que no hay suficientes unidades disponibles
        
class SpecialDiscountPriceCalculator(PriceCalculator):
    def calculate_price(self, product, quantity):
        if product.available_units >= quantity:
            discounted_quantity = quantity - (quantity // 3)
            return product.unit_price * discounted_quantity
        else:
            return -1  # Indica que no hay suficientes unidades disponibles
        
class WeightPriceCalculator(PriceCalculator):
    def calculate_price(self, product, quantity_in_grams):
        if product.available_units >= quantity_in_grams:
            return (product.unit_price / 1000) * quantity_in_grams
        else:
            return -1  # Indica que no hay suficientes unidades disponibles
