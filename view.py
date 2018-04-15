from model import *
import pygame

class View:
    def __init__(self, model):
        self.model = model
        self.width = model.map.width
        self.height = model.map.height
        self.win = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)

    def tick(self):
        self.width = self.win.get_width()
        self.height = self.win.get_height()
        
        pygame.display.flip()
