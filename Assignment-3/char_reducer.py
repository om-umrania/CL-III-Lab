# char_reducer.py
# Reducer script for character count

# Assignment 3
# Name: Om Umrania
# Roll Number: BEAD21163
# Subject: Computer Laboratory III (Computational Intelligence)

import sys

current_char = None
current_count = 0

for line in sys.stdin:
    char, count = line.strip().split('\t')
    count = int(count)

    if current_char == char:
        current_count += count
    else:
        if current_char:
            print(f"{current_char}\t{current_count}")
        current_char = char
        current_count = count

if current_char == char:
    print(f"{current_char}\t{current_count}")