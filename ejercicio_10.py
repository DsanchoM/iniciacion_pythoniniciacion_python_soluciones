total=0
contador=0
while True:
    entrada = input("Ingrese un número o 'listo' para finalizar: ")
    if entrada.lower()=="listo":
        break
    try:
        numero=float(entrada)
        total+=numero
        contador+=1
    except ValueError:
        print("Error: Por favor, ingrese un número válido.")
if contador>0:
    promedio = total / contador
    print(f"Total: {total}")
    print(f"Recuento: {contador}")
    print(f"Promedio: {promedio}")
else:
    print("No se ingresaron números.")
