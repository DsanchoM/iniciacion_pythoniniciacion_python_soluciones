
def computepay(rate,hours):
    if(hours<=40):
        pay = hours * rate
    else:
        pay = 40 * rate + (hours-40)*rate*1.5
    print( "El importe final con "+ str(hours)+ " a " + str(rate) + " la hora es: "+ str(pay))
try:
    computepay(float(input("Introduzca cual es la tarifa a cobrar por cada hora de trabajo: ")),float(input("Introduzca el numero de horas de trabajo: ")))
except:
    print("Error al introducir tipo de dato")