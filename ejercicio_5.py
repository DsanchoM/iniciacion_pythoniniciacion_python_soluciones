# Declaramos variable horas, el usuario introduce los datos
horas = float(input("Enter Hours: "))
# Declaramos variable tarifa
tarifa = float(input("Enter Rate: "))

# Calculamos el pago bruto
# Si es mas de 40 horas se multiplica la tarifa
if horas > 40:
    horas_extras = horas - 40
    pago_bruto = (40 * tarifa) + (horas_extras * tarifa * 1.5)
else:
    pago_bruto = horas * tarifa

# Se imprime el resultado
print(f"Pay: {pago_bruto:.2f}")