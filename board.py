from field import Field
from handler import *


class Board:
    def __init__(self):
        self.pawn_color = (255, 25, 25)
        self.pawn_radius = 25
        self.fields = [Field(0, 0, (255, 255, 255), 20) for _ in range(40)]
        self.red_target_fields = [Field(0, 0, (255, 128, 128), 20) for _ in range(4)]
        self.green_target_fields = [Field(0, 0, (128, 255, 128), 20) for _ in range(4)]
        self.blue_target_fields = [Field(0, 0, (128, 128, 255), 20) for _ in range(4)]
        self.yellow_target_fields = [Field(0, 0, (255, 255, 128), 20) for _ in range(4)]
        self.fields[0].set_color((255, 255, 128))
        self.fields[10].set_color((255, 128, 128))
        self.fields[20].set_color((128, 255, 128))
        self.fields[30].set_color((128, 128, 255))
        self.route1 = []
        self.route2 = []
        self.route3 = []
        self.route4 = []

        self.set_fields_position()

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