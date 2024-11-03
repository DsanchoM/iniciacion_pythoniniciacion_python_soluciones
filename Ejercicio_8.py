#EJERCICIO 8: Reescribe su cálculo de pago (EJERCICIO 2) con tiempo y medio para horas extras y crea una función llamada "computepay" que tome dos parámetros ("hours" y "rate").

#SOLUCIÓN:

def computepay(tiempo,precio):
    
    precio=float(precio)
    tiempo=int(tiempo)
    precioextra=precio*1.5
    if tiempo>40 :
        tiempoextra=tiempo-40
        salario=precio*40+precioextra*tiempoextra
    else:
        salario=precio*tiempo
    return salario

pago_hora=input("indique su tarifa por hora, por favor\n")
jornada=input("Muchas gracias. Ahora indique las horas de trabajo empleadas\n")
salario=computepay(jornada,pago_hora)
print ("Su pago bruto asciende a un total de",salario,"euros.")
