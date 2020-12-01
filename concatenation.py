# words with highest frequency

book = open("proust.txt", 'r', encoding='UTF8').read()

# divide to words (white chars)
words = book.split()
words_clean = []

#clean-up
for dirty in words:
    clean = dirty.strip('.?!();:\t\n')
    if clean.endswith("'s"):
        clean = clean[:-2]
    words_clean.append(clean.lower())

#print(words_clean[:10])

# count the same words! - use dictionary
# words_freq = {"the" : 9990, "swann" : 234}

words_freq = {}
for word in words_clean:
    # if word in words_freq:
    #     words_freq[word] += 1
    # else:
    #     words_freq[word] = 1
    try:
        words_freq[word] += 1
    except KeyError:
        words_freq[word] = 1

# print(words_freq["the"])
# print(words_freq["a"])
# print(words_freq["i"])
print(len(words_clean))
print(len(words_freq.items()))

# sort and print (also use dictionary)
#final_freq = { 9990 : ["the", "a"], 3 : ["licence", "figure", "etc"] }

final_freq = {}
for word, freq in words_freq.items():
    if freq in final_freq:
        final_freq[freq].append(word)
    else:
        final_freq[freq] = [word]

keys = list(final_freq.keys())
keys.sort(reverse=True)

#sorted_freq = sorted(final_freq.keys(), reverse=True)
for freq in keys[:50]:
    print(freq, final_freq[freq])





