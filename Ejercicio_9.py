#EJERCICIO 9: Reescribe el programa de calificación del capítulo anterior (EJERCICIO 7) utilizando una función llamada "computegrade" que tome una puntuación como parámetro y devuelva una nota como una cadena.

#SOLUCIÓN:

def computegrade(nota):
    if nota>=0.9 and nota<=1.0:
        calif="El alumno tiene una calificación de A"
    elif nota>=0.8 and nota<=1.0:
        calif="El alumno tiene una calificación de B"
    elif nota>=0.7 and nota<=1.0:
        calif="El alumno tiene una calificación de C"
    elif nota>=0.6 and nota<=1.0:
        calif="El alumno tiene una calificación de D"
    elif nota<0.6 and nota>=0.0:
        calif="El alumno tiene una calificación de F"
    else:
        calif="Su calificación no se puede calcular porque la nota introducida está fuera de los valores permitidos"
    return calif

examen1=input("Introduzca una puntuación entre 0.0 y 1.0 para conocer su calificación:\n")
try:
    examen1=float(examen1)
    calif=computegrade(examen1)
    print (calif)
except:
    print ("Por favor, introduzca un valor numérico entre 0.0 y 1.0")
