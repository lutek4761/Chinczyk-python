from field import *
from pawn import Pawn


class Base:
    def __init__(self, x_position, y_position, base_color, base_id):
        self.base_id = base_id
        self.color = base_color
        self.coords = (x_position, y_position)

        # stworzenie i ustawienie pol
        self.fields = [Field(0, 0, base_color, 20) for x in range(4)]
        self.fields[0].set_xy(x_position - 25, y_position - 25)
        self.fields[1].set_xy(x_position + 25, y_position - 25)
        self.fields[2].set_xy(x_position - 25, y_position + 25)
        self.fields[3].set_xy(x_position + 25, y_position + 25)

        # stworzenie i ustawienie pionkow
        self.__pawns = [Pawn(base_id, pawn_id, base_color) for pawn_id in range(4)]
        self.__pawns[0].set_xy(x_position - 25, y_position - 25)
        self.__pawns[1].set_xy(x_position + 25, y_position - 25)
        self.__pawns[2].set_xy(x_position - 25, y_position + 25)
        self.__pawns[3].set_xy(x_position + 25, y_position + 25)

    def tick(self):
        pass

    def render(self):
        pg.draw.circle(Handler.display, self.color, self.coords, 75)
        for field in self.fields:
            field.render()
        for pawn in self.__pawns:
            pawn.render()

    def get_coords(self):
        return self.coords

    def get_pawns(self):
        return self.__pawns
