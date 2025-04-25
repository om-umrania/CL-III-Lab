#!/usr/bin/env python3
import sys

current_year = None
count = 0
sum_temp = 0.0

def emit(year, sum_t, cnt):
    avg = sum_t / cnt
    print(f"{year}\t{avg}")

for line in sys.stdin:
    year, temp_str = line.strip().split("\t", 1)
    temp = float(temp_str)
    if year != current_year and current_year is not None:
        emit(current_year, sum_temp, count)
        count, sum_temp = 0, 0.0
    current_year = year
    sum_temp += temp
    count += 1

# Emit last year
if current_year is not None:
    emit(current_year, sum_temp, count)