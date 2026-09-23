class Turtle:
    def __init__(self,x):
        self.num = x

class Fish:
    def __init__(self,y):
        self.num = y

class Pool:
    def __init__(self,x,y):
        self.t = Turtle(x)
        self.f = Fish(y)

        print("%d turtles , %d fishes in this pool"%(self.t.num , self.f.num))

p = Pool(2,5)
