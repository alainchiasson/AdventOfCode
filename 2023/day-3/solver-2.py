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

def is_symbol( check ):
    # Check if a symbol
    if (check.isdigit() or check == '.') :
        return False
    else:
        return True
    
def symbol_adjacent ( manual, start_line, start_pos, end_pos ):
    # Find bounds of number
    min_line = max(0, start_line - 1)
    max_line = start_line + 1
    min_pos = max(0, start_pos - 1)
    max_pos =  end_pos + 1

    print(min_line, max_line, min_pos, max_pos)
    for line in manual[min_line:max_line+1]:
        print(line[min_pos:max_pos])

    # Loop through subset for other than digit or '.'
    for line in manual[min_line:max_line+1] :
        for check in line[min_pos:max_pos] :
            if is_symbol(check):
                return True
        
    return False

def scan_number ( manual, start_line, start_pos ):

    # Record position of number
    number_line = start_line
    number_start = start_pos
    number_end = start_pos

    # Digit found - now finding number state
    # Only need to advance to non-digit or end of line

    for number_end in range( number_start, len(manual[number_line])):
        if manual[number_line][number_end].isdigit() :
            continue
        else:
            break
    # Return sart and end - line is the same. 
    print( manual[number_line], manual[number_line][number_start:number_end])
    return number_start, number_end


def scan_for_digit ( manual, start_line, start_pos ):
    
    found_line = start_line
    found_pos = start_pos

    for found_line in range( start_line, len(manual) ):
        for found_pos in range( start_pos, len(manual[found_line])):
            if manual[found_line][found_pos].isdigit() :
                print( manual[found_line], found_pos)
                return found_line, found_pos
        start_pos = 0 # Next line start from start
    return -1, -1

if __name__ == '__main__':
    # Load data in an array
    manual = []
    for line in sys.stdin:
        manual.append(line.rstrip())

    sum = 0
    line_number = 0
    line_position = 0

    # Start 
    while ( line_number >= 0 ):
        # In scanning digit state
        ( line_number, line_position ) = scan_for_digit( manual, line_number, line_position )
        if (line_number >= 0 ):
            ( number_start, number_end ) = scan_number( manual, line_number, line_position )
            manual_number = int(manual[line_number][number_start:number_end])
            print( line_number, number_start, number_end, manual_number)
            if symbol_adjacent ( manual, line_number, number_start, number_end ):
                sum = sum + manual_number
            line_position = number_end

        ( line_number, line_position ) = next_position( manual, line_number, line_position )
    print(sum)
