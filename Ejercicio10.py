# EJERCICIO 10: para probar git y sentencias
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

suma = 0
numerodenumeros = 0

while True:
    usuario_input = input("introduce un número: ")
    if usuario_input.lower() == "listo":
        break
    try:
        numero = float(usuario_input)
        suma += numero
        numerodenumeros += 1
    except ValueError:
        print("No es un número, valor invalido")

if numerodenumeros > 0:
    media = suma / numerodenumeros
    print("La suma de los números es: " + str( suma) + ", ha metido " +  str(numerodenumeros) + " números, y su media es: "  +  str(media))
else:
    print("No ha metido ningun valor con número.")