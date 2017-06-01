handle = open('sample.txt', 'r')

text = handle.read()

print text

words = text.split()

print words

counts = dict()

for word in words:
    counts[word] = counts.get(word, 0) + 1

print counts

bigCount = None
bigWord = None

for word, count in counts.items():
    if bigCount is None or count > bigCount:
        bigWord = word
        bigCount = count

print bigWord, bigCount
