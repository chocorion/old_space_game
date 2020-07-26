import pygame
from model import *

from controller.controls import keyMap

class Controller:
    """Gère les interactions utilisateurs"""
    def __init__(self, model):
        self._model = model
        pygame.key.set_repeat(1,400)    #Permet la répétition de touche, interval de 200 ms

    def tick(self):
        for event in pygame.event.get():
            if event.type == keyMap["quit"]:
                return False

            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                if event.key == keyMap["shoot"]:
                    self._model.getPlayer().shoot(event.type == pygame.KEYDOWN)

                elif event.key == keyMap["left"]:
                    self._model.getPlayer().update_move("left", event.type == pygame.KEYDOWN)

                elif event.key == keyMap["right"]:
                    self._model.getPlayer().update_move("right", event.type == pygame.KEYDOWN)

                elif event.key == keyMap["up"]:
                    self._model.getPlayer().update_move("up", event.type == pygame.KEYDOWN)

                elif event.key == keyMap["down"]:
                    self._model.getPlayer().update_move("down", event.type == pygame.KEYDOWN)

        return True
