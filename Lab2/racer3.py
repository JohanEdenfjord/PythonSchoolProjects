from graphics import *


class Racer:
    def __init__(self):
        self.xVelocity = 0
        self.yVelocity = 0
        self.xPos = 0
        self.yPos = 0
        self.speedLimit = 10

    def _moveRelative(self, xDiff, yDiff):
        self.xPos += xDiff
        self.yPos += yDiff

    def _moveAbsolute(self, x, y):
        self._moveRelative(x - self.getX(), y - self.getY())

    def accelerate(self, xAcc, yAcc):
        self.xVelocity += xAcc
        self.yVelocity += yAcc
        # speedLimits
        self.yVelocity = min(self.speedLimit, self.yVelocity)
        self.yVelocity = max(-self.speedLimit, self.yVelocity)
        self.xVelocity = min(self.speedLimit, self.xVelocity)
        self.xVelocity = max(-self.speedLimit, self.xVelocity)

    def slowDown(self):
        self.xVelocity *= 0.9
        self.yVelocity *= 0.9

    def drive(self):
        self._moveRelative(self.xVelocity, self.yVelocity)

    def reset(self):
        self._moveAbsolute(0, 0)
        self.xVelocity = 0
        self.yVelocity = 0

    def getX(self):
        return self.xPos

    def getY(self):
        return self.yPos

    def checkBorders(self):
        if self.getX() > 400 or self.getX() < -400:
            self._moveAbsolute(-self.getX(), self.getY())
        elif self.getY() > 300 or self.getY() < -300:
            self._moveAbsolute(self.getX(), -self.getY())


"""  Wraps around a Racer, creating graphical elements for it    
this class delegates all method calls to the underlying Racer-object    
just doing what's needed to make the car show up correctly in    
the graphical window"""


class RacerGraphic:
    def __init__(self, racer, win):
        self.win = win
        self.model = racer
        self.circle = Circle(Point(0, 0), 10)
        self.circle.setFill('blue')
        self.circle.draw(win)
        self.letter = Text(Point(0, 0), "R")
        self.letter.setTextColor('red')
        self.letter.draw(win)

    """    Synchronize the graphics with the current state of the model    """

    def _sync(self):
        # Move the circle and text to wherever the car is
        m = self.model
        c = self.circle
        t = self.letter
        c.move(m.getX() - c.getCenter().getX(), m.getY() - c.getCenter().getY())
        t.move(m.getX() - t.getAnchor().getX(), m.getY() - t.getAnchor().getY())

    def accelerate(self, xacc, yacc):
        # Call the corresponding method in the model
        self.model.accelerate(xacc, yacc)
        # Synchronize the graphics to reflect whatever changes the model made
        self._sync()

    def slowDown(self):
        self.model.slowDown()
        self._sync()

    def drive(self):
        self.model.drive()
        self._sync()

    def reset(self):
        self.model.reset()
        self._sync()

    def checkBorders(self):
        self.model.checkBorders()
        self._sync()
