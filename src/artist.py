#
# artist.py
#
# The Artist object is an interface for pygame drawing functions.
# It easily allows sprites to be drawn by depth.
#

import pygame

from const import *
import entity

# SpriteData:
# a data storage class for use by the Artist object
class SpriteData:
    def __init__(self, sprite, x, y, depth):
        self.sprite = sprite # pointer to Sprite object
        self.x = x
        self.y = y
        self.depth = depth

# Artist:
# handles drawing of sprites and screen updating
class Artist:
    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.disp = pygame.display.set_mode( (self.width, self.height,) )
        self.sprites = []
        
    # add a sprite to the end of the queue
    def addSprite(self, sprite, x, y, depth):
        spriteData = SpriteData(sprite, x, y, depth)
        self.sprites.append( spriteData )
        return spriteData

    '''def addSpritesFromEntities(self):
        for en in entity.Entity.plist:
            if en.sprite:
                self.addSprite(en.sprite, en.x, en.y, en.depth)'''
    
    # remove a sprite from the queue
    def removeSprite(self, spriteData):
        try:
            self.sprites.remove( spriteData )
        except Exception:
            print("WARNING! Failed removal of sprite {}".format(spriteData))

    # clear the sprite queue
    def clearSpriteQueue(self):
        self.sprites = []

    # draw the sprites by the order of the queue
    def blitSprites(self):
        for sdata in self.sprites:
            if sdata.sprite.image:
                self.disp.blit(
                    sdata.sprite.image,
                    (
                        round(sdata.x - sdata.sprite.xOrigin),
                        round(sdata.y - sdata.sprite.yOrigin),
                    )
                )

    # sort the sprites by depth
    def sortSprites(self):
        self.sprites = sorted(
            self.sprites,
            key=lambda spriteData: spriteData.depth,
            reverse=True
        )

    # fill the screen with the background color
    def clearScreen(self):
        self.disp.fill(WHITE)

    # pygame display update interface function
    def update(self):
        pygame.display.update()


