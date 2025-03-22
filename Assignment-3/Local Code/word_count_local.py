# Assignment 3
# Name: Om Umrania
# Roll Number: BEAD21163
# Subject: Computer Laboratory III (Computational Intelligence)

# word_count_local.py
from collections import defaultdict

# Read file
with open("input.txt", "r") as f:
    lines = f.readlines()

word_freq = defaultdict(int)

for line in lines:
    words = line.strip().split()
    for word in words:
        word_freq[word.lower()] += 1

# Output result
print("Word Frequency Count:")
for word, count in sorted(word_freq.items()):
    print(f"{word} : {count}")


with open("word_output.txt", "w") as out:
    for word, count in sorted(word_freq.items()):
        out.write(f"{word} : {count}\n")