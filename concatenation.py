# words with highest frequency

book = open("proust.txt", 'r', encoding='UTF8').read()
words = book.split()
words_clean = []

#clean-up
for dirty in words:
    clean = dirty.strip('.?!();:\t\n')
    if clean.endswith("'s"):
        clean = clean[:-2]
    words_clean.append(clean.lower())

print(words_clean[:1000])

words_freq = {"the" : 734, "swann" : 234}

for word in words_clean:
    pass

# divide to words (white chars)
# count the same words! - use dictionary

# -- later -- :)
# sort and print