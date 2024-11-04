def summary(min, max):
    print(f"El número más pequeño ha sido: {min}")
    print(f"El número más grande ha sido: {max}")

def uploadCounter(number, min, max):
    if min is None or number < min:
        min = number
    if max is None or number > max:
        max = number
    return min, max

min = None
max = None

while True:
    number = input("Introduzca un número, (`listo` para salir): ")

    if number.lower() == "listo":
        break

    try:

        number = int(number)
        min, max = uploadCounter(number, min, max)
    except ValueError:
        print("Por favor, introduzca un número válido o `listo` para salir.")

summary(min, max)
