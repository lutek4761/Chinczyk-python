import pygame as pg
from handler import Handler
from pygame import font
from random import randint


class Pawn:
    pg.font.init()
    field_font = font.Font('freesansbold.ttf', 16)
    text = field_font.render("P", False, (0, 0, 0))

    def __init__(self, base_id, pawn_id, pawn_color):
        self.position = -1  # pozycja na sciezce
        self.starting_position = 0
        print(self.starting_position)
        self.p_coord = 0
        self.base_id = base_id
        self.pawn_id = pawn_id
        self.pawn_color = pawn_color
        self.__in_base = True
        self.radius = 25
        self.__is_hovered = False
        self.route = []

    def render(self):
        if self.__is_hovered:
            pg.draw.circle(Handler.display, (255, 128, 14), self.p_coord, self.radius)
        else:
            pg.draw.circle(Handler.display, (0, 0, 0), self.p_coord, self.radius)
        pg.draw.circle(Handler.display, self.pawn_color, self.p_coord, self.radius - 3)
        Handler.display.blit(Pawn.text, (self.p_coord[0]-5, self.p_coord[1]-5))

    def set_xy(self, x, y):
        self.p_coord = (x, y)
        self.starting_position = (x, y)

    def check_if_hovered(self):  # funkcja sprawdza czy myszka najechala na pole
        if ((Handler.mx - self.p_coord[0]) ** 2 + (Handler.my - self.p_coord[1]) ** 2) ** 0.5 < self.radius:
            self.__is_hovered = True
            return True
        else:
            self.__is_hovered = False
            return False

    def move(self):
        self.position += Handler.dice_value
        self.p_coord = self.route[self.position].coord
        self.__in_base = False
        self.__is_hovered = False
        print(self.starting_position)

    def kill(self):
        print(self.starting_position)
        self.p_coord = self.starting_position
        self.__in_base = True
        self.position = -1

    def set_route(self, route):
        self.route = route

    def is_in_base(self):
        return self.__in_base
