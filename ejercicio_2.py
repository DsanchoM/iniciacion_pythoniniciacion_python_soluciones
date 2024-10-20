#EJERCICIO 2: Escribe un programa para pedirle al usuario las horas
# y la tarifa por hora para calcular el pago bruto.

horas  = int(input("Por favor, introduce las horas:\n"))
tarifa = int(input("Por favor, introduce la tarifa por hora:\n"))

pago_bruto = horas * tarifa
print ("El pago_bruto es de", pago_bruto)