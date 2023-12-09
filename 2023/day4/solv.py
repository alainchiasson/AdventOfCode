#!/usr/bin/env python3
import sys

def calc_point( card ):

    print( card )

    # Split ID, Winning and Numbers
    ( card_id, scratch_ticket ) =  card.split(':')
    ( winning_numbers, my_numbers ) = scratch_ticket.split('|')

    drawn = []
    for x in winning_numbers.split():
        drawn.append(int(x))
    
    chosen = []
    for x in my_numbers.split():
        chosen.append(int(x))

    print(drawn)
    print(chosen)
    # see if winning is in chosen
    points = 0
    for x in drawn:
        print(x, chosen, points)
        if x in chosen:
            points = points * 2 if points > 0 else 1
            print("add, now ", points)            

    return (points)

if __name__ == '__main__':

    sum = 0

    for line in sys.stdin:
        points = calc_point( line.rstrip() )
        sum = sum + points
        print(points, sum)

    print(sum)

    