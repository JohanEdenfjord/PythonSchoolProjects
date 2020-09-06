from graphics import *


class GraphicGame:

    def __init__(self, game):
        self.model = game

        self.win = GraphWin("Cannon Game", 640, 480, autoflush=False)
        self.win.setCoords(-110, -10, 110, 155)

        self.line = Line(Point(-110, 0), Point(110, 0))
        self.line.draw(self.getWindow())

        self.model.players[0] = GraphicPlayer(self.model.players[0], self)
        self.model.players[1] = GraphicPlayer(self.model.players[1], self)

    def getBallSize(self):
        return self.model.getBallSize()

    def getCannonSize(self):
        return self.model.getCannonSize()

    def getPlayers(self):
        return self.model.getPlayers()

    def getCurrentPlayerNumber(self):
        return self.model.getCurrentPlayerNumber()

    def getCurrentPlayer(self):
        return self.model.getCurrentPlayer()

    def getOtherPlayer(self):
        return self.model.getOtherPlayer()

    def getCurrentWind(self):
        return self.model.getCurrentWind()

    def setCurrentWind(self, wind):
        return self.model.setCurrentWind(wind)

    def nextPlayer(self):
        return self.model.nextPlayer()

    def newRound(self):
        self.model.newRound()

    def getWindow(self):
        return self.win


class GraphicPlayer:

    def __init__(self, player, game):
        self.player = player
        self.game = game
        self.proj = None

        self.cannonPoint1 = Point(self.player.getX() - self.game.getCannonSize() / 2, self.game.getCannonSize())
        self.cannonPoint2 = Point(self.player.getX() + self.game.getCannonSize() / 2, 0)
        self.cannon = Rectangle(self.cannonPoint1, self.cannonPoint2)
        self.cannon.setFill(self.player.getColor())
        self.cannon.draw(self.game.getWindow())

        self.score = Text(Point(self.player.getX(), -self.game.getCannonSize() / 2), "Score:" + str(self.getScore()))
        self.score.draw(self.game.getWindow())

    def fire(self, angle, vel):
        if self.proj is not None:
            self.proj.undraw()

        proj = self.player.fire(angle, vel)
        self.proj = GraphicProjectile(proj, self.player, self.game)

        return self.proj

    def getAim(self):
        return self.player.getAim()

    def getColor(self):
        return self.player.getColor()

    def getX(self):
        return self.player.getX()

    def getScore(self):
        return self.player.getScore()

    def projectileDistance(self, proj):
        return self.player.projectileDistance(proj)

    def increaseScore(self):
        self.player.increaseScore()
        score = "score: " + str(self.getScore())
        self.score.setText(score)


class GraphicProjectile:

    def __init__(self, projectile, player, game):
        self.proj = projectile
        self.player = player
        self.game = game

        self.ballSize = self.game.getBallSize()
        self.ballPoint = Point(self.proj.getX(), self.proj.getY())
        self.ball = Circle(self.ballPoint, self.ballSize)
        self.ball.setFill(self.player.getColor())
        self.ball.draw(self.game.getWindow())

    def update(self, dt):

        self.proj.update(dt)

        center = self.ball.getCenter()
        dx = self.proj.getX() - center.getX()
        dy = self.proj.getY() - center.getY()
        self.ball.move(dx, dy)

    def getX(self):
        return self.proj.getX()

    def getY(self):
        return self.proj.getY()

    def isMoving(self):
        return self.proj.isMoving()

    def undraw(self):
        self.ball.undraw()


class InputDialog:
    """ Takes the initial angle and velocity values, and the current wind value """

    def __init__(self, angle, vel, wind):
        self.win = win = GraphWin("Fire", 200, 300)
        win.setCoords(0, 4.5, 4, .5)
        Text(Point(1, 1), "Angle").draw(win)
        self.angle = Entry(Point(3, 1), 5).draw(win)
        self.angle.setText(str(angle))

        Text(Point(1, 2), "Velocity").draw(win)
        self.vel = Entry(Point(3, 2), 5).draw(win)
        self.vel.setText(str(vel))

        Text(Point(1, 3), "Wind").draw(win)
        self.height = Text(Point(3, 3), 5).draw(win)
        self.height.setText("{0:.2f}".format(wind))

        self.fire = Button(win, Point(1, 4), 1.25, .5, "Fire!")
        self.fire.activate()
        self.quit = Button(win, Point(3, 4), 1.25, .5, "Quit")
        self.quit.activate()

    """ Runs a loop until the user presses either the quit or fire button """

    def interact(self):
        while True:
            pt = self.win.getMouse()
            if self.quit.clicked(pt):
                return "Quit"
            if self.fire.clicked(pt):
                return "Fire!"

    """ Returns the current values of (angle, velocity) as entered by the user"""

    def getValues(self):
        a = float(self.angle.getText())
        v = float(self.vel.getText())
        return a, v

    def close(self):
        self.win.close()


""" A general button class (from the book) """


class Button:
    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""

    def __init__(self, win, center, width, height, label):
        """
        Creates a rectangular button, eg:
        qb = Button(myWin, Point(30,25), 20, 10, 'Quit')
        """

        w, h = width / 2.0, height / 2.0
        x, y = center.getX(), center.getY()
        self.xmax, self.xmin = x + w, x - w
        self.ymax, self.ymin = y + h, y - h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1, p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):

        return self.active and \
               self.xmin <= p.getX() <= self.xmax and \
               self.ymin <= p.getY() <= self.ymax

    def getLabel(self):

        return self.label.getText()

    def activate(self):

        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = 1

    def deactivate(self):

        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = 0
