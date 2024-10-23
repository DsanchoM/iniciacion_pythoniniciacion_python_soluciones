

try:
    puntuacion = float(input('Dime el resultado de la puntuación'))

    if puntuacion >= 0 and puntuacion <= 1.0:

        if puntuacion >= 0.9:
            print('Grado A')
        elif puntuacion >= 0.8:
            print('Grado B')
        elif puntuacion >= 0.7:
            print('Grado C')
        elif puntuacion >= 0.6:
            print('Grado D')
        elif puntuacion < 0.6:
            print('Grado E')

    else:
        print('La puntuacion está fuera del rango entre 0.0 y 1.0');

except ValueError:
    print('Error, el input debe ser un número');