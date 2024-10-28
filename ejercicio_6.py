print("*** CÁLCULO DE SALARIO BRUTO ***")
try:
    tarifa = float(input("¿A cuánto cobra usted la hora?"))
    horas = float(input("¿Cuántas horas ha trabajado?"))
    print(f"Su salario bruto es de: {tarifa*horas}")
except:
    print("Error: Por favor, ingrese un número válido para la tarifa y las horas trabajadas.")