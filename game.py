#!/usr/bin/python3
import pygame
import sys
from model import *
from view import *

pygame.display.init()
clock = pygame.time.Clock()
FPS = 60

map_file = DEFAULT_MAP
if len(sys.argv) == 2:
    map_file = sys.argv[1]

model = Model()
model.load_map(map_file)
view = View(model)


while True:
    dt = clock.tick(FPS)
    #print(dt)

pygame.quit()
