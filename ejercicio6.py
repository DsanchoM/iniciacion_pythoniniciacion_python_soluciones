### Escribe un programa para pedirle al usuario las horas y la tarifa por hora para calcular el pago bruto.

try:
    horas = int(input('¿Cuantas horas trabaja?\n'))
    tarifa = float(input('¿Cual es su tarifa de €/h?\n'))
    pago_bruto  =  tarifa * horas
    print(f'El pago bruto es de {pago_bruto} €')
except ValueError:
    print('Error, please enter numeric input')