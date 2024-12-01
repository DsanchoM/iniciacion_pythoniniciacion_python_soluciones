#EJERCICIO 10: Escribe un programa que lea números repetidamente hasta que el usuario ingrese "listo". Una vez que se ingrese "listo", imprima el total, el recuento y el promedio de los números. Si el usuario ingresa algo que no sea un número, detecta su error usando "try" y "except" e imprime un mensaje de error y salta al siguiente número.

#SOLUCIÓN:

recuento=0
b_anterior=0
b_primero=0
while True:
    b_primero=input("Introduzca el primer dato:\n")
    try:
        b_primero=float(b_primero)
        b_anterior=b_primero
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
    promedio=suma/recuento
    b_anterior=suma
    b=input("introduzca más datos o diga listo para finalizar, por favor\n")
    try:
        b=float(b)
    except:
        if b=="listo":
            break
        else:
            print ("Error. Parámetro no válido")
            b=0
            recuento=recuento-1
print("la suma de los números introducidos es ",suma,"\n")
print("el total de números introducidos es de ",recuento,"\n")
print("el valor promedio de los números introducidos es de ",promedio,"\n")
