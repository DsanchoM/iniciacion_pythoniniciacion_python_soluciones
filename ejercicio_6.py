'''
EJERCICIO 6: Reescribe tu programa de pago usando (EJERCICIO 2) "try" y "except" para que su programa maneje la entrada
no numérica correctamente imprimiendo un mensaje y saliendo del programa. A continuación se muestran una ejecución del programa:
Enter Hours: 20
Enter Rate: nine
Error, please enter numeric input
'''

horas = input('Introduce las horas que has trabajado: ')
try:
    tarifa = input('Introduce la tarifa por hora: ')
    print(f'El pago bruto es {horas * tarifa}')
except TypeError: #Error por fallo en el tipo de la variableTypeError
    print('Error, introduce un número')
