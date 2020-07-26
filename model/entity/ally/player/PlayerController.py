from collections import namedtuple


class PlayerController:
    def __init__(self):
        self._directions = {
            'up': {
                "state": False,
                "opposite": 'down',
                "axisValue": (0, -1)
            },
            'down': {
                "state": False,
                "opposite": 'up',
                "axisValue": (0, 1)
            },
            'left': {
                "state": False,
                "opposite": 'right',
                "axisValue": (-1, 0)
            },
            'right': {
                "state": False,
                "opposite": 'left',
                "axisValue": (1, 0)
            }
        }

        self._isShooting = False

        
    def update_move(self, direction, isKeyPressed):
        currentDirection = self._directions[direction]
        currentDirection["state"] = isKeyPressed

        if isKeyPressed:
            self._directions[currentDirection["opposite"]]["state"] = False

        
    def getAxisValue(self):
        xAxis = yAxis = 0

        for d in self._directions.values():
            if d["state"]:
                x, y = d["axisValue"]

                xAxis += x
                yAxis += y
        
        return (xAxis, yAxis)


    def shoot(self, isKeyPressed):
        self._isShooting = isKeyPressed

    
    def getShoot(self):
        return self._isShooting