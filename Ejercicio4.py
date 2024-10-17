# EJERCICIO 4: Escribe un programa que solicite al usuario una temperatura en grados Celsius, 
# convierta la temperatura a Fahrenheit e imprima la temperatura convertida

celsius = float(input("Por favor, introduce la temperatura en grados celsius: "))
fahrenheit = (celsius*9 / 5) + 32
print (str(celsius) + "grados Celsius (ºC) son "  + str(fahrenheit) + " grados fahrenheit (ºF).")
