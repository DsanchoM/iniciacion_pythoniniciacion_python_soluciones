import random

def contador (numero:int)->int:
    numero += 1
    return numero

var=''
ganadas_maquina,ganadas_persona = 0,0
lista = ['piedra', 'papel', 'tijera']
while var!='salir':
    try:
        var = input('Introduce piedra, papel o tijera: ')
        if type(var) != type('str') or var not in lista:
            print('Aprende a escribir')
        else:
            maquina=random.choice(lista) #Que elija un elemento de la lista aleatoriamente
            print(f'La maquina ha sacado: {maquina}' )
            if maquina == var:
                print('Empate')
            elif ((maquina =='piedra' and var=='tijera')
                  or (maquina =='papel' and var=='piedra')
                  or (maquina =='tijera' and var=='papel')):
                #ganadas_maquina += 1
                print('La maquina gana')
                ganadas_maquina = contador(ganadas_maquina)
            else:
                #ganadas_persona += 1
                print('Has ganado')
                ganadas_persona = contador(ganadas_persona)
    except e:
        print("Error")
    print(f'Has ganado {ganadas_persona} veces. La maquina ha ganado {ganadas_maquina} veces')
