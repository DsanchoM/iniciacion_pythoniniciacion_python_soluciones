lista = []
while True:
    entrada = input("Ingrese un número o 'listo' para finalizar: ")
    if entrada.lower()=="listo":
        break
    try:
        numero=float(entrada)
        lista.append(numero)
    except ValueError:
        print("Error: Por favor, ingrese un número válido.")
if lista:
    max = max(lista)
    min = min(lista)
    print(f"Máximo: {max}")
    print(f"Mínimo: {min}")
else:
    print("No se han introducido números")