#Programación del mítico juego de piedra, papel o tijeras.

import random

piedra="piedra"
papel="papel"
tijeras="tijeras"
si="s"
no="n"
repetir_partida="s"
contador_jugador=0
contador_maquina=0


def resultado(opcion_jugador,opcion_maquina): #Esta función es la que analizará el resultado del juego y llevará el conteo del resultado
    if opcion_jugador==opcion_maquina:
        ganador=2     
        print("Ambos habeis escogido",opcion_jugador,"y habeis empatado.\n")
    elif opcion_jugador==piedra:
        if opcion_maquina==tijeras:
            print("Enhorabuena. La piedra chafa a las tijeras!!\n")
            ganador=0
        else:          
            print("Lástima. El papel envuelve a la piedra.\n")
            ganador=1
    elif opcion_jugador==papel:
        if opcion_maquina==piedra:
            print("Yiiijaaaa!!! El papel envolvió a la piedra!!\n")
            ganador=0
        else:
            print("Una pena pero tu papel fue cortado por las tijeras...\n")
            ganador=1            
    elif opcion_jugador==tijeras:
        if opcion_maquina==papel:
            print("Toma ya!!Tus tijeras hicieron pedacitos al papel\n")
            ganador=0           
        else:
            print("Ouchh, eso duele... La piedra destrozo tus tijeras\n")
            ganador=1
    return ganador


jugador=input("Introduce tu nombre:\n")
repeticion=[si,no]
opciones=[piedra,papel,tijeras]
while repetir_partida=="s":
    opcion_jugador=input("Piedra, papel o tijeras, escoge lo que quieras\n")
    opcion_jugador=str(opcion_jugador)
    try:
        if opcion_jugador not in opciones:
            raise ValueError
        opcion_maquina=random.choice(opciones)
        print("La máquina escogió",opcion_maquina,"\n")
        ganador= resultado(opcion_jugador,opcion_maquina)
        if ganador==0:
            contador_jugador=contador_jugador+1
        elif ganador==1:
            contador_maquina=contador_maquina+1
        print("El marcador es de:",jugador,contador_jugador,"VS Máquina",contador_maquina,"\n")    
        while True:
            repetir_partida=input("¿Quieres jugar otra partida? (s/n)\n")
            try:
                if repetir_partida not in repeticion:
                    raise ValueError
                break
            except ValueError:
                print("Opción no válida. Por favor, escoge s o n.\n")
    except ValueError:
            print("Opción no válida. Por favor, escoge entre piedra, papel o tijeras.\n")
