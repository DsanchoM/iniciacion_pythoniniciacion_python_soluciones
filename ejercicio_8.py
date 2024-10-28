print("*** CÁLCULO DE SALARIO BRUTO ***")
tarifa = float(input("¿A cuánto cobra usted la hora?"))
horas = float(input("¿Cuántas horas ha trabajado?"))
print(f"Su salario bruto es de: {tarifa*horas}€")
horasE = float(input("¿Cuántas horas extra ha trabajado?"))
tarifaE = float(input("¿A cuánto cobra usted la hora extra?"))

def computeplay(hours, rate):
    extra = hours*rate
    print(f"Su salario extra es de {extra}€")
computeplay(horasE,tarifaE)
