tarifa = float(input("Introduzca cual es la tarifa a cobrar por cada hora de trabajo: "))
horas = float(input("Introduzca el numero de horas de trabajo: "))
if(horas<=40):
    importe = horas * tarifa
else:
    importe = 40 * tarifa + (horas-40)*tarifa*1.5
print( "El importe final con "+ str(horas)+ " a " + str(tarifa) + " la hora es: "+ str(importe))