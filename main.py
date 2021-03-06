import pygame.gfxdraw
from pygame.locals import *
from game import *
from handler import *
import sys
import random
import math

pg.init()
pg.font.init()
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
FPS = 120
delta = 0

game = Game(4)
clock = pg.time.Clock()

while True:
    delta += clock.tick()
    if delta > 1000 / FPS:
        delta -= 1000 / FPS
    else:
        continue
    Handler.event_handler()
    game.tick()
    game.render()
    pg.display.update()
    Handler.display.fill([55, 55, 55])
