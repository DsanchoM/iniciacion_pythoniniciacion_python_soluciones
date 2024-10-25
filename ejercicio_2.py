# declaramos variable horas, el usuario introduce los datos
horas = float(input("Introduce tus horas trabajadas:"))
# declaramos variable tarifa
tarifa = float(input("Introduce tu tarifa por hora:"))
#calculamos la variable pago_bruto 
pago_bruto = horas * tarifa
#se imprime primera f es f-string 
# el :.2f significa, los : que se va a aplicar un formato, 
# 2 num de decimales, f es float en este caso
print(f"Tu pago bruto es: {pago_bruto:.2f}")