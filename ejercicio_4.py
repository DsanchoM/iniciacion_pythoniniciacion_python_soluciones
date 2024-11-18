'''
EJERCICIO 4: Escribe un programa que solicite al usuario una temperatura en grados Celsius,
convierta la temperatura a Fahrenheit e imprima la temperatura convertida
'''
grados_celsius = int(input('Introduce los grados celsisus que quieres convertir a Fahrenheit: '))
fahrenheit = grados_celsius * 9/5 +32
print(f'Los {grados_celsius} grados celsius equivalen a {fahrenheit} fahrenheit')