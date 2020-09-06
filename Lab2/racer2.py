from graphics import *


class racer:
    def __init__(self, win, speedLimit):
        self.circle = Circle(Point(0, 0), 10)
        self.circle.setFill('red')
        self.circle.draw(win)

        self.letter = Text(Point(0, 0), 'R')
        self.letter.setTextColor('white')
        self.letter.draw(win)

        self.xVelocity = 0
        self.yVelocity = 0

        self.speedLimit = speedLimit

    def accelerate(self, xVel, yVel):
        self.xVelocity += xVel
        self.yVelocity += yVel

        # tvingar hastighetsbegränsning
        self.xVelocity = min(self.speedLimit, self.xVelocity)
        self.xVelocity = max(-self.speedLimit, self.xVelocity)
        self.yVelocity = min(self.speedLimit, self.yVelocity)
        self.yVelocity = max(-self.speedLimit, self.yVelocity)

    def slowDown(self):
        self.xVelocity *= 0.85
        self.yVelocity *= 0.85

    def drive(self):
        self._moveRelative(self.xVelocity, self.yVelocity)

    def getX(self):
        return self.circle.getCenter().getX()

    def getY(self):
        return self.circle.getCenter().getY()

    def reset(self):
        self._moveAbsolute(0,0)
        self.xVelocity = 0
        self.yVelocity = 0

    def _moveAbsolute(self, x, y):
        self._moveRelative(x-self.getX(), y-self.getY())

    def _moveRelative(self, xDiff, yDiff):
        self.circle.move(xDiff, yDiff)
        self.letter.move(xDiff, yDiff)

    def checkBorders(self):
        pass
