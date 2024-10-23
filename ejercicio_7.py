"""EJERCICIO 7: Escribe un programa para solicitar una puntuación entre 0.0 y 1.0.
 Si la puntuación está fuera de rango, imprime un mensaje de error.
 Si la puntuación está entre 0.0 y 1.0, imprime una calificación usando la siguiente tabla:
Score	Grade
>= 0.9	A
>= 0.8	B
>= 0.7	C
>= 0.6	D
< 0.6	F
Ejecute el programa repetidamente para probar los diferentes valores de entrada.
"""
puntuacion = float(input("Introduce una puntuación\n"))

if puntuacion < 0.0 or puntuacion > 1.0:
    print ("La puntuación introducida está fuera de rango.")
else:
    if puntuacion >= 0.9:
        print("A")
    elif puntuacion >= 0.8:
        print ("B")
    elif puntuacion >= 0.7:
        print ("C")
    elif puntuacion >= 0.6:
        print ("D")
    else:
        print ("E")