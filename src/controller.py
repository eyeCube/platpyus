import pygame

import entity
import image

class Controller:

    def __init__(self):
        self.pygameEvents = None
        self.isRunning = True
        self.keys = {}
        self.clock = pygame.time.Clock()

    def getPygameEvents(self):
        self.pygameEvents = pygame.event.get()

    def performPygameEvents(self):
        for ev in self.pygameEvents:
            if ev.type == pygame.QUIT: # user manually forces program to close
                self.end()
            if ev.type == pygame.KEYDOWN: # key press
                self.keys.update({ev.key : True})
            if ev.type == pygame.KEYUP: # key release
                self.keys.update({ev.key : False})

    # execute step events for all entities
    def performStepEvents(self):
        for obj in entity.Entity.plist:
            obj.ev_step()

    # execute draw events for all entities
    def performDrawEvents(self):
        for obj in entity.Entity.plist:
            obj.ev_draw()
            
    # add sprites from all tiles
    def addSpritesFromTileList(self):
        for tile in image.Tile.tiles:
            plat.draw.addSprite(tile.sprite, tile.x, tile.y, tile.depth)

    # ask if the given key is currently held down
    # accepts a pygame key constant and returns a boolean
    def getKey(self, key):
        return self.keys.get(key, False)

    # stop the main game loop
    def end(self):
        self.isRunning = False

    # close the program
    def close(self):
        pygame.display.quit()
        pygame.quit()
        quit()

















