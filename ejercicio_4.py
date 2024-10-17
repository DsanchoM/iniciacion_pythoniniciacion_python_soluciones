#Ejercicio 4. Escribe un programa que solicite al usuario una temperatura en grados Celsius, convierta la temperatura a Fahrenheit e imprima la temperatura convertida

celsius = input("Indica la temperatura en grados Celsius: ")
fahrenheit = (float(celsius) * 1.8) + 32
print("La temperatura en grados Fahrenheit es: {}".format(fahrenheit))
