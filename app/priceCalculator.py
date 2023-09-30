from abc import ABC, abstractmethod

class PriceCalculator(ABC):
    @abstractmethod
    def calculate_price(self, product, quantity):
        pass
