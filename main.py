import pygame.gfxdraw
from pygame.locals import *
from game import *
from display import *
import sys
import random
import math

pg.init()
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
FPS = 10
delta = 0
mouse_clicked = False

game = Game(4)
clock = pg.time.Clock()


def event_handler():
    global mouse_clicked
    for event in pg.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pg.quit()
            exit(0)
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_clicked = True
        else:
            mouse_clicked = False


while True:
    delta += clock.tick()
    if delta > 1000 / FPS:
        delta -= 1000 / FPS
    else:
        continue
    event_handler()
    game.tick(mouse_clicked)
    game.render()
    pg.display.update()
    Display.display.fill([55, 55, 55])
