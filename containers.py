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

# tuples
print("------ Tuples --------")

t = 1, 2, 3
for i in t:
    print(i)

print(t[0])
#t[0] = 123

def div_with_rest(a, b):
    div = a // b
    rest = a % b
    return div, rest

result = div_with_rest(7, 3)
print(result[0], result[1])

d, r = div_with_rest(7, 3)
print(d, r)

# dictionary
print("------ Dictionary --------")
d = {1 : "one", 2: "two"}
#print(d[0]) # key error
print(d[1])
print(d[2])

d2 = {"one" : 1, "two" : 2}
print(d2["one"])

for key in d2:
    print(d2[key])

for value in d2.values():
    print(value)

print("----")
for k, v in d2.items():
    print(k)    
    print(v)

d3 = {"Artur" : ["123", "456"],
      "Beata" : ["256"]}

print(d3["Artur"])

print("Beata" in d3)

if "Ola" in d3:
    print(d3["Ola"])
else:
    print("no ola in d3")

try:
    print(d3["Ola"])
except KeyError:
    print("no ola in d3")

d3["Ola"] = ["678", "999"]

try:
    print(d3["Ola"])
except KeyError:
    print("no ola in d3")

rev_d = {}
for k, v in d.items():
    rev_d[v] = k

d[3] = "one"
print(d)
print(rev_d)