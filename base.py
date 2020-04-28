from field import *


class Base:
    def __init__(self, base_color, x_position, y_position):
        self.color = base_color
        self.coords = (x_position, y_position)
        self.fields = [Field(0, 0, base_color, 20) for x in range(4)]
        self.fields[0].set_xy(x_position - 25, y_position - 25)
        self.fields[1].set_xy(x_position + 25, y_position - 25)
        self.fields[2].set_xy(x_position - 25, y_position + 25)
        self.fields[3].set_xy(x_position + 25, y_position + 25)

    def tick(self):
        pass

    def render(self):
        pg.draw.circle(Handler.display, self.color, self.coords, 75)
        for field in self.fields:
            field.render()

    def get_coords(self):
        return self.coords
