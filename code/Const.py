import pygame

# C
COLOR_BLACK = (0,0,0)
COLOR_GRAY = (70,50,70)
COLOR_WHITE = (255,255,255)
COLOR_RED = (255,0,0)

# E
ENTITY_SPEED = {
    'Level01Bg0': 0,
    'Level01Bg1': 1,
    'Level01Bg2': 2,
    'Level01Bg3': 3,
    'Level01Bg4': 4,
    'Level02Bg0': 0,
    'Level02Bg1': 1,
    'Level02Bg2': 2,
    'Level02Bg3': 3,
    'Level03Bg0': 0,
    'Level03Bg1': 1,
    'Level03Bg2': 2,
    'Level03Bg3': 3,
}

ENEMY_FRAME_RECTS = [
    pygame.Rect( 0, 0, 30, 35),
    pygame.Rect( 80, 0, 30, 35),
    pygame.Rect( 160, 0, 30, 35),
    pygame.Rect( 240, 0, 30, 35),
    pygame.Rect( 320, 0, 30, 35),
    pygame.Rect( 400, 0, 30, 35),
    pygame.Rect( 480, 0, 30, 35),
    pygame.Rect( 560, 0, 30, 35),
]

# M
MENU_OPTIONS = (
    'NEW GAME',
    'SCORE',
    'HELP',
    'QUIT'
)

#P
PLAYER_FRAME_RECTS = [
    pygame.Rect( 0, 0, 12, 27),
    pygame.Rect(13, 0, 13, 27),
    pygame.Rect(28, 0, 12, 27),
    pygame.Rect(42, 0, 12, 27),
    pygame.Rect(55, 0, 14, 27),
    pygame.Rect(70, 0, 12, 27),
]

# W
WINDOW_WIDTH = 576
WINDOW_HEIGHT = 324