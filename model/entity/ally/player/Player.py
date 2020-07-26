from .PlayerController import PlayerController

from math import cos, sin

# Old constants from Model file, TODO Remove it
V_MAX = 5
ANGLE_MAX = 20

class Player():
    """Class modélisant le joueur"""

    def __init__(self):
        self._controller = PlayerController()

        self.V_Max = V_MAX          #Vitesse maximum que peut atteindre le joueur
        self.V = 0                  #Vitesse actuelle du joueur
        self.V_unit = 0.1           #Valeur de l'accélération qui peur être apportée au joueur

        self.angle_max = ANGLE_MAX  #Vitesse angulaire maximum
        self.V_angle = 0            #Vitesse angulaire actuelle du joueur
        self.angle_unit = 0.2      #Valeur de "l'accélération angulaire" du joueur
        self.angle = 90             #Angle atuelle du joueur

        self.pos = (0, 0)           #Position (x, y) du joueur dans le jeu
        self.h = 40
        self.w = 40


    def update_move(self, direction, isKeyPressed):
        self._controller.update_move(direction, isKeyPressed)

    def shoot(self, isKeyPressed):
        self._controller.shoot(isKeyPressed)

    def isShooting(self):
        return self._controller.getShoot()

    def setMove(self, newMovement):
        self.movement = newMovement

    def move(self):
        """Fonction gérant le mouvement du joueur"""
        dx, dy = self._controller.getAxisValue()

        if dy < 0:
            if self.V + self.V_unit < self.V_Max:
                self.V += self.V_unit

        elif dy > 0:
            if self.V > 0:
                if self.V - self.V_unit > 0:
                    self.V -= self.V_unit
                else:
                    self.V = 0
        else:
            if self.V > 0:
                if self.V - self.V_unit > 0:
                    self.V -= self.V_unit/4
                else:
                    self.V = 0

        delta_x = self.V * cos((self.angle - 90)%360 * 3.14/180)
        delta_y = self.V * sin((self.angle - 90)%360 * 3.14/180)

        self.pos = (self.pos[0] + delta_x, self.pos[1] + delta_y)

        angle_limit = 1 - (self.V / self.V_Max)/3
        if angle_limit < 0.3:
            angle_limit = 0.3

        if dx < 0:
            if  self.V_angle - self.angle_unit > -self.angle_max:
                self.V_angle -= self.angle_unit * angle_limit


        elif dx > 0:
            if self.V_angle + self.angle_unit < self.angle_max:
                self.V_angle += self.angle_unit * angle_limit
        else:
            if abs(self.V_angle) < 0.1:
                self.V_angle = 0

            elif self.V_angle < 0:
                self.V_angle += self.angle_unit * angle_limit

            elif self.V_angle > 0:
                self.V_angle -= self.angle_unit * angle_limit

        self.angle = (self.V_angle + self.angle)%360