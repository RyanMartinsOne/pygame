import pygame

# C
COLOR_BLACK = (0,0,0)
COLOR_GRAY = (70,50,70)
COLOR_WHITE = (255,255,255)
COLOR_RED = (255,0,0)

COIN_FRAME_RECTS = [
    pygame.Rect( 0, 0, 14, 15),
    pygame.Rect( 16, 0, 14, 15),
    pygame.Rect( 34, 0, 9, 15),
    pygame.Rect( 53, 0, 4, 15),
    pygame.Rect( 67, 0, 9, 15),
    pygame.Rect( 80, 0, 14, 15),
]

COIN_SCALE = 3

#D
DEFAULT_FRAME_SPEED = 0.1


# E
ENTITY_SPEED = {
    'Enemy'     : 2,
    'GRAVITY'   : 0.15,
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
    'Player': 2,
    'Player_Jump': -5,
    'Coin'      : 2,
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

ENEMY_SCALE = 2

EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_COIN  = pygame.USEREVENT + 2

#G
GRAVITY = 700

#J
JUMP_FORCE = -450
JUMP_KEYS = (pygame.K_SPACE, pygame.K_UP)

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

PLAYER_JUMP_FRAME_RECTS = [
    pygame.Rect( 0,  4, 12, 26),
    pygame.Rect( 31, 8, 14, 22),
    pygame.Rect( 64, 0, 13, 26),
    pygame.Rect( 96, 0, 12, 28),
    pygame.Rect(127, 8, 14, 22),
]

PLAYER_SCALE = 3

# W
WINDOW_WIDTH = 576
WINDOW_HEIGHT = 324