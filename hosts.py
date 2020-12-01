#content = open("hosts.txt", 'r').read()

for line in open("hosts.txt", 'r'):
    namesurname, address = line.split('@')
    name, surname = namesurname.split(".")
    print("{:>20} {:20} {}".format(name.capitalize(),
                            surname.capitalize(),
                            address, end=""))

#### expected result
# """
# Jan      Nowak       apollo.pl
# Ksawey   Mis         wp.pl
# """
#### 
# print(type(content))
# print(content)
# print(content.count("@"))

# print(content.splitlines())

# name = "jan"
# print(name.capitalize())
# print(name[0].upper() + name[1:])

# test = "ß"
# print(test)
# print(test.upper())

# eval("""print(2+2)""")

