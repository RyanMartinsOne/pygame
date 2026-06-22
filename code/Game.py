import pygame

from code.Menu import Menu


class Game:
    def __init__(self):
        print("Game started")
        pygame.init()
        self.window = pygame.display.set_mode((800, 600))
        print("Setup end")

    def run(self):

        menu = Menu(self.window)
        menu.run()
        pass
    