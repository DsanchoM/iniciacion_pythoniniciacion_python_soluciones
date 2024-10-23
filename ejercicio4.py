### Escribe un programa que solicite al usuario una temperatura en grados Celsius, convierta la temperatura a Fahrenheit e imprima la temperatura convertida

temp_C = float(input('Dime la temperatura en grados Celsius.'))
temp_F = (temp_C * (9/5)) + 32
print(f'La temperatura en grados Fahrenheit es de {temp_F} ')