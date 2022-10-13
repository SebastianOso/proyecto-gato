import os
#funciones

def tablero_inicial(): #funcion para imprimir el tablero y va cambiando con el input del usuario tiene + para que se vea junto
    print(casilla[0] + "|" + casilla[1] + "|" + casilla[2])
    print("-----")
    print(casilla[3] + "|" + casilla[4] + "|" + casilla[5])
    print("-----")
    print(casilla[6] + "|" + casilla[7] + "|" + casilla[8])
     

def cambiar_jugador():

    global jugador

    if jugador == "x":

        jugador = "o"

    else:

        jugador = "x"


#ganador horizontal
def ganador_hor():

    global ganador

    if casilla[0] == casilla[1] == casilla[2] != "-":

        ganador = casilla[2]

    elif casilla[3] == casilla[4] ==casilla[5] != "-":

        ganador = casilla[4]

    elif casilla[6] == casilla[8] == casilla[7] != "-":

        ganador = casilla[6]

    return ganador 


def ganador_ver(): #ganador vertical

    global ganador

    if casilla[0]==casilla[3]==casilla[6] != "-":

        ganador=casilla[3]

    elif casilla[1]==casilla[4]==casilla[7] != "-":

        ganador=casilla[1]

    elif casilla[2]==casilla[5]==casilla[8] != "-":

        ganador=casilla[2]

    return ganador


def ganador_diag(): #ganador en diagonal

    global ganador

    if casilla[0]==casilla[4]==casilla[8] != "-":

        ganador = casilla[8]

    elif casilla[2]==casilla[4]==casilla[6] != "-":

        ganador = casilla[6]

    return ganador

def empate():
    global jugando

    if "-" not in casilla:

        print(tablero_inicial())
        print("Es un empate")

        jugando=False

#menu de inicio

os.system("cls")

print("Bienvenido al juego del gato")
print("")
print("Este juego es para 2 personas")
print("Es muy fácil gana quien pueda alinear 3 simbolos (x,o) ")

nombre1 = input(("Nombre jugador 1 (x): "))

edad1 = int(input("Edad jugador 1 : "))

nombre2 =input(("Nombre jugador 2 (o): "))

edad2 = int(input("Edad jugador 2: "))

jugador1 =[nombre1,edad1]

jugador2 =[nombre2,edad2]

jugadores =[jugador1,jugador2]

print("Los jugdores son:")
print("")

for jugador in range(len(jugadores)):

    indice_jugador=jugadores[jugador]
    len_jugadores=len(indice_jugador)

    for data in range(len_jugadores):
        if data == 0:
            print(jugadores[jugador][data])

if jugador1[1] >= (jugador2[1] +3):

    print(jugador1[0],", es más grande que ", jugador2[0], end="")

    print("puede tener más ventaja")

elif  jugador2[1] >= (jugador1[1] +3):

    print(jugador2[0],", es más grande que ", jugador1[0], end=" ", )

    print("puede tener más ventaja")

print("")
input("pulsa enter  para continuar")

#variables para jugar

jugando=True #poner true y acabar el ciclo del juego

jugador = "x" #el primer jugador va a ser la x

ganador="" #al momento de iniciar el jueog no hay ganador

casilla=["-", "-", "-", "-", "-", "-", "-", "-", "-"]


while jugando:

    os.system("cls")

    tablero_inicial()

    #no se hizo funcion de escoger casilla para usar el continue
    escoger_casilla = int(input("Escoge un número del 1 al 9 para escoger tu casilla: \n"))

    if escoger_casilla >= 1 and escoger_casilla <= 9 and casilla[escoger_casilla-1] == "-":

        casilla[escoger_casilla-1] = jugador

    else:

        print("¡parece que es casilla esta ocupada!")
        input("pulse enter para continuar")
        continue

    ganador_diag()

    ganador_hor()

    ganador_ver()

    empate()

    if ganador == jugador: 
        print(tablero_inicial())

        if jugador == "x":

            print("el ganador es", jugador1[0])
            break

        if jugador == "o":

            print("el ganador es", jugador2[0] )
            break

    cambiar_jugador()
   

    