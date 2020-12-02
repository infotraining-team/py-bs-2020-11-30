def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def get_function(fun, a, b):
    return fun(a,b)

print(get_function(add, 3, 5))
print(get_function(sub, 3, 5))

#funkcje anonimowe
print(get_function(lambda a, b : a + b, 3, 5))
print(get_function(lambda a, b : a - b, 3, 5))