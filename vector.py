# Vector class
# vector in 2-D space
# constructor (x, y)
# distance() - from 0,0   # import math  math.sqrt()
# add(another_vector)
# show()

class Vector:
    pass

v1 = Vector(0,2)
print(v1.distance()) ## should print 2
v2 = Vector(1,1)
v3 = v1 + v2
v3.show() ## should print 1, 3