"""Memory, puzzle game of number pairs.
Cambios:
1. Contar y desplegar el numero de taps
2. Detectar cuando todos los cuadros se han destapado
3. Central el dígito en el cuadro
4. Como un condimento de innovación al juego. Podrías utilizar algo diferente a los dígitos para resolver el juego y que al usuario le ayude a tener mejor memoria ?

Editado por:
David Alonso Chang Ortega 
Emmanuel Cruz Durán A01658410 - Modificación Realizada "Centrar los dígitos en los cuadros"
"""

from random import *
from turtle import *

from freegames import path

car = path('car.gif')
tiles = ["😊", "😇", "🙂", "🙃", "😉", "😌", "😍", "🥰", "😘", "😗", "😙", "😚", "😋", "😛", "😝", "😜", "🤪", "🤨", "🧐", "🤓", "😎", "🥸","😀", "😃", "😄", "😁", "😆", "😅", "😂", "🤣", "🥲"] * 2
state = {'mark': None}
hide = [True] * 64
numTaps = 0



def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""

    """Contador de taps"""
    global numTaps
    numTaps += 1

    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x+26, y)
        color('grey')
        write(tiles[mark],align="center",font=('Arial', 30, 'normal'))

    """Dibujar los taps"""
    goto(-200,200)
    #Contar y desplegar el numero de taps
    write(f"Taps: {numTaps}",False,font=("Arial" ,12,"normal"))
    update()
    ontimer(draw, 100)

    """Mostrar que el juego ya acabó"""
    if all(h == False for h in hide):
        goto(-100, 0)
        color('green')
        write('¡Juego terminado!', font=('Arial', 20, 'bold'))


shuffle(tiles)
setup(460, 460, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
