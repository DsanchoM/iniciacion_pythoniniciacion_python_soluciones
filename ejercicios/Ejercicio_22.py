try:
    fileName = input("Inserte el nombre del fichero")
    mails = {}

    with open(fileName, 'r') as file:
        for line in file:

            if line.startswith("From:"):
                lineWords = line.split()
                domain = lineWords[1].split('@')[1]

                if domain in mails:
                    mails[domain] += 1
                else:
                    mails[domain] = 1

    print(mails)

except FileNotFoundError:
    print(f"No se ha encontrado el archivo, vuelva a intentarlo")