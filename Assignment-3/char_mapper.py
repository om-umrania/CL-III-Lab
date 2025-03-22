#!/usr/bin/env python3

# char_mapper.py
# Mapper script for character count

import sys

for line in sys.stdin:
    line = line.strip()
    for char in line:
        print(f"{char}\t1")