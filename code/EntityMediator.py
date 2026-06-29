import pygame

from code.Enemy import Enemy
from code.Entity import Entity
from code.Player import Player


class EntityMediator:

    @staticmethod
    def __verify_collision_window(e:Entity, entity_list: list):
        if isinstance(e, Enemy):
            if e.rect.right < 0:
                entity_list.remove(e)


    @staticmethod
    def verify_collisions(entity_list: list[Entity]):
        player = [p for p in entity_list if isinstance(p, Player)]
        enemies = [e for e in entity_list if isinstance(e, Enemy)]

        for p in player:
            for e in enemies:
                EntityMediator.__verify_collision_window(e, entity_list)
                if p.rect.colliderect(e.rect):
                    offset = (e.rect.left - p.rect.left,
                              e.rect.top - p.rect.top)
                    if p.mask.overlap(e.mask, offset):
                        pygame.mixer.music.load('./assets/sounds/effects/hurt.mp3')
                        pygame.mixer.music.play()
