#!/usr/bin/env python3
import sys

def distance( time_accelerate, time_max ):

    velocity = time_accelerate
    time_moving = time_max - time_accelerate

    return time_moving * velocity


if __name__ == '__main__':

    directions  = sys.stdin.readline().rstrip()

    skip_blank_line = sys.stdin.readline().rstrip()

    # Left array
    left = []
    right = []

    my_map = {}
    for line in sys.stdin:
        node_key = line.split('=')[0].rstrip()

        left = line.split('=')[1].lstrip()[1:4]
        right = line.split('=')[1].lstrip()[6:9]

        my_map[node_key] = { "L": left, "R": right }

    print( my_map )

    # Follow directions

    node = 'AAA'
    num_steps = 0

    while ( node != 'ZZZ'):
        for direction in directions:

            next_node = my_map[node][direction]
            num_steps = num_steps + 1
            print( node, direction,  next_node, num_steps )
            if (next_node == 'ZZZ') :
                exit()
            node = next_node

    print( num_steps )


        
