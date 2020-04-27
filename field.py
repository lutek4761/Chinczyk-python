import pygame as pg
from display import *


class Field:
    def __init__(self, x, y, color, radius):
        self.coord = (x, y)
        self.color = color
        self.radius = radius

    def tick(self):
        pass

    def render(self):
        pg.draw.circle(Display.display, (0, 0, 0), self.coord, self.radius)
        pg.draw.circle(Display.display, self.color, self.coord, self.radius - 3)
