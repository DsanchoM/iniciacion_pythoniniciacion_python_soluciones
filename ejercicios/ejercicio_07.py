try:
    score  = float( input(" Intoduzca una puntuacion entre 0.0 y 1.0"))

    match score:
        case score if score < 0.0 or score > 1.0:
            print("Error: puntuación fuera de rango")
        case score if score >= 0.9:
            print("A")
        case score if score >= 0.8:
            print( "B")
        case score if score >= 0.7:
            print("C")
        case score if score >= 0.6:
            print( "D")
        case _:
            print("F")
except:
    print("Por favor introduzca un valor numérico")