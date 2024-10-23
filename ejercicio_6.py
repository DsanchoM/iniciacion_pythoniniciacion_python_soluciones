from itertools import filterfalse

horas = input("Introduzca las horas trabajadas: ")
tarifa = input("Introduzca la tarifa: ")
error = False

try :
    horas = float(horas)
    tarifa = float(tarifa)
except ValueError as i:
    print(f"Error, introduzca un valor numérico")
    error = True

if not error:
    sueldo = float(horas) * float(tarifa)
    print("Su sueldo bruto es: " + str(sueldo))