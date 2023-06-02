
import random

num_turnos = int(input("ICuantas partidas quiere jugar: "))
nombre_jugador1 = input("Ingrese el nombre del primer jugador: ")
nombre_jugador2 = input("Ingrese el nombre del segundo jugador: ")


puntuacion_jugador1 = 0
puntuacion_jugador2 = 0


for turno in range(num_turnos):
  
    tirada_jugador1 = random.randint(1, 6)
    tirada_jugador2 = random.randint(1, 6)
    
    
    print("Turno #{}:".format(turno+1))
    print("{} sacó un {} y {} sacó un {}".format(nombre_jugador1, tirada_jugador1, nombre_jugador2, tirada_jugador2))
    
  
    if tirada_jugador1 > tirada_jugador2:
        puntuacion_jugador1 += tirada_jugador1 + tirada_jugador2
        print("{} gana el turno y suma {} puntos".format(nombre_jugador1, tirada_jugador1+tirada_jugador2))
    elif tirada_jugador2 > tirada_jugador1:
        puntuacion_jugador2 += tirada_jugador1 + tirada_jugador2
        print("{} gana el turno y suma {} puntos".format(nombre_jugador2, tirada_jugador1+tirada_jugador2))
    else:
        print("Empate, Sigue jugando para desempatar")


print("Puntuaciones finales:")
print("{}: {}".format(nombre_jugador1, puntuacion_jugador1))
print("{}: {}".format(nombre_jugador2, puntuacion_jugador2))


if puntuacion_jugador1 > puntuacion_jugador2:
    print("{} Eres un campe@n!".format(nombre_jugador1))
elif puntuacion_jugador2 > puntuacion_jugador1:
    print("{} Eres un campe@n!".format(nombre_jugador2))
else:
    print("Empate, Sigue jugando y ganaras")