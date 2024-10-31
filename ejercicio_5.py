hours = float(input("Introduce las horas : "))
fee = float(input("Introduce la tarifa por hora : "))


if hours > 40 :
    result = (hours-40)*fee + (40*fee*1.5) 
else:
    result = (hours)*fee  


print(f"El pago en bruto sera de {result} 💵")