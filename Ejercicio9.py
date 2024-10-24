# EJERCICIO 9: Reescribe el programa de calificación del capítulo anterior (EJERCICIO 7) utilizando una función llamada "computegrade" 
# que tome una puntuación como parámetro y devuelva una nota como una cadena.

def computegrade(puntuacion):
    if puntuacion >= 0.9 and puntuacion <= 1.0 :
        nota= "Su calificación es A"
    elif puntuacion >= 0.8 and puntuacion <= 1.0:
        nota= "Su calificación es B"
    elif puntuacion >= 0.7 and puntuacion <= 1.0:
        nota= "Su calificación es C"
    elif puntuacion >= 0.6 and puntuacion <= 1.0:
        nota= "Su calificación es D"
    elif puntuacion <0.6 and puntuacion <= 1.0:
        nota= "Su calificación es F"
    else :
        nota= " la puntuación está fuera de rango"

    return nota 

try :
    puntuacionUsuario = float(input("Por favor, introduce tu puntuación entre 0.0 y 1.0: "))
    computegrade(puntuacionUsuario)
    print (computegrade(puntuacionUsuario))
    
except : 

     print ("Introduzca un numero")
