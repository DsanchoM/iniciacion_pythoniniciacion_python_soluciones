"""
EJERCICIO 6: Reescribe tu programa de pago usando (EJERCICIO 2) "try" y "except" para que su programa maneje la entrada no numérica correctamente 
imprimiendo un mensaje y saliendo del programa. A continuación se muestran una ejecución del programa:
"""
try:
    horas = input("Indica tus horas: ")
    tarifa = input("Indica tu tarifa: ")
    jornada_normal = 40
    if float(horas) > jornada_normal:
        horas_extras = float(horas) - jornada_normal
        total = (jornada_normal * float(tarifa)) + (horas_extras * (float(tarifa) * 1.5))
        print("Tus Horas extras pagadas a 1.5 la tarifa son: {}".format(horas_extras))
        print("Total bruto que hay que pagar: {}".format(total))
    else:
        total = float(horas) * float(tarifa)
        print("Total bruto que hay que pagar: {}".format(total))
except: 
    print("Tanto las horas como la tarifa deben ser números")
