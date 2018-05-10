## TODO:
#   * Fonction permettant de faire la rotation d'une image selon un angle donné à utiliser dans render_map


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

        self.win = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)     #Faudra bien penser à gérer la taille :/

        self.sprite = {
            "player": [pygame.image.load(sprite) for sprite in SPRITE_PLAYER]
        }

    def render_map(self):
        """Fonction permettant de dessiner le jeu à l'écran"""
        map = self.model.map

        #Vaut mieux une fonction qui tourne une image celon un certain angle, a faire
        player_surface = self.resize(self.sprite["player"][0], 40, 40)

        old_rect = pygame.Surface.get_rect(player_surface)
        old_center = old_rect.center

        player_surface = pygame.transform.rotate(player_surface, -(self.model.player.angle))
        new_rect = pygame.Surface.get_rect(player_surface)
        new_rect.center = old_center


        self.win.blit(player_surface, new_rect.move(self.model.player.pos))


        #for element in map.array:
        #Faire chaque objet avec de base une fonction de render, qu'on "surchargera" pour les spécificitées

    def resize(self, surface, width, height):
        return pygame.transform.scale(surface, (width, height))

    def tick(self):
        self.width = self.win.get_width()
        self.height = self.win.get_height()
        self.win.fill([0, 0, 0])

        self.render_map()
        pygame.display.flip()
