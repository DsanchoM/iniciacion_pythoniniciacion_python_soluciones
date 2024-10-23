### Escribe un programa para pedirle al usuario las horas y la tarifa por hora para calcular el pago bruto.

horas = int(input('¿Cuantas horas trabaja?\n'))
tarifa = float(input('¿Cual es su tarifa de €/h?\n'))
if horas > 40:
    horas_extra = horas - 40
    horas = horas - horas_extra
else:
    horas_extra = 0

pago_bruto  =  tarifa * horas + (tarifa * 1.5) * horas_extra 

print(f'El pago bruto total es de {pago_bruto} €')
