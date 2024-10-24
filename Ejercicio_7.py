#EJERCICIO 7: Escribe un programa para solicitar una puntuación entre 0.0 y 1.0. Si la puntuación está fuera de rango, imprime un mensaje de error. Si la puntuación está entre 0.0 y 1.0, imprime una calificación usando la siguiente tabla:

#Score	Grade
#>= 0.9	A
#>= 0.8	B
#>= 0.7	C
#>= 0.6	D
#< 0.6	F

#SOLUCIÓN:

nota=input("Introduzca una puntuación entre 0.0 y 1.0 para conocer su calificación:\n")
try:
    nota=float(nota)
    if nota>=0.9 and nota<=1.0:
        calif="A"
        print("Su calificación es",calif)
    elif nota>=0.8 and nota<=1.0:
        calif="B"
        print("Su calificación es",calif)
    elif nota>=0.7 and nota<=1.0:
        calif="C"
        print("Su calificación es",calif)
    elif nota>=0.6 and nota<=1.0:
        calif="D"
        print("Su calificación es",calif)
    elif nota<0.6 and nota>=0.0:
        calif="F"
        print("Su calificación es",calif)
    else:
        print("Su calificación no se puede calcular porque la nota introducida está fuera de los valores permitidos")
except:
    print("Su calificación no se puede calcular porque la nota introducida no correspone a ningún valor numérico")
