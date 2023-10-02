from app.priceCalculator import NormalPriceCalculator, WeightPriceCalculator, SpecialDiscountPriceCalculator

# Crea un diccionario que asocie SKU a las calculadoras de precio
priceCalculator = {
    "EA": NormalPriceCalculator(),
    "WE": WeightPriceCalculator(),
    "SP": SpecialDiscountPriceCalculator(),
    # Agrega más SKU y calculadoras según sea necesario
}

def calculate_product_price(product_sku, quantity):
    if product_sku in priceCalculator:
        calculator = priceCalculator[product_sku]
    else:
        calculator = priceCalculator["EA"]  # Usar el cálculo normal como predeterminado
    return calculator.calculate_price(product_sku, quantity)

