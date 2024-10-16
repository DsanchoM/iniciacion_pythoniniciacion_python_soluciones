#EJERCICIO 4: Escribe un programa que solicite al usuario una temperatura
# en grados Celsius, convierta la temperatura a Fahrenheit e imprima la temperatura convertida

temperatura_c = input("Por favor, introduce la temperatura actual en grados Celsius\n")
temperatura_f = (int(temperatura_c) * 1.8) + 32
print ("{} grados Celsius equivalen a {} grados Fahrenheit". format((temperatura_c), temperatura_f))