# Assignment 3
# Name: Om Umrania
# Roll Number: BEAD21163
# Subject: Computer Laboratory III (Computational Intelligence)


# char_count_local.py
from collections import defaultdict

# Read file
with open("input.txt", "r") as f:
    data = f.read()

# Character frequency counter
char_freq = defaultdict(int)

for char in data:
    char_freq[char] += 1

# Output result
print("Character Frequency Count:")
for char, count in sorted(char_freq.items()):
    print(f"{repr(char)} : {count}")


with open("char_output.txt", "w") as out:
    for char, count in sorted(char_freq.items()):
        out.write(f"{repr(char)} : {count}\n")