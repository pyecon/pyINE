from src.client import get_data
import pandas as pd

test_1 = get_data(function="DATOS_TABLA", id="22344")
print(test_1)

# PIB test
#https://www.ine.es/jaxiT3/Tabla.htm?t=30683
# Datos ajustados
# renta nacional bruta
# Variacion anual
# Periodo 2021 T1-T4

get_data(function="DATOS_TABLA", id="30683")
