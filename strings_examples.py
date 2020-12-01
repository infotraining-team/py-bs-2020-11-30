name = "Leszek 'łoś' "
name2 = 'Leszek "pseudo"'
name3 = """Leszek 'asa' "osa" """
name4 = r"Leszek\nTarkowski"

print(name, name2, name3)
print(name4)

print(name.find("łoś"))
print(name3.find("osa"))
print(name.find("couldnotfind"))  # returns -1
print(name.upper())
print(name)

sentence = "Ala ma kota, a kot ma Alę"
print(sentence[4:])
print(sentence[:11])
print(sentence[4:11])
print(sentence[sentence.find("kota"):])
print(sentence[:-3])
print(sentence[-3:])
print(sentence[1:-1:2])
print(sentence[::-1])
print("************")
print(sentence.split())
print(sentence.split(','))

print("************")
paragraph = "Ala ma kota, a kot ma Alę\nAle ala się nie bawi z kotem"
print(paragraph)
print(paragraph.splitlines())

filename = "test_document.txt"
print(filename.startswith("test"))
print(filename.endswith(".txt"))

template = "Welcome {}, have a good day\nSincerely, {}"
print(template.format("Group", "Leszek"))

template2 = "Welcome {1}, have a good day\nSincerely, {0}"
print(template2.format("Group", "Leszek"))

template3 = "Welcome {who:30}, have a good day\nSincerely, {name}"
print(template3.format(who="Group", name="Leszek"))

template4 = "{:3.5f} {:.0f}"
print(template4.format(3.1233141241, 123.123))