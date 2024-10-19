#EJERCICIO 2: Escribe un programa para pedirle al usuario las horas y la tarifa por hora para calcular el pago bruto.

#SOLUCIÓN:

precio=input("indique su tarifa por hora, por favor\n")
precio=int(precio)
tiempo=input("Muchas gracias. Ahora indique las horas de trabajo empleadas\n")
tiempo=int(tiempo)
factura=precio*tiempo
print ("Debido a los datos introducidos, le indicamos que su pago bruto asciende a un total de",factura,"euros")
