# EJERCICIO 7: Escribe un programa para solicitar una puntuación entre 0.0 y 1.0. Si la puntuación está fuera de rango, 
# imprime un mensaje de error. Si la puntuación está entre 0.0 y 1.0, imprime una calificación usando la siguiente tabla:
# Score	Grade
# >= 0.9	A
# >= 0.8	B
# >= 0.7	C
# >= 0.6	D
# < 0.6	F

try :
    puntuacion = float(input("Por favor, introduce tu puntuación entre 0.0 y 1.0: "))
    

    if puntuacion >= 0.9 and puntuacion <= 1.0 :
        print ("Su calificación es A")
    elif puntuacion >= 0.8 and puntuacion <= 1.0:
        print ("Su calificación es B")
    elif puntuacion >= 0.7 and puntuacion <= 1.0:
        print ("Su calificación es C")
    elif puntuacion >= 0.6 and puntuacion <= 1.0:
        print ("Su calificación es D")
    elif puntuacion <0.6 and puntuacion <= 1.0:
        print ("Su calificación es F")

    else :

        print (" la puntuación está fuera de rango")

except : 

     print ("Introduzca un numero")
