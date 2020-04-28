from base import *
from pygame import font


class Player:
    def __init__(self, id):
        self.field_font = font.Font('freesansbold.ttf', 16)
        self.text = self.field_font.render("Player #{}".format(id), False, (255, 255, 255))
        self.id = id
        if id == 0:
            self.base = Base((0, 255, 0), 100, 100)
        if id == 1:
            self.base = Base((0, 0, 255), 600, 100)
        if id == 2:
            self.base = Base((255, 255, 0), 600, 600)
        if id == 3:
            self.base = Base((255, 0, 0), 100, 600)

    def tick(self):
        self.base.tick()

    def render(self):
        self.base.render()
        Handler.display.blit(self.text, (self.base.get_coords()[0] - 40, self.base.get_coords()[1] + 85))
