# EJERCICIO 2: Escribe un programa para pedirle al usuario las horas y la tarifa por hora para calcular el pago bruto.
# Fernando Sevil

horas = input ("¿Cuantas horas se han trabajado? \n")
tarifa = input ("¿Cual es la tarifa por hora? \n")
print ("El pago bruto es "+horas+" horas por "+tarifa+" euros la hora: "+str(int(horas)*int(tarifa))+"€\n")