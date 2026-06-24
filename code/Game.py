import pygame

from code.Level import Level
from code.Const import WINDOW_WIDTH, WINDOW_HEIGHT
from code.Menu import Menu


class Game:
    def __init__(self):
        print("Game started")
        pygame.init()
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        print("Setup end")

    def run(self):
        menu = Menu(self.window)

        while True:
            menu_return = menu.run()

            match menu_return:
                case 'NEW GAME':
                    level = Level(self.window, 'Level01')
                    level_return = level.run()
                case 'SCORE':
                    print("Exibindo pontuações...")
                case 'HELP':
                    print("Exibindo ajuda...")
                case 'QUIT':
                    pygame.quit()
                    quit()
