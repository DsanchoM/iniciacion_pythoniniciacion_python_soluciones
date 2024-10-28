try:
    puntuacion = float(input("Ingrese una puntuación entre 0.0 y 1.0: "))
    def computegrade(puntuacion):
        if puntuacion < 0.0 or puntuacion > 1.0:
            print("Error: La puntuación está fuera de rango. Debe estar entre 0.0 y 1.0.")
        else:
            if puntuacion >= 0.9:
                calificacion = "A"
            elif puntuacion >= 0.8:
                calificacion = "B"
            elif puntuacion >= 0.7:
                calificacion = "C"
            elif puntuacion >= 0.6:
                calificacion = "D"
            else:
                calificacion = "F"
            return calificacion
    resultado = computegrade(puntuacion)  
    print(f"Calificacion = {resultado}")

except ValueError:
    print("Error: Por favor, ingrese un número válido.")
