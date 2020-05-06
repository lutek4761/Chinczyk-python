import pygame as pg
from handler import *
from pygame import font


class Field:
    id = 0  # zmienna statyczna

    def __init__(self, x, y, color, radius):
        self.id = Field.id  # zmienna obiektu (po lewej) przyjmuje wartosc zmiennej statycznej (po prawej)
        self.coord = (x, y)
        self.color = color
        self.radius = radius
        self.pawn_on_this_field = None
        self.__is_hovered = False
        self.field_font = font.Font('freesansbold.ttf', 16)
        self.text = self.field_font.render("{}".format(self.id), False, (0, 0, 0))
        #print("Stworzono pole o id {}".format(Field.id))
        Field.id += 1  # zwiekszenie wartosci zmiennej statycznej o 1
        self.guard = True

    def tick(self):
        if self.check_if_hovered() and Handler.mouse_clicked and self.guard:
            self.show_info()
            self.guard = False
        elif not Handler.mouse_clicked and not self.guard:
            self.guard = True

    def render(self):
        if self.__is_hovered:
            border_color = (50, 255, 50)
        else:
            border_color = (0, 0, 0)
        pg.draw.circle(Handler.display, border_color, self.coord, self.radius)
        pg.draw.circle(Handler.display, self.color, self.coord, self.radius - 2)
        Handler.display.blit(self.text, (self.coord[0] - 8, self.coord[1] - 5))

    def show_info(self):
        print("Info o polu {}".format(self.id))
        if self.pawn_on_this_field is not None:
            print("Board id: {}, \nPawn_id: {}".format(self.pawn_on_this_field.base_id, self.pawn_on_this_field.pawn_id))
        else:
            print("Brak pionkow")

    def set_xy(self, x, y):
        self.coord = (x, y)

    def check_if_hovered(self):  # funkcja sprawdza czy myszka najechala na pole
        if ((Handler.mx - self.coord[0]) ** 2 + (Handler.my - self.coord[1]) ** 2) ** 0.5 < self.radius:
            self.__is_hovered = True
            return True
        else:
            self.__is_hovered = False
            return False

    def set_color(self, field_color):
        self.color = field_color
