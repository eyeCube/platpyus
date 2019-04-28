class A:
    def __init__(self):
        self.ev=[]
        self.name="jaek"
        def f(*args):
            kill(args[0])
        self.addev(f)
    def addev(self, f):
        self.ev.append((f, (self,),))

def kill(thing):
    print(thing.name,"killed.")

a=A()
a.ev[0][0](a.ev[0][1])

