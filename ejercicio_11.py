i=0
count = 0
print("Introduce numeros consecutivamente hasta que quieras sacar la suma total, el recuento y el promedio de estos: ")
total = 0
promedio = 0
lista = []
while i==0:
   val = input("Introduce numero: ")
   try:
       val = float(val)
       if count==0:
           grater = val
           lower = val
           count+=1
       else:
           if val>grater:
               grater=val
           if val<lower:
               lower=val
           count += 1
       lista.append(val)

   except :
       match val:
           case "listo":
               print("El valor mas pequeño de la lista es: "+str(lower))
               print("El valor más grande de la lista es: " + str(grater))
               print("Los valores introducidos han sido: " + str(lista))
               i+=1
           case _:
               print("Error en la introducción de datos")