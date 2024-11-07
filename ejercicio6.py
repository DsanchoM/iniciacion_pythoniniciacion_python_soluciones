horas = input("Introduce las horas\n")
try:
    tarifa = input("Introduce la tarifa por hora\n")
    calculo = int(horas) * int(tarifa)
    print("Pago bruto: " + str(calculo))
except:
    print("Error, please enter numeric input")



