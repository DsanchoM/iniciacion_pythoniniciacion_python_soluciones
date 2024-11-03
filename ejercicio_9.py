#EJERCICIO 9: Reescribe el programa de calificación
# del capítulo anterior (EJERCICIO 7) utilizando una función
# llamada "computegrade" que tome una puntuación como parámetro
# y devuelva una nota como una cadena.

def computegrade(puntuacion):
    if puntuacion < 0.0 or puntuacion > 1.0:
        print ("La puntuación introducida está fuera de rango.")
    else:
        if puntuacion >= 0.9:
            return "A"
        elif puntuacion >= 0.8:
            return "B"
        elif puntuacion >= 0.7:
            return "C"
        elif puntuacion >= 0.6:
            return "D"
        else:
            return "E"

puntuacion = float(input("Introduce una puntuación\n"))

print(computegrade(puntuacion))
