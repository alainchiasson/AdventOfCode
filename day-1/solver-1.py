#!/usr/bin/env python3
import sys

def first_num( string ):
    for i in range(len(string)):
        if string[i].isdigit():
            return string[i]
    return -1

def last_num( string ):
    for i in range(len(string)-1, -1, -1):
        if string[i].isdigit():
            return string[i]
    return -1

sum = 0

for line in sys.stdin:
    print(line)
    line.rstrip()
    first = int(first_num(line))
    last = int(last_num(line))
    num = first * 10 + last;
    print(num)
    sum += num
    
print(sum)

