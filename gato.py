"""
1.- hacer el tablero y las casillas
2.- funcion para escoger casilla
3.- funcion para establecer que jugador(x,o) va en turno
4.- checar si alguien gano o hay un empate 
5.- 

"""
import os

os.system("cls")

jugando=True #poner true y acabar el ciclo del juego

jugador = "x" #el primer jugador va a ser la x

ganador="" #al momento de iniciar el jueog no hay ganador

casilla=["-", "-", "-", "-", "-", "-", "-", "-", "-"]

def TableroInicial(): #funcion para imprimir el tablero y va cambiando con el input del usuario
    print(casilla[0] + "|" + casilla[1] + "|" + casilla[2])
    print("-----")
    print(casilla[3] + "|" + casilla[4] + "|" + casilla[5])
    print("-----")
    print(casilla[6] + "|" + casilla[7] + "|" + casilla[8])


def EscogerCasilla(): #funcion para escoger casilla
    EC=input("Escoge un número del 1 al 9 para escoger tu casilla: \n")
    EC_int=int(float(EC)) #innecesario el int(float()) pero no ejecutaba
    if EC_int >= 1 and EC_int <= 9 and casilla[EC_int-1] == "-": #Ec= escoger casilla
        casilla[EC_int-1]=jugador
    elif EC_int == " ":
        print("no pusiste un numero vuelve a intentarlo")
    else:
        print("¡parece que es casilla esta ocupada!")
        input()


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
        ganador=casilla[2]
    elif casilla[3] == casilla[4] ==casilla[5] != "-":
        ganador=casilla[4]
    elif casilla[6] == casilla[8] == casilla[7] != "-":
        ganador=casilla[6]
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


#def empate():
    #global ganador
    #if casilla[0] != casilla[1] !=casilla[2] != casilla[3] != casilla[4] != casilla[5] != casilla[6] != casilla[7] !=casilla[8]:
        #ganador=None
        #jugando=False


def ganador_diag(): #ganador en diagonal
    global ganador
    if casilla[0]==casilla[4]==casilla[8]:
        ganador=casilla[8]
    return ganador


while jugando:
    os.system("cls")
    TableroInicial()
    EscogerCasilla()
    ganador_diag()
    ganador_hor()
    ganador_ver()
    if ganador == jugador: 
        jugando=False
        print(TableroInicial())
        print("el ganador es", ganador)
    cambiar_jugador()
   

    