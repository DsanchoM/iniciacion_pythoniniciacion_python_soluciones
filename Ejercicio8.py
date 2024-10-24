# EJERCICIO 8: Reescribe su cálculo de pago (EJERCICIO 2) con tiempo y medio para horas extras y 
# crea una función llamada "computepay" que tome dos parámetros ("hours" y "rate").

def computepay(hours,rate):
    if hours > 40 :
        sueldo = 40 * rate + ((hours -40) * (1.5 * rate ))

    else :
 
        sueldo = (hours * rate)

    return sueldo

horas = float(input("Por favor, introduce las horas: "))
tarifa = float(input("Por favor, introduce el precio de la tarifa por cada horas: "))

salario= computepay(horas,tarifa)

print ("El pago bruto es de " + str(salario) + "€")
