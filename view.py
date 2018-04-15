from model import *
import pygame

class View:
    def __init__(self, model):
        self.model = model
        self.width = model.map.width
        self.height = model.map.height
        self.win = pygame.display.set_mode((self.width, self.height))

    def tick(self):

        pygame.display.flip()
