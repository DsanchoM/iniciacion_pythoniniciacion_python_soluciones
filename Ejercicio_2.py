#EJERCICIO 2: Escribe un programa para pedirle al usuario las horas y la tarifa por hora para calcular el pago bruto.

#SOLUCIÓN:

precio=input("indique el coste por hora de su actual contrato, por favor\n")
precio=int(precio)
tiempo=input("Muchas gracias. Ahora indique las horas de uso que marca su contador\n")
tiempo=int(tiempo)
factura=precio*tiempo
print ("Debido a los datos introducidos, le indicamos que su factura tiene asciende a un coste de",factura,"euros")
