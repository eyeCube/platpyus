# vector.py

import func

#
# >>Vector2
#
# -2-Dimensional Vector class
# -On creating a new Vector2 object,
#   pass no arguments to default to a (0,0) vector;
#   or you may pass in any number of recursively iterable variables.
# -EXAMPLE. The following all produce the same result:
#   Vector2(2,4)
#   Vector2((2,4,))
#   Vector2([(2,4,),])
#
class Vector2:
    D = 2 # number of dimensions
    
    def __init__(self, *args):
        if not args:
            self.coords = [0,0,]
        else:
            self.coords = func.flatten(args)

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
    def setCoords(self, *args): # Set Coordinates
        i = 0
        for arg in args:
            self[i] = args[i]
            i +=1

    def normalize(self):    self.setLength(1)
    def tuple(self):    return ( self.x, self.y, )
    def list(self):     return [ self.x, self.y, ]

    @property           # X-axis coordinate
    def x(self):        return self[0]
    @property           # Y-axis coordinate
    def y(self):        return self[1]
    @property           # Magnitude
    def length(self):   return ( self.x**2 + self.y**2 )**0.5














