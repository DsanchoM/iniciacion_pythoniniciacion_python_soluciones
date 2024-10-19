def summary(total, count):
    if count > 0:
        average = total / count
        print(f"Suma: {total}, contador: {count},media: {average}")
    else:
        print("No se ha insertado ningún número")


def uploadCounter(number, total, count):
    try:
        number = float(number)
        total += number
        count += 1
    except ValueError:
        print("Por favor introduzca un número")
    return total, count

total = 0
count = 0

while True:
    number = input("Introduzca un número, (`listo` para salir) ")

    if number == "listo":
        break

    total, count = uploadCounter(number, total, count)

summary(total, count)




