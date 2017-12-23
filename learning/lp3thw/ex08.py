#!/usr/bin/python3.4
"""Learning!"""

FORMATTER = "{} {} {} {}"

print(FORMATTER.format(1, 2, 3, 4))
print(FORMATTER.format("one", "two", "three", "four"))
print(FORMATTER.format(True, False, False, True))
print(FORMATTER.format(FORMATTER, FORMATTER, FORMATTER, FORMATTER))
print(FORMATTER.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
