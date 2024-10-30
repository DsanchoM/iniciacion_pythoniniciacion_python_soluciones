# EJERCICIO 8: Reescribe su cálculo de pago (EJERCICIO 2) con tiempo y medio para horas 
# extras y crea una función llamada "computepay" que tome dos parámetros ("hours" y "rate").


def CalcularPago(funParHorasTrabajadas, funParTarifa):
	
	funPagoBruto = funParHorasTrabajadas * funParTarifa

	print("Pago bruto a pagar:", funPagoBruto)

horasTrabajadas = int(input("Horas Trabajadas: "))
horasTarifa = int(input("Tarifa de las horas: "))

resultadoFuncionCalcularPago=CalcularPago(horasTrabajadas,horasTarifa)
print(resultadoFuncionCalcularPago)
