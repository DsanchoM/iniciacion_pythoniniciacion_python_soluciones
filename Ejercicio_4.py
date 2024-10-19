#EJERCICIO 4: Escribe un programa que solicita al usuario una temperatura en grados Celsius, convierte la temperatura a Fahrenheit e imprime la temperatura convertida

#SOLUCIÓN:

tempC=input("Introduzca el valor de grados Celsius que quiera convertir a Fahrenheit, por favor.\n")
tempC=int(tempC)
tempF=(tempC*9/5)+32
print(tempF,"grados Fahrenheit")
