# image.py

import pygame
import math

#---------#
#  Tiles  #
#---------#

class Tile:
    tiles = []
    
    def __init__(self, x, y, depth, sprite):
        Tile.tiles.append(self)
        self.x = x
        self.y = y
        self.depth = depth
        self.sprite = sprite
        self.bbox = None
        
    def __del__(self):
        Tile.tiles.remove(self)
        if self.bbox:
            del self.bbox

def createTile(x, y, depth, sprite):
    tile = Tile(x, y, depth, sprite)
    tile.bbox = collision.BoxCollider(tile, sprite.w, sprite.h)

#---------#
# Sprites #
#---------#

# Each instance of this Sprite object should be unique.
# Multiple objects can each point to the same Sprite.
class Sprite:
    def __init__(self, url, size, xOrigin=None, yOrigin=None):
        w = size[0]
        h = size[1]
        self.w = w
        self.h = h
        self.url = url
        self.image = pygame.image.load(url)
        if xOrigin is None:
            # automatically set x and y Origins to the center
            self.xOrigin = math.floor(w/2)
            self.yOrigin = math.floor(h/2)
        else:
            # manually supply origin
            self.xOrigin = xOrigin
            self.yOrigin = yOrigin



























