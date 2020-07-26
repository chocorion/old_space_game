#!/usr/bin/env python3

import pygame
import sys

from model.model import Model
from controller.controller import Controller
from view.view import View
from controller import *

pygame.display.init()
pygame.font.init()

clock = pygame.time.Clock()
FPS = 60


if len(sys.argv) == 2:
    map_file = sys.argv[1]

model = Model()
controller = Controller(model)
view = View(model)


while True:
    dt = clock.tick(FPS)
    if not controller.tick():
        break
    model.tick()
    view.tick()

pygame.quit()
