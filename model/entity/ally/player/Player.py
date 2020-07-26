from .PlayerController import PlayerController

from math import cos, sin


class Player():
    """Class modélisant le joueur"""

    def __init__(self, initialPos=(0, 0)):
        self._controller = PlayerController()

        self._maxSpeed = 5
        self._speed = 0
        self._acceleration = 0.1
        self._pos = initialPos

        self._angularMaxSpeed = 20
        self._angularSpeed = 0
        self._angularAcceleration = 0.2
        self._angle = 90

        self._height = 40
        self._width = 40


    def update_move(self, direction, isKeyPressed):
        self._controller.update_move(direction, isKeyPressed)


    def shoot(self, isKeyPressed):
        self._controller.shoot(isKeyPressed)


    def isShooting(self):
        return self._controller.getShoot()


    def move(self):
        """Fonction gérant le mouvement du joueur"""
        axisX, axisY = self._controller.getAxisValue()

        self._updateSpeed(axisY)

        dx = self._speed * cos((self._angle - 90)%360 * 3.14/180)
        dy = self._speed * sin((self._angle - 90)%360 * 3.14/180)

        self._pos = (self._pos[0] + dx, self._pos[1] + dy)

        self._updateAngle(axisX)


    def _updateSpeed(self, axisY):
        if axisY < 0:
            if self._speed + self._acceleration < self._maxSpeed:
                self._speed += self._acceleration

        elif axisY > 0:
            if self._speed > 0:
                if self._speed - self._acceleration > 0:
                    self._speed -= self._acceleration
                else:
                    self._speed = 0
        else:
            if self._speed > 0:
                if self._speed - self._acceleration > 0:
                    self._speed -= self._acceleration/4
                else:
                    self._speed = 0


    def _updateAngle(self, axisX):
        angle_limit = 1 - (self._speed / self._maxSpeed)/3
        if angle_limit < 0.3:
            angle_limit = 0.3


        if axisX < 0:
            if  self._angularSpeed - self._angularAcceleration > -self._angularMaxSpeed:
                self._angularSpeed -= self._angularAcceleration * angle_limit


        elif axisX > 0:
            if self._angularSpeed + self._angularAcceleration < self._angularMaxSpeed:
                self._angularSpeed += self._angularAcceleration * angle_limit
        else:
            if abs(self._angularSpeed) < 0.1:
                self._angularSpeed = 0

            elif self._angularSpeed < 0:
                self._angularSpeed += self._angularAcceleration * angle_limit

            elif self._angularSpeed > 0:
                self._angularSpeed -= self._angularAcceleration * angle_limit

        self._angle = (self._angularSpeed + self._angle)%360


    def getWidth(self):
        return self._width


    def getHeight(self):
        return self._height


    def getAngle(self):
        return self._angle


    def getPosition(self):
        return self._pos