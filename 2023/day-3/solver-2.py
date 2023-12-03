#!/usr/bin/env python3
import sys

def next_position ( manual, start_line, start_pos ):

    next_line = start_line
    next_pos = start_pos + 1

    if next_pos > len(manual[start_line]):
        next_line =+ 1
        next_pos = 0

    if next_line > len( manual ):
        next_line = -1 # The End
    
    return next_line, next_pos 

def scan_for_digit ( manual, start_line, start_pos ):
    
    found_line = start_line
    found_pos = start_pos

    for found_line in range( start_line, len(manual) ):
        for found_pos in range( start_pos, len(manual[found_line])):
            if manual[found_line][found_pos].isdigit() :
                return found_line, found_pos
        start_pos = 0 # Next line start from start
    return -1, -1

if __name__ == '__main__':
    # Load data in an array
    manual = []
    for line in sys.stdin:
        manual.append(line.rstrip())

    line_number = 0
    line_position = 0

    # Start 
    while ( line_number >= 0 ):
        # In scanning digit state
        ( line_number, line_position ) = scan_for_digit( manual, line_number, line_position )

        # Record position of number

        number_line = line_number
        number_start = line_position
        number_end = line_position # We don't know this yet.

        # Digit found - now finding number state
        # Only need to advance to non-digit or end of line

        for number_end in range( line_position, len(manual[line_number])):
            if manual[line_number][number_end].isdigit() :
                continue
            else:
                break

        print( number_line, number_start, number_end, manual[number_line][number_start:number_end])

        line_position = number_end

        ( line_number, line_position ) = next_position( manual, line_number, line_position )

    