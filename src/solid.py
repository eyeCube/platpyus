# solid.py

import platpyus as plat
import entity

def createSolid(spr, x, y):
    obj = entity.Entity(x, y, spr)
    obj.depth = 1000
    plat.addDrawFunction(obj, plat.drawNormal)
    plat.bboxInit(obj, obj.sprite.w, obj.sprite.h, solid=True)
    return obj
