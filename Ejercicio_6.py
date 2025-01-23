#EJERCICIO 6: Reescribe tu programa de pago usando (EJERCICIO 2) "try" y "except" para que su programa maneje la entrada no numérica correctamente imprimiendo un mensaje y saliendo del programa. A continuación se muestran una ejecución del programa:

#Enter Hours: 20
#Enter Rate: nine
#Error, please enter numeric input

#SOLUCIÓN:

precio=input("indique su tarifa por hora, por favor\n")
try:
    precio=int(precio)
    tiempo=input("Muchas gracias. Ahora indique las horas de trabajo empleadas\n")
    tiempo=int(tiempo)
    factura=precio*tiempo
    print ("Debido a los datos introducidos, le indicamos que su pago bruto asciende a un total de",factura,"euros")
except:
    print ("Error, please enter numeric input\n")
