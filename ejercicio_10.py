#EJERCICIO 10: Escribe un programa que lea números repetidamente
# hasta que el usuario ingrese "listo". Una vez que se ingrese "listo",
# imprima el total, el recuento y el promedio de los números.
# Si el usuario ingresa algo que no sea un número, detecta su error
# usando "try" y "except" e imprime un mensaje de error y salta al siguiente número.

print("Para dejar de introducir números, escribe 'Listo'")

suma = 0
contador = 0
promedio = 0
while True:
    num = input("Introduce un número:\n")
    if str(num) != "Listo":
        try:
            num = int(num)
            suma += num
            contador += 1

        except:
            print("No has introducido un número")

    else:
        promedio = suma / contador
        print(f"Has introducido {contador} números, que suman {suma} y su promedio es {promedio}\n")
        break
