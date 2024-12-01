#EJERCICIO 11: Escribe otro programa que solicite una lista de números como arriba y al final imprima el máximo y el mínimo de los números en lugar del promedio.

#SOLUCIÓN

recuento=0
b_anterior=0
b_primero=0
lista=[]
while True:
    b_primero=input("Introduzca el primer dato:\n")
    try:
        b_primero=float(b_primero)
        b_anterior=b_primero
        lista.append(b_primero)
        break
    except:
        print ("Error. Parámetro no válido")
b=0
while b!="listo":
    b_primero=float(b_primero)
    recuento=recuento+1
    b=float(b)
    suma=b+b_anterior
    suma=float(suma)
    b_anterior=suma
    b=input("introduzca más datos o diga listo para finalizar, por favor\n")
    try:
        b=float(b)
        lista.append(b)
    except:
        if b=="listo":
            break
        else:
            print ("Error. Parámetro no válido")
            b=0
            recuento=recuento-1
maximo=max(lista)
minimo=min(lista)
print("la suma de los números introducidos es ",suma,"\n")
print("el total de números introducidos es de ",recuento,"\n")
print("El número más grande de los introducidos ha sido el ",maximo,"\n")
print("El número más pequeño de los introducidos ha sido el ",minimo,"\n")
