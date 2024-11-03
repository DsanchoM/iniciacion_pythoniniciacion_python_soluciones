#EJERCICIO 11: Escribe otro programa que solicite una lista de números
# como arriba y al final imprima el máximo y el mínimo de los números
# en lugar del promedio.

print("Para dejar de introducir números, escribe 'Listo'")
lista = []
while True:
    num = input("Introduce un número:\n")
    if str(num) != "Listo":
        try:
            num = int(num)
            lista.append(num)
        except:
            print("No has introducido un número")
    else:
        maximo = max(lista)
        minimo = min (lista)
        print(f"Has introducido los números {lista}. El máximo es {maximo} y el mínimo es {minimo}. \n")
        break
