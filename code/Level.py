import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import COLOR_BLACK, WINDOW_WIDTH, EVENT_ENEMY
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, coins):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []

        pygame.time.set_timer(EVENT_ENEMY, 2500)

        self.font_hud = pygame.font.Font("assets/fonts/PixelOperator8.ttf", 14)

        # background
        self.entity_list.extend(EntityFactory.get_entity(f"{self.name}Bg"))

        # player
        self.entity_list.append(EntityFactory.get_entity("Player"))

        # enemy
        self.entity_list.append(EntityFactory.get_entity("Enemy"))

        self.coins = coins

    def run(self):
        pygame.mixer.music.load(f"./assets/sounds/music/{self.name}.mp3")
        pygame.mixer.music.play(-1)
        clock = pygame.time.Clock()

        while True:
            # Delta time para manter animação num ritmo constante
            dt = clock.tick(60) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == EVENT_ENEMY:
                    self.entity_list.append(EntityFactory.get_entity('Enemy'))

            for entity in self.entity_list:
                if hasattr(entity, "update"):
                    entity.update(dt)

                entity.move()
                self.window.blit(source=entity.image, dest=entity.rect)

            self.level_text(f"Moedas: {self.coins}", COLOR_BLACK, (5, 9))
            self.level_text(
                f"fps: {clock.get_fps():.0f}", COLOR_BLACK, (WINDOW_WIDTH - 77, 5)
            )
            self.level_text(f"entidades: {len(self.entity_list)}", COLOR_BLACK, (WINDOW_WIDTH - 150, 50))

            pygame.display.flip()

    def level_text(self, text: str, text_color: tuple, text_position: tuple):
        text_surface = self.font_hud.render(text, True, text_color).convert_alpha()
        text_rect = text_surface.get_rect(left=text_position[0], top=text_position[1])
        self.window.blit(source=text_surface, dest=text_rect)