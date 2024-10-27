# EJERCICIO 5: Escribe un programa para pedirle al usuario las horas y la tarifa por hora para calcular el pago bruto.
# Fernando Sevil

horas = input ("¿Cuantas horas se han trabajado? \n")
tarifa = input ("¿Cual es la tarifa por hora? \n")
horas_extra = int(horas) - 40
sueldo = int(horas) * int(tarifa)
if horas_extra>0:
    sueldo = int(sueldo) + (int(horas_extra)*(int(tarifa)/2))
print ("El pago bruto es "+horas+" horas por "+tarifa+" euros la hora: "+str(sueldo)+"€\n")
