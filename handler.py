from game import *
from pygame.locals import *
import pygame as pg


class Handler:
    display = pg.display.set_mode((800, 800))
    mx, my = pg.mouse.get_pos()
    mouse_clicked = False

    @staticmethod
    def event_handler():
        Handler.mx, Handler.my = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pg.quit()
                exit(0)
            if event.type == pg.MOUSEBUTTONDOWN:
                Handler.mouse_clicked = True
            else:
                Handler.mouse_clicked = False
    # statyczne pole klasy, umozliwia latwy dostep do tej zmiennej wszystkim innym klasom, bo starczy wywolac
    # Handler.display i mamy oryginalna zmienna, na ktorej dzialamy.
