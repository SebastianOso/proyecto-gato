""""
1.- hacer el tablero y las casillas
2.- funcion para establecer que jugador(x,o) va en turno
3.- checar si alguien gano o hay un empate 

ya creo?

"""
jugando=True

jugador = "x"

casilla=["-", "-", "-", "-", "-", "-", "-", "-", "-"]

def TableroInicial():
    print(casilla[0] + "|" + casilla[1] + "|" + casilla[2])
    print("-----")
    print(casilla[3] + "|" + casilla[4] + "|" + casilla[5])
    print("-----")
    print(casilla[6] + "|" + casilla[7] + "|" + casilla[8])

def EscogerCasilla():
    EC=int(input("Escoge un número del 1 al 9 para escoger tu casilla: \n" ))
    if EC >= 1 and EC <= 9 and casilla[EC-1] == "-":
        casilla[EC-1]=jugador
    else:
        print("parece que es casilla esta ocupada")

while jugando:
    TableroInicial()
    EscogerCasilla()



