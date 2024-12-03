# Desarrollar un código que emule una partida del famoso juego piedra papel y tijera,
# entre la máquina y el usuario.
# El código debe tener las siguientes características:
# 1.El programa le pide al usuario que elija entre las tres posibilidades
# 2.Sacar un mensaje de error si el usuario no ha introducido bien su respuesta
# 3.El programa devuelve una frase diciendo qué ha sacado la máquina y si gana o pierde el usuario
# 4.El programa se ejecuta constantemente. (pregunta de nuevo cuando la partida ha terminado)
# 5.Se han de emplear (funciones, bucles, condicionales, try/except,)
# 6.Voluntario (llevar el conteo de las partidas ganadas cada uno y se muestre en cada ronda

import random

# Contadores de victorias
user_wins = 0
machine_wins = 0

# Función para jugar una ronda
def play_round():
    global user_wins, machine_wins
    options = ["piedra", "papel", "tijera"]
    machine_choice = random.choice(options)
    
    # Pedir al usuario que ingrese su elección
    user_choice = input("Elige entre piedra, papel o tijera: ").lower()
    
    # Validación de entrada
    if user_choice not in options:
        print("Entrada inválida. Por favor, elige entre 'piedra', 'papel' o 'tijera'.")
        return  # Sale de la función sin contar la partida

    print(f"La máquina eligió: {machine_choice}")

    # Determinar el ganador
    if user_choice == machine_choice:
        print("Empate!")
    elif (user_choice == "piedra" and machine_choice == "tijera") or \
         (user_choice == "papel" and machine_choice == "piedra") or \
         (user_choice == "tijera" and machine_choice == "papel"):
        print("¡Ganaste esta ronda!")
        user_wins += 1
    else:
        print("La máquina gana esta ronda.")
        machine_wins += 1

    # Mostrar el conteo de victorias
    print(f"Puntaje: Usuario {user_wins} - Máquina {machine_wins}\n")

# Bucle principal del juego
while True:
    try:
        play_round()
        
        # Preguntar al usuario si quiere jugar otra ronda
        play_again = input("¿Quieres jugar otra vez? (sí/no): ").lower()
        if play_again != "sí":
            print("Gracias por jugar!")
            break
    except Exception as e:
        print("Ocurrió un error inesperado:", e)
