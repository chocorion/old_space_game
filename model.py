import sys

DEFAULT_MAP = "maps/map_0.map"

class Event_Manager:
    def __init__(self, model):
        self.model = model

    def qui():
        return False

class Map:
    def __init__(self):
        self.array = []
        self.width = 0
        self.height = 0
        self.player_pos = (0, 0)

    def load(self, filename):
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
                    self.player_pos = (int(_row[1]), int(_row[2]))
        except:
            sys.stderr.write("Error in load map, can't open file.\n")

class Model:
    def __init__(self):
        self.map = Map()
        self.map_path = DEFAULT_MAP

    def load_map(self, map_name):
        self.map_path = map_name
        self.map.load(map_name)
