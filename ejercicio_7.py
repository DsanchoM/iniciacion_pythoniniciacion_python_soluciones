puntuacion = float(input("Intrduzca la puntuacion: "))
grade = ""

if puntuacion < 0.0 or puntuacion > 1.0 :
    print(f"Puntuación fuera de rango")
else :
    if puntuacion >= 0.9 :
        grade = "A"
    elif puntuacion >= 0.8 :
        grade = "B"
    elif puntuacion >= 0.7 :
        grade = "C"
    elif puntuacion >= 0.6 :
        grade = "D"
    else :
        grade = "F"

print(grade)