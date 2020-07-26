from math import sin, cos

class GameObject():
    def __init__(self, speed, angle, rotation_angle, rotation_speed, pos, width, height):
        self.speed = speed
        self.angle = angle
        self.rotation = rotation_angle
        self.rotation_speed = rotation_speed

        self.pos = pos

        self.width = width
        self.height = height

    def calculate_new_coord(self):
        delta_x = self.speed * cos((self.angle - 90)%360 * 3.14/180)
        delta_y = self.speed * sin((self.angle - 90)%360 * 3.14/180)

        return (self.pos[0] + delta_x, self.pos[1] + delta_y)

    def play(self):
        self.pos = self.calculate_new_coord()
        self.rotation += self.rotation_speed

    def getName(self):
        return "GameObject"