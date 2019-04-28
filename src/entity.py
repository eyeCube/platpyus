# entity.py

import math

import platpyus as plat
import vector
import func
import collision

class Entity:
    plist = []
    
    def __init__(self, x, y, sprite=None):
        Entity.plist.append(self)
        self.x = x
        self.y = y
        self.sprite = sprite
        self.depth = 0 # draw depth
        self.velocity = vector.Vector2()
        self.fxns_step = []
        self.fxns_draw = []
        self.bbox = None
        
    def __del__(self):
        Entity.plist.remove(self)
        if self.bbox:
            del self.bbox

    # Custom events #
    def ev_step(self):
        for i in self.fxns_step:
            i(self)
    
    def ev_draw(self):
        for i in self.fxns_draw:
            i(self)
#

'''# normal draw event for entities
def drawEntityNormal(obj):
    plat.draw.addSprite(obj.sprite, obj.x, obj.y, obj.depth)'''



'''def createCreature(_type, x, y):
    obj = Entity(x, y, _type)
    obj.depth = 100
    plat.addStepFunction(obj, entity.stepMotion)
    plat.addDrawFunction(obj, plat.drawNormal)
    return obj'''
    

'''def addForce(obj, vector): no need for this function...
    obj.velocity += vector'''


'''velx = obj.velocity.x
    vely = obj.velocity.y
    xm = math.floor(abs(obj.velocity.x))
    ym = math.floor(abs(obj.velocity.y))
    xs = func.sign(obj.velocity.x)
    ys = func.sign(obj.velocity.y)
    i = 0
    doneX = False
    doneY = False
    while True:
        i += 1
        if ( not doneX and
            collision.placeFree(obj.bbox, obj.x + xs, obj.y) ):
            # Move
            obj.x += xs
        else:
            # X Collision occurred
            obj.velocity.setX(0)
            doneX = True
        if i >= xm:
            doneX = True
        if ( not doneY and
            collision.placeFree(obj.bbox, obj.x, obj.y + ys) ):
            obj.y += ys
        else:
            # Y Collision occurred
            obj.velocity.setY(0)
            doneY = True
        if i >= ym:
            doneY = True'''
