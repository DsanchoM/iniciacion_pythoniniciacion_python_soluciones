'''
EJERCICIO 7: Escribe un programa para solicitar una puntuación entre 0.0 y 1.0.
Si la puntuación está fuera de rango, imprime un mensaje de error.
Si la puntuación está entre 0.0 y 1.0, imprime una calificación usando la siguiente tabla:
Score	Grade
>= 0.9	A
>= 0.8	B
>= 0.7	C
>= 0.6	D
< 0.6	F
Ejecute el programa repetidamente para probar los diferentes valores de entrada.
'''
valor = float(input('Introduce una puntuación: '))
if valor > 1 or valor < 0:
    print('Fuera de rango')
elif valor >= 0.9:
    print('A')
elif valor >= 0.8:
    print('B')
elif valor >= 0.7:
    print('C')
elif valor >= 0.6:
    print('D')
else:
    print('F')
