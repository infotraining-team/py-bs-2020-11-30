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