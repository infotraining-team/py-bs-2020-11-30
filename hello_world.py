# Welcome :)
print("Hello world")
a = 1
print(a + 10)

if a > 3:
    print("tada")   
else:
    print("something")

alist = [1, 2, 3]
another_list = [1, "Leszek", 3.14]

another_list.append(123)
print("List length", len(another_list))

for x in alist:
    print(x)
    x = x + 2  ## to nic nie zmienia
               ## może gdyby był operator x++ (ale nie ma)

x = 0
while x < 5:
    x += 1
    print("x", x)

alist[0] = 3

print(alist)

# print("*****")
# for i in range(1,10, 2):
#     print(i)