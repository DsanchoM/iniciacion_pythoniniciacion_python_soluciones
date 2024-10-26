# Función para obtener horas trabajadas
def obtener_horas():
    while True:
        try:
            horas = float(input("Enter Hours: "))
            return horas
        except ValueError:
            print("Error, please enter numeric input")

# Función para obtener tarifa por hora
def obtener_tarifa():
    while True:
        try:
            tarifa = float(input("Enter Rate: "))
            return tarifa
        except ValueError:
            print("Error, please enter numeric input")

# Obtenemos datos del usuario
horas = obtener_horas()
tarifa = obtener_tarifa()

# Calculamos el pago bruto
pago_bruto = horas * tarifa

# Se imprime el resultado
print(f"Pay: {pago_bruto:.2f}")