#!/usr/bin/env python3
import sys

def distance( time_accelerate, time_max ):

    velocity = time_accelerate
    time_moving = time_max - time_accelerate

    return time_moving * velocity


if __name__ == '__main__':

    race_durations  = sys.stdin.readline().rstrip()

    ( label, durations ) = race_durations.split(':')
    race_time = []
    for time in durations.split():
        race_time.append(int(time))

    race_records    = sys.stdin.readline().rstrip()

    ( label, distances ) = race_records.split(':')
    race_dist = []
    for dist in distances.split():
        race_dist.append(int(dist))


    product = 1

    for index in range(0,len(race_time)):
        print('========')
        print(race_time[index], race_dist[index])

        wins = 0

        for acceleration in range(0, race_time[index]):
            print( acceleration, distance( acceleration, race_time[index]))

            if (  distance( acceleration, race_time[index]) > race_dist[index] ):
                wins = wins + 1
        
        print('--------')
        product = product * wins
        print( product, wins )

    print(product)