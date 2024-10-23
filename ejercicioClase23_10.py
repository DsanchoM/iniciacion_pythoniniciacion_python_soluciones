import math

def calcular_area_circulo(radio):
    area = math.pi * pow(radio,2)
    return area
try:
    radio = float(input("Introduce radio: "))
    print(calcular_area_circulo(radio))
except:
    print("Error no es un numero el radio introducido")
