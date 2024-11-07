horas = input("Introduce las horas\n")

tarifa = input("Introduce la tarifa por hora\n")

if int(horas) > 40:
    extra = int(horas) - 40
    calculo = (40 * int(tarifa)) + (extra * int(tarifa) * 1.5)
else:
    calculo = int(horas) * int(tarifa)

print("Pago bruto: " + str(calculo))