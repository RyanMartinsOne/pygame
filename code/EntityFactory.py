import random

from code.Background import Background
from code.Const import WINDOW_WIDTH
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position: tuple=(0,0)):
        match entity_name:
            case "Level01Bg":
                list_bg = [
                    Background(f"Level01Bg{i}", pos)
                    for i in range(5)
                    # Create 2 Backgrounds, one at the start and other in the end
                    for pos in [position, (WINDOW_WIDTH, 0)]
                ]
                return list_bg

            case "Level02Bg":
                list_bg = [
                    Background(f"Level02Bg{i}", pos)
                    for i in range(4)
                    # Create 2 Backgrounds, one at the start and other in the end
                    for pos in [position, (WINDOW_WIDTH, 0)]
                ]
                return list_bg

            case "Level03Bg":
                list_bg = [
                    Background(f"Level03Bg{i}", pos)
                    for i in range(4)
                    # Create 2 Backgrounds, one at the start and other in the end
                    for pos in [position, (WINDOW_WIDTH, 0)]
                ]
                return list_bg

            case "Player":
                return Player("Player", (30, 240))

            case "Enemy":
                return Enemy("Enemy", (WINDOW_WIDTH + random.randint(80, 200), 250))

        return None