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
       count += 1
       total += val
       promedio = total/count
       lista.append(val)

   except :
       match val:
           case "listo":
               print("El promedio de todos los valores introducidos es: "+str(promedio))
               print("Los valores introducidos han sido: " + str(lista))
               print("La suma total de todos los valores ha sido: " + str(total))
               i+=1
           case _:
               print("Error en la introducción de datos")

