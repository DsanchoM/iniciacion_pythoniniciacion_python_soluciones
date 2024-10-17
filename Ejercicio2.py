# EJERCICIO 2: Escribe un programa para pedirle al usuario las horas y la tarifa por hora para calcular el pago bruto.

horas = float(input("Por favor, introduce las horas: "))
tarifa = float(input("Por favor, introduce la tarifa por hora: "))
print ("El pago bruto es de " + str(horas * tarifa) + "€")
