from code.Const import PLAYER_FRAME_RECTS
from code.Entity import Entity
from code.SpriteAnimator import SpriteAnimator

PLAYER_SCALE = 3


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.animator = SpriteAnimator(self.image, PLAYER_FRAME_RECTS, PLAYER_SCALE)
        self.image = self.animator.get_frame()
        self.rect = self.image.get_rect(topleft=position)

    def update(self, dt: float):
        self.animator.update(dt)
        topleft = self.rect.topleft
        self.image = self.animator.get_frame()
        self.rect = self.image.get_rect(topleft=topleft)

    def move(self):
        pass