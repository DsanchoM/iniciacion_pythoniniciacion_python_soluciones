'''
Escribe un programa para solicitar una puntuación entre 0.0 y 1.0. Si la puntuación está fuera de rango, imprime un mensaje de error. 
Si la puntuación está entre 0.0 y 1.0, imprime una calificación usando la siguiente tabla:
Score	Grade
>= 0.9	A
>= 0.8	B
>= 0.7	C
>= 0.6	D
< 0.6	F
'''

while True:
    try:
        score = float(input("Ingrese la puntuación (0.0-1.0): "))
        if 0.0 <= score <= 1.0:
            break
        else:
            print("Error: La puntuación debe estar entre 0.0 y 1.0.")
    except ValueError:
        print("Error: Ingrese un número válido.")

if score >= 0.9:
    grade = "A"
elif score >= 0.8:
    grade = "B"
elif score >= 0.7:
    grade = "C"
elif score >= 0.6:
    grade = "D"
else:
    grade = "F"

print("La calificación es:", grade)


