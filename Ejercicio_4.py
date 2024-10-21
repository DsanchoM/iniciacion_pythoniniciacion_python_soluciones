# EJERCICIO 4: Escribe un programa que solicite al usuario una temperatura en grados Celsius, convierta la temperatura a Fahrenheit e imprima la temperatura convertida
# Fernando Sevil

celsius = input ("¿Cual es la temperatura en º Celsius?\n")
fahrenheit = ((float(celsius) * 9) / 5) + 32

print (f"Para una temperatura de {celsius}ºC le corresponde {fahrenheit}ºF\n")
