#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    if not line or line.startswith("#"):
        continue
    try:
        date, temp = line.split(",", 1)
        year = date.split("-")[0]
        temp = float(temp)
        print(f"{year}\t{temp}")
    except Exception:
        continue
