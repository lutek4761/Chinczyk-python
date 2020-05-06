from base import *
from pygame import font
from pawn import Pawn
from dice import Dice


class Player:

    def __init__(self, id, route):
        self.field_font = font.Font('freesansbold.ttf', 16)
        self.text = self.field_font.render("Player #{}".format(id), False, (255, 255, 255))
        self.id = id
        self.route = route
        self.roll_attempts = 0
        if id == 0:
            self.base = Base(100, 100, (0, 255, 0), id)
            self.dice = Dice(175, 25)
        if id == 1:
            self.base = Base(600, 100, (0, 0, 255), id)
            self.dice = Dice(675, 25)
        if id == 2:
            self.base = Base(600, 600, (255, 255, 0), id)
            self.dice = Dice(675, 525)
        if id == 3:
            self.base = Base(100, 600, (255, 0, 0), id)
            self.dice = Dice(175, 525)

        self.__pawns = self.base.get_pawns()
        self.assign_route_to_pawns()

    def set_route(self, route):
        self.route = route

    def tick(self):
        if self.has_all_pawns_in_base() and self.dice.check_if_hovered() and Handler.mouse_clicked \
                and Handler.dice_value != 6 and self.roll_attempts < 3:
            self.dice.roll()
            self.roll_attempts += 1
            self.dice.y_pos += 50
            if self.roll_attempts == 3:
                Handler.player_moved = True
                self.dice.y_pos -= 150
                self.roll_attempts = 0
        self.base.tick()
        for pawn in self.__pawns:
            if pawn.check_if_hovered() and Handler.mouse_clicked and self.can_move_pawn(pawn):
                if pawn.is_in_base() and Handler.dice_value == 6:
                    Handler.dice_value = 1
                    self.handle_movement_and_killing(pawn)
                    self.dice.roll()
                    self.roll_attempts += 1
                    self.dice.y_pos += 50
                elif not pawn.is_in_base() and Handler.dice_value != 6:
                    self.handle_movement_and_killing(pawn)
                    Handler.player_moved = True
                    self.roll_attempts = 0
                    self.dice.set_default_position()
                elif not pawn.is_in_base() and Handler.dice_value == 6:
                    self.handle_movement_and_killing(pawn)
                    self.dice.roll()
                    self.roll_attempts += 1
                    self.dice.y_pos += 50
                if self.roll_attempts == 3:
                    Handler.player_moved = True
                    self.dice.set_default_position()
                    self.roll_attempts = 0
        if self.cant_perform_an_action() and self.dice.check_if_hovered() and Handler.mouse_clicked:
            Handler.player_moved = True

    def cant_perform_an_action(self):
        for pawn in self.__pawns:
            if self.can_move_pawn(pawn):
                return False
            if pawn.is_in_base() and Handler.dice_value == 6:
                return False
        return True

    @staticmethod
    def check_for_kills(field):
        if field.pawn_on_this_field is not None:
            field.pawn_on_this_field.kill()

    def can_move_pawn(self, pawn):
        if pawn.is_in_base() and Handler.dice_value != 6:
            return False
        if pawn.position + Handler.dice_value > len(self.route) - 1:  # jesli wyjdzie poza plansze
            return False
        if self.route[
            pawn.position + Handler.dice_value].pawn_on_this_field is not None:  # jesli pole, na ktore idzie jest zajete
            if self.route[pawn.position + Handler.dice_value].pawn_on_this_field.base_id == pawn.base_id:
                return False
        return True

    def handle_movement_and_killing(self, pawn):
        self.route[pawn.position].pawn_on_this_field = None
        pawn.move()
        self.check_for_kills(self.route[pawn.position])
        self.route[pawn.position].pawn_on_this_field = pawn

    def render(self):
        self.base.render()
        Handler.display.blit(self.text, (self.base.get_coords()[0] - 40, self.base.get_coords()[1] + 85))

    def assign_route_to_pawns(self):
        for pawn in self.__pawns:
            pawn.set_route(self.route)

    def has_all_pawns_in_base(self):
        for pawn in self.__pawns:
            if not pawn.is_in_base():
                return False
        return True
