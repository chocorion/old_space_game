import sys

DEFAULT_MAP = "maps/map_0.map"
VX_MAX = 20
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
        self.Vx_Max = VX_MAX
        self.Vx = 0
        self.angle_max = ANGLE_MAX
        self.angle = 0
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
        if self.go_right:
            self.angle -= 1
        elif self.go_left:
            self.angle += 1

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
