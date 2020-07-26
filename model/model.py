import sys
from math import *
from random import randrange
from model.entity.ally.player import Player
from model.entity.ally.Projectile import Projectile
from model.Map import Map

DEFAULT_MAP = "maps/map_0.map"
V_MAX = 5
ANGLE_MAX = 20

def check_collision(x1, y1, h1, w1, x2, y2, h2, w2):
    return x1 < x2 + w2 and x1 + w1 > x2 and y1 < y2 + h2 and y1 + h1 > y2



class Model:
    """Model du jeu"""
    def __init__(self, map_path=DEFAULT_MAP):
        self.player = Player()
        self.map = Map(self)

        self.map_path = map_path
        self.load_map()

    def load_map(self):
        self.map.load(self.map_path)

    def check_player_collision(self):
        for element in self.map.array:
            if check_collision(
                self.player.pos[0], self.player.pos[1], self.player.w, self.player.h,
                element.pos[0], element.pos[1], element.width, element.height):
                break


    def tick(self):
        self.player.move()
        for element in self.map.array:
            element.play()
        self.check_player_collision()
        if randrange(0, 100)%26 == 0:
            self.map.add_random_asteroid()

        if self.player.isShooting():
            projectile = Projectile(10, self.player.angle, 0, 0, self.player.pos, 20, 40)
            self.map.add_obj(projectile)

    def getPlayer(self):
        return self.player