a = 5

l = [1,2,3]

def add(a,b):
    return a+b

print(type(a))
print(type(l))
print(type(add))

print(id(a))
print(id(l))
print(id(add))

print(a)
print(l)
print(add)

class Test:
    def __init__(self, name="empty"):
        print("Constructor")
        self.name = name + " " + str(id(self))
        self.attribute = 0

    def method(self):
        print("I am method from", self.name)

print(type(Test))
print(id(Test))

obj1 = Test()
obj2 = Test("object 2")

# print(type(obj1))
# print(id(obj1))
# print(type(obj2))
# print(id(obj2))

obj1.method()
# Test.method(obj1)
obj2.method()

obj1.attribute = 123
obj2.attribute = 666

print(obj1.name)
print(obj2.name)
