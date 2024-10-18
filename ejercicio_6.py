def main():
    try:
        nhoras = int(input("Escriba el numero de horas: "))
        phoras = int(input("Escriba el precio de las horas: "))
    except ValueError:
        print("Error, please enter numeric input")
        return main()
    else:
        if nhoras <= 40:
            print("TOTAL",nhoras*phoras,"€")

        if nhoras > 40:
            horas_b = nhoras-40
            horas_a = nhoras-horas_b
            phoras_ex = 1.5 * phoras
            print ("TOTAL",horas_a*phoras+horas_b*phoras_ex,"€")
main()
