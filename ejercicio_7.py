try:
    calificacion = float(input('Ingrese calificación entre 0 y 1: '))
    
    if calificacion < 0 or calificacion > 1:
        raise ValueError('La calificación debe estar entre 0 y 1')

    if calificacion >= 0.9:
        calificacion_letra = 'A'
    elif calificacion >= 0.8:
        calificacion_letra = 'B'
    elif calificacion >= 0.7:
        calificacion_letra = 'C'
    elif calificacion >= 0.6:
        calificacion_letra = 'D'
    else:
        calificacion_letra = 'F'

    print('Tu calificación es:', calificacion_letra)

except ValueError as e:
    print('Error:', e)
