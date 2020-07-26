import sys
from random import randrange

from model.entity.enemy.Asteroid import Asteroid

class Map:
    """Class modélisant la map du jeu"""
    def __init__(self, model):
        self.array = []     #Liste contenant tous les objets du jeu
        self.width = 0
        self.height = 0
        self.model = model

    def load(self, filename):
        """Lecture du fichier passé en argument"""
        player_pos = (0, 0)
        try:
            file = open(filename, "r")

            for row in file.readlines():
                row = row.strip('\n')
                _row = row.split(' ')

                if _row[0] == "width":
                    self.width = int(_row[1])

                elif _row[0] == "height":
                    self.height = int(_row[1])

                elif _row[0] == "player":
                    self.model.player.pos = (int(_row[1]), int(_row[2]))
        except:
            sys.stderr.write("Error in load map, can't open file.\n")
        return player_pos

    def add_random_asteroid(self):
        """self, speed, angle, rotation_angle, rotation_speed, pos, type, width, height"""

        self.add_obj(Asteroid.createRandom())

    def add_obj(self, obj):
        self.array.append(obj)
