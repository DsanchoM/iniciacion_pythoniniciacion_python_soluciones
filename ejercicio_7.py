# Solicitar la puntuación al usuario
while True:
    try:
        puntuacion = float(input("Introduce una puntuación entre 0.0 y 1.0: "))
        
        # Verificar si la puntuación está en el rango adecuado
        if 0.0 <= puntuacion <= 1.0:
            break  # Sale del bucle si la entrada es válida
            #se puede obviar el break, se seguirá pidindo número aunque la entrada no sea válida
        else:
            print("Error: La puntuación debe estar entre 0.0 y 1.0.")
    except ValueError:
        print("Error: Por favor, introduce un número válido.")

# Determinar la calificación según la puntuación
if puntuacion >= 0.9:
    calificacion = 'A'
elif puntuacion >= 0.8:
    calificacion = 'B'
elif puntuacion >= 0.7:
    calificacion = 'C'
elif puntuacion >= 0.6:
    calificacion = 'D'
else:
    calificacion = 'F'

# Imprimir la calificación
print(f"La calificación es: {calificacion}")
