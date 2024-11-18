'''
EJERCICIO 5:
Reescribe tu cálculo de pago (EJERCICIO 2) para darle al empleado 1.5 veces la tarifa por hora por las horas trabajadas por encima de las 40 horas.
La salida es la siguiente:
Enter Hours: 45
Enter Rate: 10
Pay: 475.0
'''
horas = int(input('Introduce las horas que has trabajado: '))
tarifa = int(input('Introduce la tarifa por hora: '))
if horas>40:
    pago = (40*tarifa)
    horas_extras = ((horas - 40) * tarifa) * 1.5
    print(f'Total: {pago+horas_extras} ')
else:
    print(f'El pago bruto es {horas * tarifa}')
