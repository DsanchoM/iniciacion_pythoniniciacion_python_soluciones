#EJERCICIO 4: Escribe un programa que solicite al usuario una temperatura en grados Celsius, convierta la temperatura a Fahrenheit e imprima la temperatura convertida

# Solicitar la temperatura en grados Celsius
celsius = float(input("Introduce la temperatura en grados Celsius: "))

# Convertir a grados Fahrenheit
fahrenheit = (celsius * 1.8) + 32

# Mostrar la temperatura convertida
print(f"La temperatura en grados Fahrenheit es: {fahrenheit:.2f}")
