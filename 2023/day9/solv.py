#!/usr/bin/env python3
import sys

def distance( time_accelerate, time_max ):

    velocity = time_accelerate
    time_moving = time_max - time_accelerate

    return time_moving * velocity


if __name__ == '__main__':

    sum = 0 

    for line in sys.stdin:
        observarions = []
        first_pass = []

        for observation in line.split():
            first_pass.append(int(observation))
        observarions.append(first_pass)
        print(observarions)
        my_pass = 0

    # Reduce to a line of zeros

        non_zero = True
        while non_zero :
            non_zero = False
            next_pass = []
            for x in range(0, len(observarions[my_pass])-1):
                next_pass.append( observarions[my_pass][x+1] - observarions[my_pass][x])
            observarions.append(next_pass)
            next_pass.append
            print(observarions)
            my_pass = my_pass + 1
            for x in next_pass:
                if x != 0:
                    non_zero = True
                    continue
    #
    # Calculate last values bsed on previous ones.
        for x in range(len(observarions), 0, -1):
            obs_index = x-1
            print(obs_index, observarions[obs_index], len(observarions[obs_index]))
            if ( x == len(observarions) ):
                observarions[obs_index].append( 0 )
            else:
                observarions[obs_index].append( observarions[obs_index][len(observarions[obs_index])-1] + observarions[obs_index+1][len(observarions[obs_index])-1])
            print(obs_index, observarions[obs_index], len(observarions[obs_index]))

        sum = sum + observarions[0][-1]
    
    print(sum)


    