from field import Field


class Board:
    def __init__(self):
        self.pawn_color = (255, 25, 25)
        self.pawn_radius = 25
        self.fields = [Field(180, 60, self.pawn_color, self.pawn_radius),
                       Field(100, 60, self.pawn_color, self.pawn_radius)]
        self.route1 = []
        self.route2 = []
        self.route3 = []
        self.route4 = []

    def tick(self):
        for field in self.fields:
            field.tick()

    def render(self):
        for field in self.fields:
            field.render()
