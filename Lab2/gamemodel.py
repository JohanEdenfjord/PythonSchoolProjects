from math import sin, cos, radians
import random


class Game:

    def __init__(self, cannonSize, ballSize):
        self.cannonSize = cannonSize
        self.ballSize = ballSize
        p1 = Player("blue", -90, self)
        p2 = Player("red", 90, self)
        self.players = [p1, p2]
        self.currentPlayer = 0
        self.otherPlayer = 1
        self.wind = random.uniform(-10, 10)

    def getPlayers(self):
        return self.players

    def getCannonSize(self):
        return self.cannonSize

    def getBallSize(self):
        return self.ballSize

    def getCurrentPlayer(self):
        return self.players[self.currentPlayer]

    def getOtherPlayer(self):
        return self.players[self.otherPlayer]

    def getCurrentPlayerNumber(self):
        return self.currentPlayer

    def nextPlayer(self):
        currentPlayer = self.currentPlayer
        self.currentPlayer = self.otherPlayer
        self.otherPlayer = currentPlayer

    def setCurrentWind(self, wind):
        self.wind = wind

    def getCurrentWind(self):
        return self.wind

    def newRound(self):
        # self.nextPlayer()
        self.setCurrentWind(random.uniform(-10, 10))


class Player:

    def __init__(self, col, position, game):
        self.color = col
        self.position = position
        self.game = game
        self.score = 0
        self.angle = 45
        self.velocity = 0

    def fire(self, angle, velocity):
        if self.game.getCurrentPlayerNumber() == 1:
            proj = Projectile(180 - angle, velocity, self.game.getCurrentWind(), self.getX(),
                              self.game.getCannonSize() / 2, -110, 110)
        else:
            proj = Projectile(angle, velocity, self.game.getCurrentWind(), self.getX(), self.game.getCannonSize() / 2,
                              -110, 110)

        self.angle = angle
        self.velocity = velocity

        return proj

    def projectileDistance(self, proj):
        center = self.getX()
        cannonSize = self.game.getCannonSize() / 2
        lPosCannon = center - cannonSize
        rPosCannon = center + cannonSize
        projectileCenter = proj.getX()
        projectileSize = self.game.getBallSize()

        leftPosition = projectileCenter - projectileSize
        rightPosition = projectileCenter + projectileSize

        if leftPosition > rPosCannon:
            return -rPosCannon + leftPosition
        elif rightPosition < lPosCannon:
            return -lPosCannon + rightPosition
        else:
            return 0

    def getAim(self):
        return self.angle, self.velocity

    def getScore(self):
        return self.score

    def increaseScore(self):
        self.score += 1

    def getColor(self):
        return self.color

    def getX(self):
        return self.position


class Projectile:

    def __init__(self, angle, velocity, wind, xPos, yPos, xLower, xUpper):
        self.yPos = yPos
        self.xPos = xPos
        self.xLower = xLower
        self.xUpper = xUpper
        theta = radians(angle)
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)
        self.wind = wind

    """ 
        Advance time by a given number of seconds
        (typically, time is less than a second, 
         for large values the projectile may move erratically)
    """

    def update(self, time):
        # Compute new velocity based on acceleration from gravity/wind
        yvel1 = self.yvel - 9.8 * time
        xvel1 = self.xvel + self.wind * time

        # Move based on the average velocity in the time period 
        self.xPos = self.xPos + time * (self.xvel + xvel1) / 2.0
        self.yPos = self.yPos + time * (self.yvel + yvel1) / 2.0

        # make sure yPos >= 0
        self.yPos = max(self.yPos, 0)

        # Make sure xLower <= xPos <= mUpper   
        self.xPos = max(self.xPos, self.xLower)
        self.xPos = min(self.xPos, self.xUpper)

        # Update velocities
        self.yvel = yvel1
        self.xvel = xvel1

    """ A projectile is moving as long as it has not hit the ground or moved outside the xLower and xUpper limits """

    def isMoving(self):
        return 0 < self.getY() and self.xLower < self.getX() < self.xUpper

    def getX(self):
        return self.xPos

    """ The current y-position (height) of the projectile". Should never be below 0. """

    def getY(self):
        return self.yPos
