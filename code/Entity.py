from abc import ABC, abstractmethod

import pygame.image


class Entity(ABC):
    def __init__(self, name:str, position:tuple):
        self.name = name
        self.image = Entity.load_image(name)
        self.rect = self.image.get_rect(left=position[0], top=position[1])
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 0

    @staticmethod
    def load_image(name: str) -> pygame.Surface:
        return pygame.image.load(f'./assets/images/{name}.png').convert_alpha()

    def set_image(self, surface:pygame.Surface, topleft:tuple):
        self.image = surface
        self.rect = self.image.get_rect(topleft=topleft)
        self.mask = pygame.mask.from_surface(self.image)

    @abstractmethod
    def move(self):
        pass