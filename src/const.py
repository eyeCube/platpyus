# const.py

import pygame

import image

# Game data
GAME_TITLE = "Platpyus"

# Settings
WINDOW_W = 1024
WINDOW_H = 768
FPSMAX = 60

# Colors - RGB values 0-255
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
ORANGE = (255,128,0,)
YELLOW = (255,255,0,)
CYAN = (0,255,255,)
PURPLE = (255,0,255,)

# Sprites
# import some sprites for shared use by the objects in the game
SPR_PC = image.Sprite("../art/sprite/spr_pc.png", (16, 16,))

# Key commands
COMMANDS = {
    pygame.K_LEFT:  {"move":(-1,0)},
    pygame.K_RIGHT: {"move":(1,0)},
}
