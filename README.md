## proyecto-pci "Gato"

Sebastián Osorio Arteaga A01706119

CONTEXTO

Para este proyecto de la materia me gustaria hacer el juego del gato(tic-tac-toe), ya que pienso que es lo demasiado complicado como para incluir todo el temario a tratar de la clase como es el tema de las funciones, operadores lógicos, funciones, etc. y pienso que tampoco es demasiado sencillo, además de que en las anteriores tarea de la preparatoria nunca se nos planteo un proyecto como un juego o algo parecido, y solo haciamos tareas como cuestionarios o cosas sencillaas,por lo que en mi opinion sería un buen reto 

ALGORITMO

1.-Hacer un tablero que funcionaria con una lista y cambia segun lo que ponga el usuario

tablero = ["-","-","-","-","-","-","-","-","-"] 

-|-|-       [0]|[1]|[2]     
-----       -----------
-|-|-       [3]|[4]|[5] 
-----       -----------
-|-|-       [6]|[7]|[8] 

2.-Definir variables para saber que jugador tiene el turno

jugador = "X"

3.-Hacer una función para pedirle al usuario que casilla quiere poner su X ó O y también checar en esta misma funcion si habia antes una X ó O

turno = int(input("que casilla del tablero escoges usa numeros del 1-9"))
"""(se tendra que restarle -1 al numero que de el usuario para que coincida con el numero de las listas)

4.-Hacer función para cambiar de jugador


5.-Hacer una funcion para saber quien gano en los casos horizantales, diagonales y verticales 


COMO FUNCIONA:

Es muy simple te descargas el código "gato_final.py" y corres el código, te pide nombre y edad para saber quien es el jugador (x) y el jugador(o)
después para escoger la casilla lo haces en base que el tablero de 3x3, la primera casilla
arriba a la izquierda es la posición 1 y la ultima casilla abajo a la derecha es la posición 9. 
Y gana quien quien pueda alinear 3 simbolos (x,o) :^)

