# player.py
# classes and functions for the player object

from const import *
import platpyus as plat
import entity
import events

# a data storage class for persistent player data
class Data:
    x = 32 + 8
    y = 32 + 8
    walkSpeed = 2
    runSpeed = 4

# step event for pc entity
def commandActions(pc):
    for k,v in COMMANDS.items():
        if plat.game.getKey(k):
            doCommand(pc, v)

# perform player action using a command dict consisting of:
#  {k: a command string like "move", and
#   v: additional information about the command, like where to move.}
def doCommand(pc, dic):
    for k, v in dic.items():
        if k == "move":
            print(v)
            pc.velocity += v
            if pc.velocity.length > Data.runSpeed:
                pc.velocity.setLength(Data.runSpeed)

# create, initialize, and return the player character object
def init():
    pc = entity.Entity(Data.x, Data.y, SPR_PC)
    plat.bboxInit(pc, pc.sprite.w, pc.sprite.h)
    plat.addStepFunction(pc, commandActions)
    plat.addStepFunction(pc, events.motion)
    plat.addStepFunction(pc, events.gravity)
    plat.addDrawFunction(pc, events.draw)
    return pc






