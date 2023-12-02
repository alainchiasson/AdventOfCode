#!/usr/bin/env python3
import sys

def get_id( string ):
    (just_text, game_id)= string.split(':')[0].split()
    return int(game_id)

def get_game( string ):
    return string.split(':')[1]

def count_red( string ):
    for ball_count in string.split(','):
        if ball_count.split()[1] == 'red':
            return int(ball_count.split()[0])
    return 0

def count_blue( string ):
    for ball_count in string.split(','):
        if ball_count.split()[1] == 'blue':
            return int(ball_count.split()[0])
    return 0

def count_green( string ):
    for ball_count in string.split(','):
        if ball_count.split()[1] == 'green':
            return int(ball_count.split()[0])
    return 0

def draw_set_possible( string ):
    for draw in string.split(','):
        if count_red(draw) > 12:
            return False
        if count_green(draw) > 13:
            return False
        if count_blue(draw) > 14:
            return False
    return True

def game_set_possible( string ):
    for draw in string.split(','):
        if not draw_set_possible(draw):
            return False
    return True


def game_possible( string ):
    for game_set in string.split(';'):
        if not game_set_possible(game_set):
            return False
    return True

def calc_power_set( string ):
    ( red, blue, green ) = ( 0,0,0 )
    for game_set in string.split(';'):
        for draw in game_set.split(','):
            red = red if red > count_red(draw) else count_red(draw)
            blue = blue if blue > count_blue(draw) else count_blue(draw)
            green = green if green > count_green(draw) else count_green(draw)
    return red * blue * green

sum = 0

for line in sys.stdin:
    input = line.rstrip()
    game_id = get_id(input)
    sum += calc_power_set(get_game(input))
    
print(sum)

