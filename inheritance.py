class A:
    def __init__(self):
        self.a_attr = 0
        print("A constructor")
    def method_A(self):
        print("method A")

class B(A):
    def __init__(self):
        A.__init__(self)
        self.b_attr = 1
        print("B constructor")

    # def method_A(self):
    #     print("method A from B")

# class B:
#     def __init__(self):
#         self.a = A()

inst1 = A()
inst2 = B()
inst2.method_A()

#print(inst2.a_attr)

# class Shape:
#     pass

# class Rectangle:
#     def Area(self):
#         pass

# class Circle:
#     def Area(self):
#         pass

        #         Shape
        #         |    |
        #       |         |              
        #     |             |
        # Circle          Rectangle

###array<Shape> shapes
# shapes = []
# shapes.append(Rectangle)
# shapes.append(Circle)

# for shape in shapes:
#     shape.Area()

