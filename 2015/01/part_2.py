#  Usage: From root folder
#  $ python 2015/01/part_2.py 2015/01/input

import sys

DIRS = {"(": 1, ")": -1}


def reach_basement(dirs):
    reach_basement = 0
    for dir in dirs:
        reach_basement += DIRS[dir]
        yield reach_basement
        if reach_basement == -1:
            break


if __name__ == "__main__":
    with open(sys.argv[1]) as file:
        for line in file.readlines():
            print(len(list((reach_basement(line.strip())))))
