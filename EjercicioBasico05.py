# EJERCICIO 5: Reescribe tu cálculo de pago (EJERCICIO 2) 
# para darle al empleado 1.5 veces la tarifa por hora por las horas
# trabajadas por encima de las 40 horas. La salida es la siguiente:

# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

horasTrabajadasMasCuarenta = 0
horastarifaMasCuarenta = 0

horasTrabajadas = int(input("Horas Trabajadas: "))
horasTarifa = int(input("Tarifa de las hora: "))

if horasTrabajadas > 40:
	
	horasTrabajadasMasCuarenta = horasTrabajadas - 40
	pagoBrutoMas40 = horasTrabajadasMasCuarenta * horasTarifa * 1.5
	pagoBrutoTotal = 40 * horasTarifa + pagoBrutoMas40

else:
	
	pagoBrutoTotal = horasTrabajadas * horasTarifa


print("Pago bruto a pagar total:", pagoBrutoTotal)
