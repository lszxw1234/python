

letters = {}
with open('letters.txt') as text:
    for line in text:
        line = line.strip()
        words = line.split(' ')
        for word in words:
            word = word.lower()
            if word not in letters:
                letters[word] = 1
            else:
                letters[word] += 1

for (key, value) in letters.items():
    print(key +':      ' +str(value))