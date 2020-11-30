a = 1

if a != 0:
    c = 1/a
else:
    c = 999999


try:    
    1/a
except ZeroDivisionError as error:
    print("Additional information")
    print(error)
    raise
finally:
    print("zawsze się wykonam")

alist = [1,2,3]
# print(alist[3])

name = "Leszek"
#name + 2
print(name + " Tarkowski")


