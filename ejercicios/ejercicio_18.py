numbers = []

while True:
    try:
        number = input("Introduzca un número, (`listo` para salir): ")
        if number == "listo":
            break
        numbers.append(float(number))
    except:
        print("inserta un valor numérico")

print(max(numbers))
print(min(numbers))