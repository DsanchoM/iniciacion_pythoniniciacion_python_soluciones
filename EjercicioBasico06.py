# EJERCICIO 6: Reescribe tu programa de pago usando 
# (EJERCICIO 2) "try" y "except" para que su programa maneje la 
# entrada no numérica correctamente imprimiendo un mensaje y saliendo del programa. 
# A continuación se muestran una ejecución del programa:

# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input

try: 
	horasTrabajadas = int(input("Horas Trabajadas: "))
	horasTarifa = int(input("Tarifa de las horas: "))

	pagoBruto = horasTrabajadas * horasTarifa

	print("Pago bruto a pagar:", pagoBruto)
except:
	print("Entre un numero")
