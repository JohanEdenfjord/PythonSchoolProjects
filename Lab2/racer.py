from graphics import *
import racer3

def main():
    win = GraphWin("Racer", 800, 600, autoflush=False)
    win.setCoords(-400, -300, 400, 300)
    racer = racer3.RacerGraphic(racer3.Racer(), win)

    while True:

        racer.checkBorders()

        key = win.checkKey()
        if key == "Up":
            racer.accelerate(0,1)
        elif key == "Down":
            racer.accelerate(0,-1)
        elif key == "Right":
            racer.accelerate(1,0)
        elif key == "Left":
            racer.accelerate(-1,0)
        elif key == "space":
            racer.slowDown()
        elif key == "BackSpace":
            racer.reset()

        racer.drive()
        update(50)


main()
