from model.entity.GameObject import GameObject
from random import randrange

class Asteroid(GameObject):
    def __init__(self, speed, angle, rotation_angle, rotation_speed, pos, width, height):
        super().__init__(speed, angle, rotation_angle, rotation_speed, pos, width, height)

    @staticmethod
    def createRandom():
        speed = randrange(1, 10)
        angle = randrange(0, 360)
        rotation_angle = randrange(0, 360)
        rotation_speed = randrange(0, 6)
        pos = (randrange(0, 700), randrange(0, 1000))
        width = height = randrange(10, 50)

        return Asteroid(speed, angle, rotation_angle, rotation_speed, pos, width, height)

    def getName(self):
        return "asteroid"