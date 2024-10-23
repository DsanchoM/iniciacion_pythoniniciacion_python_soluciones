horas = input("Introduzca las horas trabajadas: ")
tarifa = input("Introduzca la tarifa: ")
if float(horas) > 40 :
    horas_extra = float(horas) - 40
    sueldo = (horas_extra * (float(tarifa) * 1.5)) + (40 * float(tarifa))
else :
    sueldo = float(horas) * float(tarifa)

print("Su sueldo bruto es: " + str(sueldo))