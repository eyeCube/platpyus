# main.py

import pygame

from const import *
import platpyus as plat

def main():
    pygame.init()
    pygame.display.set_caption(GAME_TITLE)
    
    while plat.game.isRunning:
        plat.game.clock.tick(FPSMAX)
        plat.game.getPygameEvents()
        plat.game.performPygameEvents()
        plat.game.performStepEvents()   # <-- Step Event
        # Drawing Sequence #
        plat.draw.clearScreen()
        plat.draw.clearSpriteQueue()
        plat.game.performDrawEvents()   # <-- Draw Event (queue sprites)
        plat.game.addSpritesFromTileList()
        plat.draw.sortSprites()
        plat.draw.blitSprites()
        plat.draw.update()
        #
    plat.game.close()

if __name__ == '__main__':
    main()

        #plat.draw.addSpritesFromEntities()
