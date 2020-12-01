alist = [1, 2, 3, 4]
string_list = ["Ola", "leszek", "Staś", "adam"]

a = 0
for elem in alist:
    print(elem)

alist.append(123)
alist.insert(0, 345)
alist.remove(2)
print(alist)
alist.pop(3)
alist.reverse()
sorted_list = alist.sort(reverse=True)
print(sorted_list)
print(alist)
print(80*"*")
# sortowanie alfabetyczne
string_list.sort(key=str.lower)
print(string_list)
string_list.sort(key=len)
print(string_list)
#alist.extend(string_list)
#alist.insert(4, string_list)
alist.append(string_list)
print(alist)
print("third:", alist[3])
print("forth:", alist[4])
print("forth[2]:", alist[4][2])

print("leszek" in string_list)    #True
print("Eberhard" in string_list)  #False

print("Lens:")
print(len(string_list))
print(len(string_list[0]))

name = "Aleksander"
print(name[0])
print(len(name))
print(name[len(name)-1])
print(name[-1])

print("-"*30)
new_list = [1,2,3,4]

other_list = new_list  # this is not a copying
print(id(other_list))
print(id(new_list))
print(new_list is other_list)

other_list = new_list[:]  # this shallow copy
print(id(other_list))
print(id(new_list))
print(new_list is other_list)

other_list[0] = 123
print(new_list)
print(other_list)

## https://www.python.org/dev/peps/pep-0008/