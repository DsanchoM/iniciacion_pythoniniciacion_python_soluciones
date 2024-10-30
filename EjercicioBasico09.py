# EJERCICIO 9: Reescribe el programa de calificación del capítulo anterior 
# (EJERCICIO 7) utilizando una función llamada "computegrade" que tome una
# puntuación como parámetro y devuelva una nota como una cadena.


def calcularGrado(funParPuntuacion):
	
	if funParPuntuacion < 0 or funParPuntuacion >1.0:
		funRango = "Fuera de Rango"
	elif funParPuntuacion >= 0.9 and funParPuntuacion <= 1.0:
		funRango = "A"
	elif funParPuntuacion >= 0.8 and funParPuntuacion < 0.9:
		funRango = "B"
	elif funParPuntuacion >= 0.7 and funParPuntuacion < 0.8:
		funRango = "C"
	elif funParPuntuacion >= 0.6 and funParPuntuacion < 0.7:
		funRango = "D"
	elif puntuacion >= 0 and puntuacion < 0.6:
		funRango = "F"
	
	return funRango

try:
	puntuacion = float(input("Puntuacion: "))

	relCalcularGradoReturn=str(calcularGrado(puntuacion))
	print(relCalcularGradoReturn)

except:
	
	print("Entre un numero entre 0.0 y 1.0")

