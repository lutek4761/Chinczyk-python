from random import randint
import pygame as pg
from handler import Handler


class Dice:
    def __init__(self, x, y):
        self.value = randint(1, 6)
        self.x_pos = x
        self.y_pos = y
        self.default_pos = (x, y)
        self.y_offset = 0
        Handler.dice_value = self.value
        self.__is_hovered = False

    def roll(self):
        self.value = randint(1, 6)
        Handler.dice_value = self.value

    def tick(self):
        pass

    def set_default_position(self):
        self.x_pos = self.default_pos[0]
        self.y_pos = self.default_pos[1]

    def check_if_hovered(self):  # funkcja sprawdza czy myszka najechala na pole
        if self.x_pos < Handler.mx < self.x_pos + 50 and self.y_pos < Handler.my < self.y_pos + 50:
            self.__is_hovered = True
            return True
        else:
            self.__is_hovered = False
            return False

    def render(self):
        x = self.x_pos
        y = self.y_pos
        if self.__is_hovered:
            pg.draw.rect(Handler.display, (255, 0, 0), (x, y, 50, 50))
        else:
            pg.draw.rect(Handler.display, (0, 0, 0), (x, y, 50, 50))
        pg.draw.rect(Handler.display, (255, 255, 255), (x + 5, y + 5, 40, 40))
        if self.value == 1:
            pg.draw.circle(Handler.display, (0, 0, 0), (x + 25, y + 25), 5)
        if self.value == 2:
            pg.draw.circle(Handler.display, (0, 0, 0), (x + 20, y + 20), 5)
            pg.draw.circle(Handler.display, (0, 0, 0), (x + 30, y + 30), 5)
        if self.value == 3:
            pg.draw.circle(Handler.display, (0, 0, 0), (x + 15, y + 15), 5)
            pg.draw.circle(Handler.display, (0, 0, 0), (x + 25, y + 25), 5)
            pg.draw.circle(Handler.display, (0, 0, 0), (x + 35, y + 35), 5)
        if self.value == 4:
            pg.draw.circle(Handler.display, (0, 0, 0), (x + 15, y + 15), 5)
            pg.draw.circle(Handler.display, (0, 0, 0), (x + 15, y + 35), 5)
            pg.draw.circle(Handler.display, (0, 0, 0), (x + 35, y + 15), 5)
            pg.draw.circle(Handler.display, (0, 0, 0), (x + 35, y + 35), 5)
        if self.value == 5:
            pg.draw.circle(Handler.display, (0, 0, 0), (x + 25, y + 25), 5)
            pg.draw.circle(Handler.display, (0, 0, 0), (x + 15, y + 15), 5)
            pg.draw.circle(Handler.display, (0, 0, 0), (x + 15, y + 35), 5)
            pg.draw.circle(Handler.display, (0, 0, 0), (x + 35, y + 15), 5)
            pg.draw.circle(Handler.display, (0, 0, 0), (x + 35, y + 35), 5)
        if self.value == 6:
            pg.draw.circle(Handler.display, (0, 0, 0), (x + 15, y + 15), 5)
            pg.draw.circle(Handler.display, (0, 0, 0), (x + 15, y + 25), 5)
            pg.draw.circle(Handler.display, (0, 0, 0), (x + 15, y + 35), 5)
            pg.draw.circle(Handler.display, (0, 0, 0), (x + 35, y + 15), 5)
            pg.draw.circle(Handler.display, (0, 0, 0), (x + 35, y + 25), 5)
            pg.draw.circle(Handler.display, (0, 0, 0), (x + 35, y + 35), 5)
