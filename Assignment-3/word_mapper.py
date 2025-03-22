# word_mapper.py
# Mapper script for word count

import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        print(f"{word.lower()}\t1")