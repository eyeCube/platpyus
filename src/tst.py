
def gameEnd():
    print("game over")

#entity collision events
'''

    # Custom events #
    
    def ev_collision(self):
        for i in self.fxns_collision:
            i(self)

self.fxns_collision.append(M_PARENT, lambda x: die(x))'''

class Monster(object):
    def __init__(self, *args, **kwargs):
        self.ev_collision = []
    def __del__(self):
        pass

    
class M_Player(Monster):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.name = "Jake"
    def __del__(self):
        super().__init__(self)
        pass

# creature class as blueprints for monsters
class M_Sleeper(Monster):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.addEvent_collision(M_Player, gameEnd, [])
    def __del__(self):
        super().__init__(self)
        pass
    def addEvent_collision(self, cls, fxn, *args):
        self.ev_collision.append((cls, fxn, *args))
        
class M_SleeperKing(M_Sleeper):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.name="Sleeper King"
    def __del__(self):
        super().__init__(self)
        pass
    
#M_SLEEPER.ADD_COLLISION()

M = Monster()
m = M_Sleeper()
print(type(m).__name__)
print(m.ev_collision[0][0].__name__)
print(m.ev_collision[0][0].__name__ == type(m).__name__)
print(m.ev_collision[0][0].__name__ == type(M).__name__)
p = M_Player()
k = M_SleeperKing()

if isinstance(m, M_Sleeper):
    print("yey1")
if isinstance(M, object):
    print("yey2")
if issubclass(type(m), object):
    print("yey3")
if issubclass(type(p), Monster):
    print("yey4")
if issubclass(type(k), Monster):
    print("yey5")
if isinstance(k, Monster):
    print("yey6")
if isinstance(k, M_Sleeper):
    print("yey7")
if isinstance(k, M_SleeperKing):
    print("yey8")
