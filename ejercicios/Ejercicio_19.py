try:
    fileName = input("Inserte el nombre del fichero")
    days = {}

    with open(fileName, 'r') as file:
        for line in file:

            if line.startswith("From"):
                lineWords = line.split()

                if len(lineWords) > 2:
                    weekDay = lineWords[2]

                    if weekDay in days:
                        days[weekDay] += 1
                    else:
                        days[weekDay] = 1

    print(days)

except FileNotFoundError:
    print(f"No se ha encontrado el archivo, vuelva a intentarlo")
