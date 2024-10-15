tarifa = float(input("Introduzca cual es la tarifa a cobrar por cada hora de uso:"))
horas = float(input("Introduzca el numero de horas de uso:"))
importe = horas * tarifa
print( "El importe final con "+ str(horas)+ " a " + str(tarifa) + " la hora es: "+ str(importe))