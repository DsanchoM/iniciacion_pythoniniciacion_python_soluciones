try:
    hours = float(input("Introduce las horas : "))
    fee = float(input("Introduce la tarifa por hora : "))

    print(f"El pago en bruto sera de {hours*fee}")
except ValueError:
    print(f"Error, please enter numeric input")

