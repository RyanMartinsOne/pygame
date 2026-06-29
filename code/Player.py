import pygame
from code.Const import PLAYER_FRAME_RECTS, PLAYER_JUMP_FRAME_RECTS, PLAYER_SCALE, JUMP_FORCE, GRAVITY, JUMP_KEYS
from code.Entity import Entity
from code.SpriteAnimator import SpriteAnimator


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        # Run animation
        self.run_animator  = SpriteAnimator(self.image, PLAYER_FRAME_RECTS, PLAYER_SCALE)

        # Jump animation
        jump_sheet = Entity.load_image('PlayerJump')
        self.jump_animator = SpriteAnimator(
            jump_sheet,
            PLAYER_JUMP_FRAME_RECTS,
            PLAYER_SCALE,
            frame_durations=[0.1, 0.2, 0.3, 0.4, 0.3, 0.1]
            #                 0    1    2    3    4    5
        )

        self.animator = self.run_animator
        self.image    = self.animator.get_frame()
        self.rect     = self.image.get_rect(topleft=position)

        # Physics
        self.vel_y      = 0.0
        self.is_jumping = False
        self.ground_y   = position[1]
        self._dt        = 0.0

    def update(self, dt: float):
        self._dt = dt
        self.animator.update(dt)
        self.set_image(self.animator.get_frame(), self.rect.topleft)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        # Start jump
        if any(pressed_keys[k] for k in JUMP_KEYS) and not self.is_jumping:
            self.vel_y = JUMP_FORCE
            self.is_jumping = True
            self.jump_animator.current_frame = 0
            self.jump_animator.timer = 0.0
            self.animator = self.jump_animator

        # Fall animation
        if self.is_jumping:
            self.vel_y    += GRAVITY * self._dt
            self.rect.top += int(self.vel_y * self._dt)

            # Stop if reach the ground
            if self.rect.top >= self.ground_y:
                self.rect.top   = self.ground_y
                self.vel_y      = 0.0
                self.is_jumping = False
                self.animator   = self.run_animator