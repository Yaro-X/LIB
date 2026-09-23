import random as r

class Pool():
    def start(self):
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)
        print(self.x , self.y)

    def move(self):
        self.new_x = self.x + r.choice([-1,1])
        self.new_y = self.y + r.choice([-1,1])
        self.range()

    def range(self):
        m = []
        for i in [self.new_x , self.new_y]:
            if i< 0:
                j = 0 - i

            elif i >10:
                j = 10 - (i - 10)
    
            else:
                j = i

            m.append(j)
##        print(m)
        self.x = m[0]
        self.y = m[1]

        print(self.x , self.y)

class Fish(Pool):
    pass

class Turtle(Pool):
    def move(self):
        self.new_x = self.x + r.choice([-2,-1,1,2])
        self.new_y = self.y + r.choice([-2,-1,1,2])
        self.range()


t = Turtle()
f = Fish()

