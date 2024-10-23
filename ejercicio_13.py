try:
    with open('mbox-short.txt','r') as file:
        # lee cada linea y la imprime para no cargar todas en memoria
        for line in file:
            print(line.strip().upper())
except:
    print("Error trying to open the file")