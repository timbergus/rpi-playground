#!/usr/bin/python3.7
"""Example."""

HANDLE = open('./data-science/sample.txt', 'r')

TEXT = HANDLE.read()

print(TEXT)

WORDS = TEXT.split()

print(WORDS)

COUNTS = dict()

for word in WORDS:
    COUNTS[word] = COUNTS.get(word, 0) + 1

print(COUNTS)

BIG_COUNT = None
BIG_WORD = None

for word, count in COUNTS.items():
    if BIG_COUNT is None or count > BIG_COUNT:
        BIG_WORD = word
        BIG_COUNT = count

print(BIG_WORD, BIG_COUNT)
