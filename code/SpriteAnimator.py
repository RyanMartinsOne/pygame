import pygame

ANIMATION_SPEED = 0.1  # segundos por frame


class SpriteAnimator:
    def __init__(self, spritesheet: pygame.Surface, frame_rects: list, scale: int = 1):
        self.frames = self._slice_and_scale(spritesheet, frame_rects, scale)
        self.current_frame = 0
        self.timer = 0.0

    def _slice_and_scale(self, spritesheet, frame_rects, scale) -> list:
        frames = []
        for r in frame_rects:
            surf = pygame.Surface((r.width, r.height), pygame.SRCALPHA)
            surf.blit(spritesheet, (0, 0), r)
            if scale != 1:
                surf = pygame.transform.scale(surf, (r.width * scale, r.height * scale))
            frames.append(surf)
        return frames

    def update(self, dt: float):
        self.timer += dt
        if self.timer >= ANIMATION_SPEED:
            self.timer = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)

    def get_frame(self) -> pygame.Surface:
        return self.frames[self.current_frame]