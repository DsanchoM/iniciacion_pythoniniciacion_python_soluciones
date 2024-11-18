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

    max_mails = None
    max_email = None

    for email, count in mails.items():
        if max_mails is None or count > max_mails:
            max_mails = count
            max_email = email

    if max_email:
        print(f"La persona con más mensajes es: {max_email} con {max_mails} mensajes.")


except FileNotFoundError:
    print(f"No se ha encontrado el archivo, vuelva a intentarlo")
