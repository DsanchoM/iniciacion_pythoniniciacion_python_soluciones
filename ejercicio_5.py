"""
EJERCICIO 5: Reescribe tu cálculo de pago (EJERCICIO 2) para darle al empleado 1.5 veces la tarifa por hora por las horas trabajadas por encima de las 40 horas. La salida es la siguiente:
Enter Hours: 45
Enter Rate: 10
Pay: 475.0
"""
horas = input("Indica tus horas: ")
tarifa = input("Indica tu tarifa: ")
if float(horas) > 40:
    horas_extras = float(horas) - 40
    total = (40 * float(tarifa)) + (horas_extras * (float(tarifa) * 1.5))
    print("Tus Horas extras pagadas a 1.5 la tarifa son: {}".format(horas_extras))
    print("Total bruto que hay que pagar: {}".format(total))
else:
    total = float(horas) * float(tarifa)
    print("Total bruto que hay que pagar: {}".format(total))
