from field import Field
from handler import *


class Board:
    def __init__(self):
        self.pawn_color = (255, 25, 25)
        self.pawn_radius = 25

        #stworzenie wszystkich pol (poza polami docelowymi graczy)
        self.fields = [Field(0, 0, (255, 255, 255), 20) for _ in range(40)]

        #stworzenie pol docelowych dla graczy
        self.red_target_fields = [Field(0, 0, (255, 128, 128), 20) for _ in range(4)]
        self.green_target_fields = [Field(0, 0, (128, 255, 128), 20) for _ in range(4)]
        self.blue_target_fields = [Field(0, 0, (128, 128, 255), 20) for _ in range(4)]
        self.yellow_target_fields = [Field(0, 0, (255, 255, 128), 20) for _ in range(4)]

        #nadanie specjalnego koloru dla startowych pozycji
        self.fields[0].set_color((255, 255, 128))
        self.fields[10].set_color((255, 128, 128))
        self.fields[20].set_color((128, 255, 128))
        self.fields[30].set_color((128, 128, 255))

        #nadanie odpowiednich pozycji dla wszystkich pol
        self.set_fields_position()

        #stworzenie indywidualnych sciezek dla graczy
        self.routes = self.create_routes()  # {green, blue, yellow, red}

    def tick(self):
        for field in self.fields:
            field.tick()

    def render(self):
        for field in self.fields:
            field.render()
        for i in range(len(self.red_target_fields)):
            self.red_target_fields[i].render()
            self.green_target_fields[i].render()
            self.blue_target_fields[i].render()
            self.yellow_target_fields[i].render()

    def create_routes(self):
        yellow_route = [self.fields[x] for x in range(0, 40)]
        for x in self.yellow_target_fields:
            yellow_route.append(x)
        blue_route = [self.fields[x] for x in range(-10, 30)]
        for x in self.blue_target_fields:
            blue_route.append(x)
        green_route = [self.fields[x] for x in range(-20, 20)]
        for x in self.green_target_fields:
            green_route.append(x)
        red_route = [self.fields[x] for x in range(-30, 10)]
        for x in self.red_target_fields:
            red_route.append(x)
        return [green_route, blue_route, yellow_route, red_route]

    def set_fields_position(self):
        self.fields[0].set_xy(600, 400)
        self.fields[1].set_xy(550, 400)
        self.fields[2].set_xy(500, 400)
        self.fields[3].set_xy(450, 400)
        self.fields[4].set_xy(400, 400)
        self.fields[5].set_xy(400, 450)
        self.fields[6].set_xy(400, 500)
        self.fields[7].set_xy(400, 550)
        self.fields[8].set_xy(400, 600)
        self.fields[9].set_xy(350, 600)
        self.fields[10].set_xy(300, 600)
        self.fields[11].set_xy(300, 550)
        self.fields[12].set_xy(300, 500)
        self.fields[13].set_xy(300, 450)
        self.fields[14].set_xy(300, 400)
        self.fields[15].set_xy(250, 400)
        self.fields[16].set_xy(200, 400)
        self.fields[17].set_xy(150, 400)
        self.fields[18].set_xy(100, 400)
        self.fields[19].set_xy(100, 350)
        self.fields[20].set_xy(100, 300)
        self.fields[21].set_xy(150, 300)
        self.fields[22].set_xy(200, 300)
        self.fields[23].set_xy(250, 300)
        self.fields[24].set_xy(300, 300)
        self.fields[25].set_xy(300, 250)
        self.fields[26].set_xy(300, 200)
        self.fields[27].set_xy(300, 150)
        self.fields[28].set_xy(300, 100)
        self.fields[29].set_xy(350, 100)
        self.fields[30].set_xy(400, 100)
        self.fields[31].set_xy(400, 150)
        self.fields[32].set_xy(400, 200)
        self.fields[33].set_xy(400, 250)
        self.fields[34].set_xy(400, 300)
        self.fields[35].set_xy(450, 300)
        self.fields[36].set_xy(500, 300)
        self.fields[37].set_xy(550, 300)
        self.fields[38].set_xy(600, 300)
        self.fields[39].set_xy(600, 350)

        self.red_target_fields[0].set_xy(350, 550)
        self.red_target_fields[1].set_xy(350, 500)
        self.red_target_fields[2].set_xy(350, 450)
        self.red_target_fields[3].set_xy(350, 400)

        self.green_target_fields[0].set_xy(150, 350)
        self.green_target_fields[1].set_xy(200, 350)
        self.green_target_fields[2].set_xy(250, 350)
        self.green_target_fields[3].set_xy(300, 350)

        self.blue_target_fields[0].set_xy(350, 150)
        self.blue_target_fields[1].set_xy(350, 200)
        self.blue_target_fields[2].set_xy(350, 250)
        self.blue_target_fields[3].set_xy(350, 300)

        self.yellow_target_fields[0].set_xy(550, 350)
        self.yellow_target_fields[1].set_xy(500, 350)
        self.yellow_target_fields[2].set_xy(450, 350)
        self.yellow_target_fields[3].set_xy(400, 350)