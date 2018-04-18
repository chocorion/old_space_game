import sys
from math import *

DEFAULT_MAP = "maps/map_0.map"
V_MAX = 5
ANGLE_MAX = 20

class Event_Manager:
    def __init__(self, model):
        self.model = model

    def quit(self):
        return False

    def move_player(self, dir, state):
        self.model.player.update_move(dir, state)
        return True

class Map:
    def __init__(self, model):
        self.array = []
        self.width = 0
        self.height = 0
        self.model = model

    def load(self, filename):
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

class Player():
    def __init__(self):
        self.V_Max = V_MAX
        self.V = 0
        self.V_unit = 0.5

        self.angle_max = ANGLE_MAX
        self.V_angle = 0
        self.angle_unit = 0.2
        self.angle = 90

        self.pos = (0, 0)

        self.go_up = False
        self.go_left = False
        self.go_right = False

    def update_move(self, dir, state):
        if dir == "up":
            self.go_up = state

        elif dir == "left":
            self.go_left = state
            if state:
                self.go_right = False

        elif dir == "right":
            self.go_right = state
            if state:
                self.go_left = False

    def move(self):
        if self.go_up:
            if self.V + self.V_unit < self.V_Max:
                self.V += self.V_unit
        else:
            if self.V > 0:
                if self.V - self.V_unit > 0:
                    self.V -= self.V_unit
                else:
                    self.V = 0

        delta_x = self.V * cos((self.angle)%360 * 3.14/180)
        delta_y = self.V * sin((self.angle)%360 * 3.14/180)
        print(self.angle, delta_x, delta_y)

        self.pos = (self.pos[0] + delta_x, self.pos[1] + delta_y)

        if self.go_left:
            if  self.V_angle - self.angle_unit > -self.angle_max:
                self.V_angle -= self.angle_unit


        elif self.go_right:
            if self.V_angle + self.angle_unit < self.angle_max:
                self.V_angle += self.angle_unit
        else:
            if abs(self.V_angle) < 0.1:
                self.V_angle = 0

            elif self.V_angle < 0:
                self.V_angle += self.angle_unit

            elif self.V_angle > 0:
                self.V_angle -= self.angle_unit

        self.angle = (self.V_angle + self.angle)%360

class Model:
    def __init__(self):
        self.player = Player()
        self.map = Map(self)
        self.map_path = DEFAULT_MAP


    def load_map(self, map_name):
        self.map_path = map_name
        self.map.load(map_name)

    def tick(self):
        self.player.move()
