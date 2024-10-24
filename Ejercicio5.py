# EJERCICIO 5: Reescribe tu cálculo de pago (EJERCICIO 2) para darle al empleado 1.5 veces la tarifa 
# por hora por las horas trabajadas por encima de las 40 horas. La salida es la siguiente:
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

print ("Programa Horas/Tarifas")
horas = float(input("Por favor, introduce las horas: "))
tarifa = float(input("Por favor, introduce el precio de la tarifa por cada horas: "))



if horas > 40 :
    print ("El pago bruto es de " + str(40 * tarifa + ((horas -40) * (1.5 * (tarifa))) ) + "€")

else :
 
    print ("El pago bruto es de " + str(horas * tarifa) + "€")
