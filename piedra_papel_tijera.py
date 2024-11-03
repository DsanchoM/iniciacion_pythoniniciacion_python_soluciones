import random
validador = True
contador = 0
gana_jugador = 0
gana_maquina = 0
empate = 0
def validar_jugada (tirada_jugador, tirada_maquina):
    """Funcion para validar la jugada"""
    if (tirada_jugador == tirada_maquina):
        print (f"Tú has jugado {tirada_jugador} y la máquina ha jugado {tirada_maquina}. Hay empate.\n")
        return "empate"
    elif (tirada_jugador == "piedra" and tirada_maquina == "papel") or (tirada_jugador == "papel" and tirada_maquina == "tijera")or (tirada_jugador == "tijera" and tirada_maquina == "pìedra"):
        print(f"Tú has jugado {tirada_jugador} y la máquina ha jugado {tirada_maquina}. Gana la máquina.\n")
        return "maquina"
    else:
        print(f"Tú has jugado {tirada_jugador} y la máquina ha jugado {tirada_maquina}. Has ganado.\n")
        return "jugador"


print("*****Juego de piedra, papel o tijera*****\n")
print("Cuando desees finalizar, escribe 'Fin'\n")

while validador:
    tirada_jugador = input ("Elige una opción para jugar: piedra, papel o tijera:\n")

    if tirada_jugador == "Fin":
        print(f"Juego finalizado. Se han jugado {contador} partidas.\nTú has ganado {gana_jugador}.\nLa máquina ha ganado {gana_maquina}.\nHabéis empatado {empate} veces.")
        validador = False

    elif tirada_jugador == "piedra" or tirada_jugador == "papel" or tirada_jugador == "tijera":
        tirada_maquina = random.choice (["piedra", "papel", "tijera"])
        contador +=1
        resultado = validar_jugada (tirada_jugador, tirada_maquina)
        if (resultado == "empate"):
            empate += 1
        elif (resultado == "jugador"):
            gana_jugador += 1
        else:
            gana_maquina +=1
        print (f"Llevais {contador} partidas. Tú has ganado {gana_jugador} y la máquina ha ganado {gana_maquina}. Empates: {empate}\n" )
    else:
        print("Por favor, escribe solo una de las opciones posibles.\n")