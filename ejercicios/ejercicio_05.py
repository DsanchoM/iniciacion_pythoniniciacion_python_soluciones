hours = float(input("Introduzca el número de horas"))
fee = float(input("Introduzca el precio de la tarifa"))

if hours > 40.0:
    total = ((hours - 40.0) * (fee * 1.5)) + (40 * fee)
else:
    total = (hours * fee)

print(f"El coste total es: {total}€ ")
