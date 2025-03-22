# word_mapper.py
# Mapper script for word count


# Assignment 3
# Name: Om Umrania
# Roll Number: BEAD21163
# Subject: Computer Laboratory III (Computational Intelligence)

import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        print(f"{word.lower()}\t1")