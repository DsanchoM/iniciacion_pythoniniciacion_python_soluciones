#EJERCICIO 2: Escribe un programa para pedirle al usuario las horas y la tarifa por hora para calcular el pago bruto.

# Solicitar las horas y la tarifa por hora
horas = float(input("Introduce las horas (puede usar decimales): "))
tarifa_por_hora = float(input("Introduce la tarifa por hora: "))

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

#El enunciado de este ejecicio se puede interpretar de muchas formas, para mi la forma más correcta sería:

# Función para convertir una hora en formato HH:MM a minutos totales
def horas_a_minutos(hora_completa):
    horas, minutos = map(int, hora_completa.split(":"))  # Dividir por ":" y convertir a enteros
    return horas * 60 + minutos

# Solicitar la hora de inicio y la hora de fin en formato HH:MM
inicio = input("Introduce la hora de inicio (formato HH:MM): ")
fin = input("Introduce la hora de fin (formato HH:MM): ")

# Convertir las horas y minutos a minutos totales
inicio_total_minutos = horas_a_minutos(inicio)
fin_total_minutos = horas_a_minutos(fin)

# Calcular la diferencia de tiempo en minutos
minutos_totales = fin_total_minutos - inicio_total_minutos

# Solicitar la tarifa por hora
tarifa_por_hora = float(input("Introduce la tarifa por hora: "))

# Convertir minutos a horas
horas_totales = minutos_totales / 60

# Calcular el pago bruto
pago_bruto = horas_totales * tarifa_por_hora

# Separar las horas y minutos para mostrar
horas_entero = int(horas_totales)
minutos = (horas_totales - horas_entero) * 60

# Mostrar el tiempo y el pago bruto
print(f"{horas_entero} horas y {minutos:.0f} minutos.")
print(f"El pago bruto es: {pago_bruto:.2f}")


