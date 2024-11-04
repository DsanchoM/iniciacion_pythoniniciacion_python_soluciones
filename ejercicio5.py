print("Introduce las horas")
horas = input()

print("Introduce la tarifa por hora")
tarifa = input()

if int(horas) > 40:
    extra = int(horas) - 40
    calculo = (40 * int(tarifa)) + (extra * int(tarifa) * 1.5)
else:
    calculo = int(horas) * int(tarifa)

print("Pago bruto: " + str(calculo))