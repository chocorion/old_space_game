from model import *
import pygame

DEFAULT_WIDTH = 700
DEFAULT_HEIGHT = 1000

SPRITE_PLAYER = ["assets/player/ship_00.png"]


class View:
    """Class définissant la vue"""
    def __init__(self, model):
        self.model = model
        self.width = model.map.width
        self.height = model.map.height

        self.win = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)

        self.sprite = {
            "player": [pygame.image.load(sprite) for sprite in SPRITE_PLAYER]
        }

    def render_map(self):
        map = self.model.map

        player_surface = self.resize(self.sprite["player"][0], 40, 40)

        old_rect = pygame.Surface.get_rect(player_surface)
        old_center = old_rect.center

        player_surface = pygame.transform.rotate(player_surface, -(self.model.player.angle + 90))
        new_rect = pygame.Surface.get_rect(player_surface)
        new_rect.center = old_center


        self.win.blit(player_surface, new_rect.move(self.model.player.pos))


        #for element in map.array:

    def resize(self, surface, width, height):
        return pygame.transform.scale(surface, (width, height))

    def tick(self):
        self.width = self.win.get_width()
        self.height = self.win.get_height()
        self.win.fill([0, 0, 0])

        self.render_map()
        pygame.display.flip()
