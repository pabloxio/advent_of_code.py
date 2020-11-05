#  Usage: From root folder
#  $ python 2015/01/part_1.py 2015/01/input

import sys

DIRS = {"(": 1, ")": -1}


def final_floor(dirs):
    return sum([DIRS[dir] for dir in dirs])


if __name__ == "__main__":
    with open(sys.argv[1]) as file:
        for line in file.readlines():
            print(final_floor(line.strip()))