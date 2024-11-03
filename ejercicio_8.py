#EJERCICIO 8: Reescribe su cálculo de pago (EJERCICIO 2)
#con tiempo y medio para horas extras y crea una función
#llamada "computepay" que tome dos parámetros ("hours" y "rate").

def computepay(hours, rate):
    pay = hours * rate
    return pay

horas  = float(input("Por favor, introduce las horas:\n"))
tarifa = float(input("Por favor, introduce la tarifa por hora:\n"))

print("El pago_bruto es de", computepay(horas, tarifa))