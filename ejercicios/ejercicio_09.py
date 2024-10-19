def coputegrade(score):
    match score:
        case score if score < 0.0 or score > 1.0:
            return "Error: puntuación fuera de rango"
        case score if score >= 0.9:
            return "A"
        case score if score >= 0.8:
            return "B"
        case score if score >= 0.7:
            return "C"
        case score if score >= 0.6:
            return "D"
        case _:
            return "F"


try:
    score = float(input(" Intoduzca una puntuacion entre 0.0 y 1.0"))
    print(f"Calificación obtenida: {coputegrade(score)}")
except:
    print("Por favor introduzca un valor numérico")