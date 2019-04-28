# ev_step.py

import math

import collision
import vector

_gravityVector = vector.Vector2(0, 0.2)


#----------------------#
# step event functions #
#----------------------#
# these have to be manually added to the ev_step function for
# objects that you want to have that functionality

def gravity(obj):
    vect = _gravityVector
    #if grounded: #MAKE A GROUNDED VARIABLE FOR PLATFORMING ENTITIES
    if collision.placeFree(obj.bbox, obj.x + vect.x, obj.y + vect.y):
        obj.velocity += vect

# stepMotion
# moves the entity according to its current velocity vector.
# returns:
#   True if movement successful with no collisions
#   False if movement unsuccessful, collision detected.
def motion(obj):
    _max = math.ceil(max(obj.velocity.x, obj.velocity.y))
    if _max == 0: return
    velx = obj.velocity.x / _max
    vely = obj.velocity.y / _max
    for i in range(_max):
        # Check X
        if ( obj.velocity.x and
            collision.placeFree(obj.bbox, obj.x + velx, obj.y) ):
            obj.x += velx
        else:
            obj.velocity.setX(0)
        # Check Y
        if ( obj.velocity.y and
            collision.placeFree(obj.bbox, obj.x, obj.y + vely) ):
            obj.y += vely
        else:
            obj.velocity.setY(0)



#----------------------#
# draw event functions #
#----------------------#
# these have to be manually added to the ev_draw function for
# objects that you want to have that functionality
import platpyus as plat

def draw(obj):
    plat.draw.addSprite(obj.sprite, obj.x, obj.y, obj.depth)


























