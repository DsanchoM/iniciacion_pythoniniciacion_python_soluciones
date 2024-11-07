# EJERCICIO 10: Escribe un programa que lea números repetidamente hasta que el usuario ingrese "listo". 
# Una vez que se ingrese "listo", imprima el suma, el recuento y el promedio de los números. 
# Si el usuario ingresa algo que no sea un número, detecta su error usando "try" y "except" e imprime un mensaje de error y salta al siguiente número. 
# Ejemplo de ejecución:
# Enter a numero: 4
# Enter a numero: 5
# Enter a numero: bad data
# Invalid input
# Enter a numero: 7
# Enter a numero: done
# 16 3 5.333333333333333
# EJERCICIO 11: Escribe otro programa que solicite una lista de números como arriba y al final imprima el máximo y el mínimo 
# de los números en lugar del promedio.

max_num = None
min_num = None

while True:
    usuario_input = input("introduce un número: ")
    if usuario_input.lower() == "listo":
        break
    try:
        numero = float(usuario_input)
        # Actualizar el máximo y mínimo
        if max_num is None or numero > max_num:
            max_num = numero
        if min_num is None or numero < min_num:
            min_num = numero
    except ValueError:
        print("No es un número, valor invalido")

if max_num is not None and min_num is not None:
    print("El máximo es: " + str( max_num) + " y el mínimo es: " +  str(min_num))
else:
    print("No ha metido ningun valor con número.")