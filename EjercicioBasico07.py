# EJERCICIO 7: Escribe un programa para solicitar una puntuación entre 0.0 y 1.0. 
# Si la puntuación está fuera de rango, imprime un mensaje de error. 
# Si la puntuación está entre 0.0 y 1.0, imprime una calificación usando la siguiente tabla:

# Score 	Grade
# >= 0.9 	A
# >= 0.8 	B
# >= 0.7 	C
# >= 0.6 	D
# < 0.6 	F


puntuacion = float(input("Puntuacion: "))

try:
		
	if puntuacion < 0 or  puntuacion >1.0:
		print("Fuera de rango")
	elif puntuacion >= 0.9 and puntuacion <= 1.0:
		print("A")
	elif puntuacion >= 0.8 and puntuacion < 0.9:
		print("B")
	elif puntuacion >= 0.7 and puntuacion < 0.8:
		print("C")
	elif puntuacion >= 0.6 and puntuacion < 0.7:
		print("D")
	elif puntuacion >= 0 and puntuacion < 0.6:
		print("F")
		
except:
	
	print("Entre un numero entre 0.0 y 1.0")
