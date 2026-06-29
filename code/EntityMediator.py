import pygame

from code.Coin import Coin
from code.Enemy import Enemy
from code.Entity import Entity
from code.Player import Player


class EntityMediator:

    sound_coin = None
    sound_hurt = None

    @staticmethod
    def __load_sounds():
        if EntityMediator.sound_coin is None or EntityMediator.sound_hurt is None:
            EntityMediator.sound_coin = pygame.mixer.Sound('./assets/sounds/effects/coin.wav')
            EntityMediator.sound_hurt = pygame.mixer.Sound('./assets/sounds/effects/hurt.wav')

    @staticmethod
    def __verify_collision_window(e: Entity, entity_list: list):
        if isinstance(e, (Enemy, Coin)):
            if e.rect.right < 0:
                entity_list.remove(e)

    @staticmethod
    def verify_collisions(entity_list: list[Entity]):
        EntityMediator.__load_sounds()

        players = [p for p in entity_list if isinstance(p, Player)]
        enemies = [e for e in entity_list if isinstance(e, Enemy)]
        coins   = [c for c in entity_list if isinstance(c, Coin)]

        for e in enemies:
            EntityMediator.__verify_collision_window(e, entity_list)
        for c in coins:
            EntityMediator.__verify_collision_window(c, entity_list)

        collected_coins = 0

        for p in players:
            for e in enemies:
                if p.rect.colliderect(e.rect):
                    offset = (e.rect.left - p.rect.left, e.rect.top - p.rect.top)
                    if p.mask.overlap(e.mask, offset):
                        EntityMediator.sound_hurt.play()

            for c in coins:
                if p.rect.colliderect(c.rect):
                    offset = (c.rect.left - p.rect.left, c.rect.top - p.rect.top)
                    if p.mask.overlap(c.mask, offset):
                        entity_list.remove(c)
                        EntityMediator.sound_coin.play()
                        collected_coins += 1

        return collected_coins