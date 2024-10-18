
nhoras = int(input("Escriba el numero de horas: "))
phoras = int(input("Escriba el precio de las horas: "))

if nhoras <= 40:
    print(f"TOTAL",{nhoras*phoras})

if nhoras > 40:
    horas_b = nhoras-40
    horas_a = nhoras-horas_b
    phoras_ex = 1.5 * phoras
    print ("TOTAL",horas_a*phoras+horas_b*phoras_ex,"€")



