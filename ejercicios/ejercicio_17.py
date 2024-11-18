try:
    fileName = input("Inserte el nombre del fichero")
    counter = 0

    with open(fileName, 'r') as file:

        for line in file:

            if line.startswith("From"):
                lineWords = line.split()
                print(lineWords[1])
                counter += 1

    print(f"Habia un total {counter} de lineas que emepezaban con From")

except FileNotFoundError:
    print(f"No se ha encontrado el archivo, vuelva a intentarlo")