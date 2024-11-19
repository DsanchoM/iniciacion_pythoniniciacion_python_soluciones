'''
EJERCICIO 8: Reescribe su cálculo de pago (EJERCICIO 2)
con tiempo y medio para horas extras y crea una función llamada "computepay" que tome dos parámetros ("hours" y "rate").
'''


def computepay(horas: int, tarifa: int) -> None:
    print(f'El pago bruto es {horas * tarifa}')


horas = int(input('Introduce las horas que has trabajado: '))
tarifa = int(input('Introduce la tarifa por hora: '))
computepay(horas, tarifa)
