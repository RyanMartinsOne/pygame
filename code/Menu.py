import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WINDOW_WIDTH, COLOR_BLACK, MENU_OPTIONS, COLOR_GRAY


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("assets/background/orig.png")
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer.music.load("assets/sounds/music/time_for_adventure.mp3")
        pygame.mixer.music.play(-1)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(
                "Keep Safe",
                50,
                COLOR_BLACK,
                ((WINDOW_WIDTH / 2), 70)
            )

            for i in range(len(MENU_OPTIONS)):
                self.menu_text(
                    MENU_OPTIONS[i],
                    20,
                    COLOR_GRAY,
                    ((WINDOW_WIDTH / 2), 170 + 25 * i)
                )

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def menu_text(self, text: str, text_size: int, text_color: tuple, text_center_position: tuple):
        text_font: Font = pygame.font.Font("assets/fonts/PixelOperator8.ttf", text_size)
        text_surface: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surface.get_rect(center=text_center_position)
        self.window.blit(source=text_surface, dest=text_rect)
