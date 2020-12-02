# Vector class
# vector in 2-D space
# constructor (x, y)
# distance() - from 0,0   # import math  math.sqrt()
# add(another_vector)
# show()

import math

class Vector:
    def __init__(self, *arg):
        self.__pos = arg  

    pos = property(fget=lambda self : self.__pos)

    def distance(self):
        return math.sqrt(sum( x**2 for x in self.pos ))

    def add(self, v2):
        # TODO at home :)
        # tips - zip, *args
        # Vector(*positions)
        result = Vector(self.pos[0] + v2.pos[0], self.pos[1] + v2.pos[1])
        return result

    def show(self):
        print("V:", self.pos)

def return_type():
    return Vector

if __name__ == "__main__":
    t = 1,2,3   
    v1 = Vector(*t)
    #v1.x = 10
    print(v1.distance()) ## should print 2
    v2 = Vector(1,3,4)
    v3 = v1.add(v2)
    v3.show() ## should print 1, 3

    v4 = return_type()(2,3)
    v4.show()
    print(v1.pos)
    print(type(v1.pos))
    print(v1.distance())
