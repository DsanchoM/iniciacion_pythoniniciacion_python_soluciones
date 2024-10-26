'''
Reescribe tu programa de pago usando (EJERCICIO 2) "try" y "except" para que su programa maneje la entrada no numérica correctamente imprimiendo un mensaje y saliendo del programa. 
A continuación se muestran una ejecución del programa:
Enter Hours: 20
Enter Rate: nine
Error, please enter numeric input
'''

# Solicitar las horas y la tarifa por hora
while True:
    try:
        horas = float(input("Introduce las horas (puede usar decimales): "))
        tarifa_por_hora = float(input("Introduce la tarifa por hora: "))
        break
    except ValueError:
        print("Error: Debes ingresar números para las horas y la tarifa.")


# Convertir la fracción de hora al formato correcto "sexagésimas" (asumimos que .3 son 30 minutos, es decir, media hora)
horas_corregidas = int(horas) + (horas % 1) * 10 / 6

# Separar las horas y minutos 
horas_entero = int(horas_corregidas)
minutos = (horas_corregidas - horas_entero) * 60

# Calcular el pago bruto con las horas corregidas
pago_bruto = horas_corregidas * tarifa_por_hora

# Mostrar las horas y minutos, y el pago bruto
print(f"{horas_entero} horas y {minutos:.0f} minutos.")
print(f"El pago bruto es: {pago_bruto:.2f}")