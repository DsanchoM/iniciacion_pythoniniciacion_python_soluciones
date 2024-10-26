def computepay(hours, rate):
    # Calculamos el pago bruto
    if hours > 40:
        horas_extras = hours - 40
        pago_bruto = (40 * rate) + (horas_extras * rate * 1.5)
    else:
        pago_bruto = hours * rate
    return pago_bruto

# Solicitamos los datos al usuario
hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

# Llamamos a la función y mostramos el resultado
pago = computepay(hours, rate)
print(f"Pay: {pago:.2f}")