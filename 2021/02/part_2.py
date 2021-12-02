#  Usage: From root folder
#  $ python 2021/02/part_2.py 2021/02/input

import sys


if __name__ == "__main__":
    with open(sys.argv[1]) as file:
        commands = [c.strip() for c in file.readlines()]

    horizontal = 0
    depth = 0
    aim = 0
    for command in commands:
        direction, x = command.split(" ")
        units = int(x)

        if direction == "forward":
            horizontal += units
            if aim != 0:
                depth += aim * units
        if direction == "down":
            aim += units
        if direction == "up":
            aim -= units

    print(horizontal * depth)
