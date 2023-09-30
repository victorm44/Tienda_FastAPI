from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from database import app
from models import Product
from price_calculator import NormalPriceCalculator, WeightPriceCalculator, SpecialDiscountPriceCalculator

router = APIRouter()

# Inicializar calculadoras de precio
normal_price_calculator = NormalPriceCalculator()
weight_price_calculator = WeightPriceCalculator()
special_discount_calculator = SpecialDiscountPriceCalculator()

# Definir rutas y controladores relacionados con productos aquí
