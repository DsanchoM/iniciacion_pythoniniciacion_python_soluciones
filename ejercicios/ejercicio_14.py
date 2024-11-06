try:
    fileName = input("Inserte el nombre del fichero")

    spamValue = 0
    counter = 0

    with open(fileName,'r') as file:
        for line in file:
            if line.startswith( "X-DSPAM-Confidence:"):
                number = float(line[line.find(':') + 1:].strip())
                spamValue += number
                counter += 1

    if counter > 0:
        average = spamValue / counter
        print(f"La confianza promedio del spam es: {average}")
    else:
        print("No se ha encontrado ninugna línea con 'X-DSPAM-Confidence:' en el archivo")

except FileNotFoundError:
    print(f"No se ha encontrado el archivo, vuelva a intentarlo")