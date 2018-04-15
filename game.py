#!/usr/bin/python3
import pygame
import sys

from model import *
from view import *
from controller import *

pygame.display.init()
pygame.font.init()
clock = pygame.time.Clock()
FPS = 60



map_file = DEFAULT_MAP
if len(sys.argv) == 2:
    map_file = sys.argv[1]

model = Model()
model.load_map(map_file)
event_manager = Event_Manager()
controller = Controller(event_manager)
view = View(model)


while True:
    dt = clock.tick(FPS)
    if not controller.tick():
        break
    view.tick()
    #print(dt)

pygame.quit()
