from model.entity.GameObject import GameObject

class Projectile(GameObject):
    def __init__(self, speed, angle, rotation_angle, rotation_speed, pos, width, height):
        super().__init__(speed, angle, rotation_angle, rotation_speed, pos, width, height)

    def getName(self):
        return "shoot"