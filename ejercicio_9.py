def computegrade(grade):
    i=0
    while i==0:
        if grade>=0.0 and grade<=1.0:
            i+=1
        if i==0:
            grade = float(input("Introduzca un número entre 0.0 y 1.0 para saber la calificación final: "))
    if grade>=0.9:
        return "Your grade is: A"
    elif grade>=0.8:
        return "Your grade is: B"
    elif grade >= 0.7:
        return "Your grade is: C"
    elif grade>=0.6:
        return "Your grade is: D"
    else:
        return "Your grade is: F"

try:
    print(computegrade(float(input("Introduzca un número entre 0.0 y 1.0 para saber la calificación final: "))))
except:
    print("Error en el tipo de dato")
