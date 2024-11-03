# EJERCICIO 7: Escribe un programa para solicitar una puntuaci�n entre 0.0 y 1.0. Si la puntuaci�n est� fuera de rango, imprime un mensaje de error. 
# Fernando Sevil

import string


while True:

    try:
        puntuacion = float(input("Dame una puntuaci�n entre 0 y 1 \n"))

        if 0 <= puntuacion <= 1: # evalua si la puntuacion esta dentro del rango
            break # Si es correcto sale del bucle
        else:
            print ("La puntuacion debe ser superior a 0 y menor que 1. \n")

    except ValueError:
        print("Error: Por favor, introduce valores num�ricos. \n")

# Asigna el grado seg�n la puntuaci�n
if puntuacion >= 0.9:
    Grado = "A"
elif puntuacion >= 0.8:
    Grado = "B"
elif puntuacion >= 0.7:
    Grado = "C"
elif puntuacion >= 0.6:
    Grado = "D"
else:
    Grado = "F"

print(f"El grado obtenido es: {Grado} \n")