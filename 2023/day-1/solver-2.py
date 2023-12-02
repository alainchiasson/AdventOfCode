#!/usr/bin/env python3
import sys

numbers = [
    ["zero"     , 0],
    ["one"      , 1],
    ["two"      , 2],
    ["three"    , 3],
    ["four"     , 4],
    ["five"     , 5],
    ["six"      , 6],
    ["seven"    , 7],
    ["eight"    , 8],
    ["nine"     , 9],
    ["0"        , 0],
    ["1"        , 1],
    ["2"        , 2],
    ["3"        , 3],
    ["4"        , 4],
    ["5"        , 5],
    ["6"        , 6],
    ["7"        , 7],
    ["8"        , 8],
    ["9"        , 9]
]


def first_num( my_string ):
 
    first_pos = len(my_string)
    first_num = -1

    for number in numbers:
        the_pos = my_string.find(number[0])
        if the_pos != -1:
            if the_pos < first_pos:
                first_pos = the_pos
                first_num = number[1]

    return first_num

def last_num( my_string ):
 
    last_pos = -1 
    last_num = -1

    for number in numbers:
        the_pos = my_string.rfind(number[0])
        if the_pos != -1:
            if the_pos > last_pos:
                last_pos = the_pos
                last_num = number[1]

    return last_num

sum = 0

for line in sys.stdin:
    strip_line = line.rstrip()
    first = int(first_num(strip_line))
    last = int(last_num(strip_line))
    num = first * 10 + last;
    print(strip_line)
    print(num)
    print()
    sum += num
    
print(sum)

