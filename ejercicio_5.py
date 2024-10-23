""""#EJERCICIO 5: Reescribe tu cálculo de pago (EJERCICIO 2) para darle
# al empleado 1.5 veces la tarifa por hora por las horas trabajadas
# por encima de las 40 horas. La salida es la siguiente:
#Enter Hours: 45
#Enter Rate: 10
#Pay: 475.0
"""
horas  = int(input("Por favor, introduce las horas trabajadas:\n"))
tarifa = int(input("Por favor, introduce la tarifa por hora:\n"))

if horas > 40 :
    horasMas = horas - 40
    pago = (40 * tarifa) + (horasMas * tarifa *1.5)
else:
    pago = horas * tarifa
print ("El pago bruto es de", pago)