def add(a, b):
    """adds two things together
    and returns the result
    """
    c = a + b
    return c

print(add(3, 4))
print(add("Ala", 'k'))
# print(add("Ala",3))

def print_person(name, surname="Noone", age=None):
    print(name, surname)

print_person("Leszek", "Tarkowski")
imie = "Ola"
nazwisko = "Aasdas"
print_person(imie, nazwisko)

print_person(name=imie, surname=nazwisko)
print_person(surname=nazwisko, name="Leszek")
print_person("Oleg")
help(add)

print("---------")
def multiadd(*args):
    res = 0
    for i in args:
        res += i
    return res

print(multiadd(2, 3))
print("---------")
print(multiadd(2, 3, 4, 5, 6))

def print_names(name, surname, *args, **kwargs):
    print(name, surname)
    print(args)
    print(kwargs)

print_names("Leszek", "T", 213)
print_names(name="Leszek", surname="T", age=43)

