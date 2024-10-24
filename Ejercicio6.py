# EJERCICIO 6: Reescribe tu programa de pago usando (EJERCICIO 2) "try" y "except" para que su programa maneje la entrada no numérica correctamente imprimiendo un mensaje y saliendo del programa. A continuación se muestran una ejecución del programa:
# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input


try :
    horas = float(input("Por favor, introduce las horas: "))
    tarifa = float(input("Por favor, introduce el precio de la tarifa por cada horas: "))


    if horas > 40 :
        print ("El pago bruto es de " + str(40 * tarifa + ((horas -40) * (1.5 * (tarifa))) ) + "€")

    else :
 
        print ("El pago bruto es de " + str(horas * tarifa) + "€")

except : 

     print ("Introduzca un numero")
