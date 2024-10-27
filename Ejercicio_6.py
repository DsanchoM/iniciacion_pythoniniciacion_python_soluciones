# EJERCICIO 6: Reescribe tu programa de pago usando (EJERCICIO 2) "try" y "except" para que su programa maneje la entrada no numérica correctamente imprimiendo un mensaje y saliendo del programa
# Fernando Sevil

try:
    horas = int(input("¿Cuantas horas se han trabajado? \n"))
    tarifa = int(input("¿Cual es la tarifa por hora? \n"))
except ValueError:
    print("Error: Por favor, introduce valores numéricos.")
    exit()  # Salir del programa si hay un error

horas_extra = int(horas) - 40 
sueldo = horas * tarifa

if horas_extra>0:
    sueldo = sueldo + (horas_extra*tarifa/2) # Agregar el pago de horas extra

print(f"El pago bruto es {horas} horas por {tarifa} euros la hora: {sueldo}€\n")
