
import pygame
import math

# entity.py
# vector.py
# func.py
# collision.py
# ev_step.py

G=0.2 #gravity intensity
#_gravityVector = vector.Vector2(0, G)


def kill(thing):
    thing.hp=0
#clean up dead things at end of each step?
#del thing


#----------------------#
# step event functions #
#----------------------#
# these have to be manually added to the ev_step function for
# objects that you want to have that functionality

def gravity(obj, vector2):
    vect = vector2
    #if grounded: #MAKE A GROUNDED VARIABLE FOR PLATFORMING ENTITIES
    if collision.placeFree(obj.bbox, obj.x + vect.x, obj.y + vect.y):
        obj.velocity += vect

# stepMotion
# moves the entity according to its current velocity vector.
# returns: NOTHING CURRENTLY>>>
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

def draw(obj):
    plat.draw.addSprite(obj.sprite, obj.x, obj.y, obj.depth)


#----------------------#
#   collisions         #
#----------------------#

class BoxCollider():
    instances = [] # is this necessary????? Might be..... but also need list of collision events for each entity or type of entity
    
    def __init__(self, owner, w, h, solid=False):
        BoxCollider.instances.append(self)
        # owner object has information about X and Y location
        self.owner = owner
        self.width = w
        self.height = h
        self.solid = solid

    def __del__(self):
        BoxCollider.instances.remove(self)

#placeFree:
# moves collision box to the new location x,y and
# check for a collision with all bboxes at their current positions
def placeFree(bbox, x, y):
    #maybe check a list of all solid objects instead of all objects...
    for col in BoxCollider.instances: # should check its own list of collisions
        if col is bbox: continue # shouldn't be needed with ^
        if col.solid: # and collides with solid
            if overlaps(
                x, y, bbox.w, bbox.h,
                col.owner.x, col.owner.y, col.w, col.h
            ):
                return False # instead return ids of ALL colliding things?
    return True

#overlaps: returns whether two boxes overlap
def overlaps(x1, y1, w1, h1, x2, y2, w2, h2):
    x1 = round(x1)
    y1 = round(y1)
    x2 = round(x2)
    y2 = round(y2)
    return (
        x1 <= x2 + w2 and
        x1 + w1 >= x2 and
        y1 <= y2 + h2 and
        y1 + h1 >= y2
    )

class Player(Entity):
    def __init__(self):
        def collev(self):
            kill(self)
        addEventCollision(self, wallParent, collev)
        self.terrain=(AIR,WATER,)


# various independent global functions

# flatten:
# reduces an iterable down to one layer.
# recursively check each item in the iterable.
# if any items in the root iterable are themselves iterable,
# then split those items and add them into the root iterable.
def flatten(*args):
    ans = []
    for arg in args:
        if hasattr(arg, '__iter__'):
            ans.extend(flatten(*arg))
        else:
            ans.append(arg)
    return ans

# sign: returns 1 or -1 (positive or negative)
def sign(value):
    return 1 if value >= 0 else -1


#
# >>Vector2
#
# -2-Dimensional Vector class.
# -On creating a new Vector2 object,
#   pass no arguments to default to a (0,0) vector;
#   or you may pass in any number of recursively iterable variables.
#     -EXAMPLE. The following all produce the same result:
#       Vector2(2,4)
#       Vector2((2,4,))
#       Vector2([(2,4,),])
#     which is a Vector2 object with coords values 2 and 4
#
class Vector2:
    D = 2 # number of dimensions
    
    def __init__(self, *args):
        if not args:#default
            self.coords = [0,0,]
        else:       #extract the coordinate data
            self.coords = flatten(args)
    
    def __getitem__(self,index):        return self.coords[index]
    def __setitem__(self,index,value):  self.coords[index] = value

    #for +,-,+=,-= : val must have __getitem__ (must be indexable)
    def __add__(self, val):     # Vector Addition
        ans = []
        for i in range(Vector2.D):  
            ans.append(self[i] + val[i])
        return Vector2(ans)
    def __iadd__(self, val):    # "
        for i in range(Vector2.D):
            self[i] += val[i]
        return self
    def __sub__(self, val):     # Vector Subtraction
        ans = []
        for i in range(Vector2.D):
            ans.append(self[i] - val[i])
        return Vector2(ans)
    def __isub__(self, val):    # "
        for i in range(Vector2.D):
            self[i] -= val[i]
        return self
    
    def __mul__(self, val):     # Scalar Multiplication
        ans = []
        for i in range(Vector2.D):
            ans.append(self[i] * val)
        return Vector2(ans)
    def __imul__(self, val):    # "
        for i in range(Vector2.D):
            self[i] *= val
        return self
    def __truediv__(self, val): # Scalar Division
        ans = []
        for i in range(Vector2.D):
            ans.append(self[i] / val)
        return Vector2(ans)
    def __itruediv__(self, val):# "
        for i in range(Vector2.D):
            self[i] /= val
        return self
    
    def setX(self, x):      self[0] = x
    def setY(self, y):      self[1] = y
    def setCoords(self, *args): # Set Coordinates using an iterable
        self.coords = flatten(args)
    def setLength(self, val):   # Set Length or Magnitude
        c = self.length
        if c != 0:
            for i in range(Vector2.D):
                self[i] = (self[i] / c) * val
        else:
            self.setX(val)
    #rotate the Vector2 about the origin (0,0) by rads radians.
    def rotate(self, rads):
        length = self.length
        rot = self.radians + rads
        self.setX(math.cos(rot))
        self.setY(math.sin(rot))
        self.setLength(length)
    def tuple(self):        return (self.x, self.y,)
    def list(self):         return [self.x, self.y,]
    def normalize(self):    self.setLength(1)

    @property           # X-axis coordinate
    def x(self):        return self[0]
    @property           # Y-axis coordinate
    def y(self):        return self[1]
    @property           # Magnitude
    def length(self):   return ( self.x**2 + self.y**2 )**0.5
    @property           # Angle in Radians
    def radians(self):  return math.atan2(self.y, self.x)
    @property           # Angle in Degrees
    def degrees(self):  return math.atan2(self.y, self.x) * 180 / math.pi


        
class Entity:
    plist = [] #plist??? Name
    
    def __init__(self, x, y, sprite=None):
        Entity.plist.append(self)
        self.x=x
        self.y=y
        self.sprite=sprite
        self.depth=0 # draw depth
        self.velocity=Vector2()
        self.mobility=0
        self.fxns_step=[]
        self.fxns_draw=[]
        self.bbox=None
        
    def __del__(self):
        Entity.plist.remove(self)
        #are these del statements necessary? Probably not, I think...
        #unless references to them exist elsewhere...
        if self.bbox:
            del self.bbox
        if self.stats:
            del self.stats
        #

    # Custom events #
    def ev_step(self):
        for i in self.fxns_step:
            i(self)
    
    def ev_draw(self):
        for i in self.fxns_draw:
            i(self)


#put this in the game file, not platpyus.
class Stats:
    def __init__(self):
        self.hp=0
        self.hpMax=0
        self.stam=0
        self.stamMax=0
        self.atk=0
        self.atkType=0 #shock, pierce
        self.defs=0 #shock armor
        self.defp=0 #pierce armor
        self.spd=0 #attack speed
        self.knockback=0
        self.kick=0
        self.poise=0 #resistance vs. kick
        self.eva=0 #evasion. Parrying? Blocking??
        #self.range=0 #range bonus? Nahhh
        #self.fatigue=0 #damages stamina? Could just have max stam. damage, don't need a new var for this.


#-----------#
# collision #
#-----------#

def bboxInit(obj, w, h):
    obj.bbox = collision.BoxCollider(obj, w, h)

#--------#
# entity #
#--------#

def addStepFunction(obj, func):
    obj.fxns_step.append(func)
def addDrawFunction(obj, func):
    obj.fxns_draw.append(func)

#----------------#
# global objects #
#----------------#

game = controller.Controller()
draw = artist.Artist(WINDOW_W, WINDOW_H)
pc = player.init()





'''
Ideas

different buttons for attacking w/ melee weapons:
(these could be different skills on a skill tree?)
    bludgeon
    swing
    thrust
    throw

Classes:
    Knight
        Skills:
            Bludgeon
                range: 1 (+ weapon reach)
                deals damage based on weapon mass and type.
            Thrust
                range: 3 (+ weapon reach)
                Pierce attack +2
            Throw
                range: inf.
                Atk +4 - weapon mass
        Attributes:
            HP +20
            Atk +2
            Def +2
            Eva +4
    Mystic
        Skills:
        Attributes:
            Wis +2
    Rogue
        Skills:
        Attributes:
            HP +10
            Atk +2
            Spd +2
            Eva +6
            Mob +2

 H         H 
 H    #    H 
.H....@....H.


'''
        


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
