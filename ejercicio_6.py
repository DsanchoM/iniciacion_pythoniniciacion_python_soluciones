""""EJERCICIO 6: Reescribe tu programa de pago usando (EJERCICIO 2) "try" y "except" para que su programa maneje la entrada no numérica correctamente imprimiendo un mensaje y saliendo del programa. A continuación se muestran una ejecución del programa:
Enter Hours: 20
Enter Rate: nine
Error, please enter numeric input
"""
try:
    horas  = int(input("Por favor, introduce las horas trabajadas:\n"))
    tarifa = int(input("Por favor, introduce la tarifa por hora:\n"))

    if horas > 40 :
        horasMas = horas - 40
        pago = (40 * tarifa) + (horasMas * tarifa *1.5)
    else:
        pago = horas * tarifa
    print ("El pago bruto es de", pago)
except:
    print("Por favor, introduzca un valor numérico:")
