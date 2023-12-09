#!/usr/bin/env python3
import sys

def distance( time_accelerate, time_max ):

    velocity = time_accelerate
    time_moving = time_max - time_accelerate

    return time_moving * velocity


if __name__ == '__main__':

    race_durations  = sys.stdin.readline().rstrip()

    ( label, durations ) = race_durations.split(':')

    race_time = int(durations.replace(" ",""))
    race_records    = sys.stdin.readline().rstrip()

    ( label, distances ) = race_records.split(':')
    race_dist = int(distances.replace(" ",""))
    
    product = 1

    print('========')
    print(race_time, race_dist)

    wins = 0

    for acceleration in range(0, race_time):
        print( acceleration, distance( acceleration, race_time ))

        if (  distance( acceleration, race_time) > race_dist ):
            wins = wins + 1
    
    print('--------')
    product = product * wins
    print( product, wins )

    print(product)