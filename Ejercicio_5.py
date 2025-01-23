#EJERCICIO 5: Reescribe tu cálculo de pago (EJERCICIO 2) para darle al empleado 1.5 veces la tarifa por hora por las horas trabajadas por encima de las 40 horas. La salida es la siguiente:

#Enter Hours: 45
#Enter Rate: 10
#Pay: 475.0

#SOLUCIÓN:

precio=input("indique su tarifa por hora, por favor\n")
precio=float(precio)
tiempo=input("Muchas gracias. Ahora indique las horas de trabajo empleadas\n")
tiempo=int(tiempo)
precioextra=precio*1.5
if tiempo>40 :
    tiempoextra=tiempo-40
    salario1=precio*40+precioextra*tiempoextra
    print ("Su pago bruto asciende a un total de", salario1,"euros.")
else:
    salario2=precio*tiempo
    print ("Debido a los datos introducidos, le indicamos que su pago bruto asciende a un total de",salario2,"euros")
