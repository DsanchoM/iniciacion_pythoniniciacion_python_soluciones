'''
Reescribe tu cálculo de pago (EJERCICIO 2) para darle al empleado 1.5 veces la tarifa por hora por las horas trabajadas por encima de las 40 horas. La salida es la siguiente:
Enter Hours: 45
Enter Rate: 10
Pay: 475.0
'''
# Solicitar las horas y la tarifa por hora
horas = float(input("Introduce las horas (puede usar decimales): "))
tarifa_por_hora = float(input("Introduce la tarifa por hora: "))

# Convertir la fracción de hora al formato correcto "sexagésimas" (asumimos que .3 son 30 minutos, es decir, media hora)
horas_corregidas = int(horas) + (horas % 1) * 10 / 6

# Separar las horas y minutos 
horas_entero = int(horas_corregidas)
minutos = (horas_corregidas - horas_entero) * 60

# Calcular el pago bruto con las horas
if(horas_corregidas > 40):
    horas_extra = horas_corregidas - 40
    pago_bruto = 40 * tarifa_por_hora + (horas_extra * tarifa_por_hora * 1.5)
else:
    pago_bruto = horas_corregidas * tarifa_por_hora

# Mostrar las horas y minutos, y el pago bruto
print(f"{horas_entero} horas y {minutos:.0f} minutos.")
print(f"El pago bruto es: {pago_bruto:.2f}")