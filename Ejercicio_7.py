def main():
    score = float(input("Escribe la puntuación entre 0 y 1. "))
    if score < 0 or score > 1:
        print(f'{score} ERROR escriba un numero entre 0 y 1.')
    elif score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    else:
        print("F")
    return main()
main()