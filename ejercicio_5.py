print("*** CÁLCULO DE SALARIO BRUTO ***")
tarifa = float(input("¿A cuánto cobra usted la hora?"))
horas = float(input("¿Cuántas horas ha trabajado?"))
if horas>40:
    sueldoBase = 40 * tarifa;
    sueldoExtra = (horas-40)*(tarifa+1.5)
    print(f"Su salario bruto es de: {sueldoBase+sueldoExtra}")
else:
    print(f"Su salario bruto es de: {tarifa*horas}")