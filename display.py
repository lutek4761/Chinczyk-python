from game import *


class Display:
    display = pg.display.set_mode((800, 600))
    # statyczne pole klasy, umozliwia latwy dostep do tej zmiennej wszystkim innym klasom, bo starczy wywolac
    # Display.display i mamy oryginalna zmienna, na ktorej dzialamy.
