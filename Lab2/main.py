
from gamemodel import *
from gamegraphics import *


def graphicFire(game, angle, vel):
    player = game.getCurrentPlayer()

    gproj = player.fire(angle, vel)
    while gproj.isMoving():
        gproj.update(1 / 50)
        update(50)
    return gproj


def graphicPlay():
    game = Game(10, 3)
    ggame = GraphicGame(game)

    while True:
        angle, vel = gameInput(ggame)
        proj = graphicFire(ggame, angle, vel)
        finishShot(ggame, proj)


def gameInput(game):
    player = game.getCurrentPlayer()
    oldAngle, oldVelocity = player.getAim()
    wind = game.getCurrentWind()
    theOldInputs = InputDialog(oldAngle, oldVelocity, wind)
    interaction = theOldInputs.interact()

    if interaction == "Fire!":
        InputDialog.close(theOldInputs)
        return InputDialog.getValues(theOldInputs)
    elif interaction == "Quit":
        quit()


def finishShot(game, proj):
    player = game.getCurrentPlayer()

    other = game.getOtherPlayer()

    distance = other.projectileDistance(proj)
    if distance == 0.0:
        player.increaseScore()

        game.newRound()

    game.nextPlayer()
    # game.nextPlayer()


graphicPlay()
