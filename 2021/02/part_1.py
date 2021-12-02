#  Usage: From root folder
#  $ python 2021/02/part_1.py 2021/02/input

import sys


if __name__ == "__main__":
    with open(sys.argv[1]) as file:
        commands = [c.strip() for c in file.readlines()]

    horizontal = 0
    depth = 0
    for command in commands:
        direction, x = command.split(" ")
        units = int(x)

        if direction == "forward":
            horizontal += units
        if direction == "down":
            depth += units
        if direction == "up":
            depth -= units

    print(horizontal * depth)
