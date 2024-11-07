a = float(input("Introduzca una puntuación entre 0.0 y 1.0\n"))

if a < 0 or a > 1:
    print("Valor fuera de rango")
elif a >= 0.9:
    print("GRADO A")
elif a >= 0.8:
    print("GRADO B")
elif a >= 0.7:
    print("GRADO C")
elif a >= 0.6:
    print("GRADO D")
else:
    print("GRADO e")

