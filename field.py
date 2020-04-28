import pygame as pg
from handler import *


class Field:
    id = 0  # zmienna statyczna

    def __init__(self, x, y, color, radius):
        self.id = Field.id  # zmienna obiektu (po lewej) przyjmuje wartosc zmiennej statycznej (po prawej)
        self.coord = (x, y)
        self.color = color
        self.radius = radius
        self.is_hovered = False;
        print("Stworzono pole o id {}".format(Field.id))
        Field.id += 1  # zwiekszenie wartosci zmiennej statycznej o 1

    def tick(self):
        self.check_if_hovered()

    def render(self):
        if self.is_hovered:
            border_color = (50, 255, 50)
        else:
            border_color = (0, 0, 0)
        pg.draw.circle(Handler.display, border_color, self.coord, self.radius)
        pg.draw.circle(Handler.display, self.color, self.coord, self.radius - 2)

    def set_xy(self, x, y):
        self.coord = (x, y)

    def check_if_hovered(self):  # funkcja sprawdza czy myszka najechala na pole
        if ((Handler.mx - self.coord[0])**2 + (Handler.my - self.coord[1])**2)**0.5 < self.radius:
            self.is_hovered = True
            return True
        else:
            self.is_hovered = False
            return False

    def set_color(self, field_color):
        self.color = field_color

