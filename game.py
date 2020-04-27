import pygame as pg
from board import Board
from player import Player


class Game:
    def __init__(self, players_num):
        self.board = Board()
        self.players = [Player(player_id) for player_id in range(players_num)]  # jeden ze sposobow inicjalizowania tablicy w pythonie, poczytaj o "list comprahension"
        self.current_player = self.players[0]
        self.current_player_id = 0
        self.guard = True  # zmienna potrzebna do mechanizmu by podczas klikniecia gracz zmienil sie raz a nie 60 razy na sekunde

    def render(self):
        self.board.render()

    def tick(self, mouse_clicked):
        self.board.tick()
        if mouse_clicked and self.guard:
            self.switch_to_next_player()
            self.guard = False
        elif not (mouse_clicked or self.guard):
            self.guard = True

    def switch_to_next_player(self):
        self.current_player_id += 1
        if self.current_player_id > len(self.players) - 1:
            self.current_player_id = 0
        self.current_player = self.players[self.current_player_id]
        print("Switched to player {}".format(self.current_player_id))
