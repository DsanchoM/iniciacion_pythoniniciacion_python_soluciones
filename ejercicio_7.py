"""
EJERCICIO 7: Escribe un programa para solicitar una puntuación entre 0.0 y 1.0. Si la puntuación está fuera de rango,
imprime un mensaje de error. Si la puntuación está entre 0.0 y 1.0, imprime una calificación usando la siguiente tabla:
Score	Grade
>= 0.9	A
>= 0.8	B
>= 0.7	C
>= 0.6	D
< 0.6	F
"""

try:
    numero = float(input("Introduce un número: "))
    if numero >= 0.0 and numero <= 1.0:
        if numero < 0.6:
            print("la puntuación es F")
        elif numero >= 0.6 and numero < 0.7:
            print("la puntuación es D")
        elif numero >= 0.7 and numero < 0.8:
            print("la puntuación es C")
        elif numero >= 0.8 and numero < 0.9:
            print("la puntuación es B")
        else:
            print("la puntuación es A")
    else:
        print("el numero no está entre 0.0 y 1.0")
        numero = float(input("Introduce un número: "))

except:
    print("No has introducido un número")
    numero = float(input("Introduce un número: "))