from code.Const import ENEMY_FRAME_RECTS
from code.Entity import Entity
from code.SpriteAnimator import SpriteAnimator

ENEMY_SCALE = 2


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.animator = SpriteAnimator(self.image, ENEMY_FRAME_RECTS, ENEMY_SCALE)
        self.image = self.animator.get_frame()
        self.rect = self.image.get_rect(topleft=position)

    def update(self, dt: float):
        self.animator.update(dt)
        topleft = self.rect.topleft
        self.image = self.animator.get_frame()
        self.rect = self.image.get_rect(topleft=topleft)

    def move(self):
        pass