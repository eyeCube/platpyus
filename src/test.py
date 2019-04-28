class A:
    meta_a = 0
    class B:
        def __init__(self, a):
            self.a = a
        def print(self):
            print(self.a)

    def __init__(self):
        self.what = "what"
        print(self.what)
            
b = A.B(1)
b.print()
'''classes within classes. How barbaric!'''
