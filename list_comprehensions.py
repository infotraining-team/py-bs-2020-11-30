l = [1,2,3,4,5]

l2 = []
for x in l:
    if x > 2:
        l2.append(x ** 2)
print(sum(l2))

l3 = [x ** 2 for x in l if x > 2]

print(l2)
print(l3)

print(sum([x ** 2 for x in l if x > 2]))

# 123 - suma jej składników dziesiętniych to 6
# 398223075 - suma = 39
## print(2 ** 1000)

#sum = 0
# for i in str(2 ** 1000):
#     sum += int(i)
# print(sum)

print(sum(int(i) for i in str(2 ** 1000)))