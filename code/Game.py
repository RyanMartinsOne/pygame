import pygame

from code.Const import WINDOW_WIDTH, WINDOW_HEIGHT
from code.Menu import Menu


class Game:
    def __init__(self):
        print("Game started")
        pygame.init()
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        print("Setup end")

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass
