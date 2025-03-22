#!/usr/bin/env python3

# char_mapper.py
# Mapper script for character count


# Assignment 3
# Name: Om Umrania
# Roll Number: BEAD21163
# Subject: Computer Laboratory III (Computational Intelligence)

import sys

for line in sys.stdin:
    line = line.strip()
    for char in line:
        print(f"{char}\t1")