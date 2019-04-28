
import math

def flatten(*args):
    ans = []
    for arg in args:
        if hasattr(arg, '__iter__'):
            ans.extend(flatten(*arg))
        else:
            ans.append(arg)
    return ans

class Vector2:
    D = 2 # number of dimensions
    
    def __init__(self, *args):
        if not args:
            self.coords = [0,0,]
        else:
            self.coords = flatten(args)

    def __getitem__(self,index):        return self.coords[index]
    def __setitem__(self,index,value):  self.coords[index] = value

    def __add__(self, val):     # Vector Addition
        ans = []
        for i in range(Vector2.D): # val must have __getitem__
            ans.append(self[i] + val[i])
        return Vector2(ans)
    def __iadd__(self, val):
        for i in range(Vector2.D):
            self[i] += val[i]
        return self

    def __sub__(self, val):     # Vector Subtraction
        ans = []
        for i in range(Vector2.D):
            ans.append(self[i] - val[i])
        return Vector2(ans)
    def __isub__(self, val):
        for i in range(Vector2.D):
            self[i] -= val[i]
        return self

    def __mul__(self, val):     # Scalar Multiplication
        ans = []
        for i in range(Vector2.D):
            ans.append(self[i] * val)
        return Vector2(ans)
    def __imul__(self, val):
        for i in range(Vector2.D):
            self[i] *= val
        return self

    def __truediv__(self, val): # Scalar Division
        ans = []
        for i in range(Vector2.D):
            ans.append(self[i] / val)
        return Vector2(ans)
    def __itruediv__(self, val):
        for i in range(Vector2.D):
            self[i] /= val
        return self
    
    def setX(self, x):      self[0] = x
    def setY(self, y):      self[1] = y
    def setLength(self, val):   # Set Magnitude
        c = self.length
        if c != 0:
            for i in range(Vector2.D):
                self[i] = ( self[i] / c ) * val
        else:
            self[0] = val
    def setCoords(self, *args): # Set Coordinates
        i = 0
        for arg in args:
            self[i] = args[i]
            i +=1

    def normalize(self):    self.setLength(1)
    def tuple(self):    return ( self.x, self.y, )
    def list(self):     return [ self.x, self.y, ]

    def rotate(self, rads):
        length=self.length
        rot=self.radians + rads
        self.setX(math.cos(rot))
        self.setY(math.sin(rot))
        self.setLength(length)

    @property           # X-axis coordinate
    def x(self):        return self[0]
    @property           # Y-axis coordinate
    def y(self):        return self[1]
    @property           # Magnitude
    def length(self):   return ( self.x**2 + self.y**2 )**0.5
    @property
    def radians(self):  return math.atan2(self.y, self.x)# + math.pi
    @property
    def degrees(self):  return math.atan2(self.y, self.x) * 180 / math.pi




print(list((0,2)))

'''
v=Vector2(1,2)
print(v.radians)
print(v.degrees)
print(v.length)
print("x",v.x)
print("y",v.y)

v = v / 6
print(v.radians)
print(v.degrees)
print(v.length)
print("x",v.x)
print("y",v.y)
'''
'''
v.rotate(0)
print(v.degrees)
print(v.length)
print("x",v.x)
print("y",v.y)
v.rotate(math.pi*4)
print(v.degrees)
print(v.length)
print("x",v.x)
print("y",v.y)'''
