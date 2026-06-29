from code.Const import COIN_FRAME_RECTS, ENTITY_SPEED, COIN_SCALE
from code.Entity import Entity
from code.SpriteAnimator import SpriteAnimator


class Coin(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.animator = SpriteAnimator(self.image, COIN_FRAME_RECTS, COIN_SCALE)
        self.image = self.animator.get_frame()
        self.rect = self.image.get_rect(topleft=position)

    def update(self, dt: float):
        self.animator.update(dt)
        self.set_image(self.animator.get_frame(), self.rect.topleft)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]