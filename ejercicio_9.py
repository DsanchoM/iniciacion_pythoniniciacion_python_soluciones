'''
EJERCICIO 9: Reescribe el programa de calificación del capítulo anterior (EJERCICIO 7) utilizando una función llamada "computegrade"
que tome una puntuación como parámetro y devuelva una nota como una cadena.
'''

def computegrade(valor: float) -> str:
    if valor > 1 or valor < 0:
        return 'Fuera de rango'
    elif valor >= 0.9:
        return 'A'
    elif valor >= 0.8:
        return 'B'
    elif valor >= 0.7:
        return 'C'
    elif valor >= 0.6:
        return 'D'
    else:
        return 'F'


valor = float(input('Introduce una puntuación: '))
respuesta = computegrade(valor)
print(f'{respuesta}')
