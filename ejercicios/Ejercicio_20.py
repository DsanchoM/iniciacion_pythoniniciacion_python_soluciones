try:
    fileName = input("Inserte el nombre del fichero")
    mails = {}

    with open(fileName, 'r') as file:
        for line in file:

            if line.startswith("From:"):
                lineWords = line.split()
                email = lineWords[1]

                if email in mails:
                    mails[email] += 1
                else:
                    mails[email] = 1

    print(mails)

except FileNotFoundError:
    print(f"No se ha encontrado el archivo, vuelva a intentarlo")