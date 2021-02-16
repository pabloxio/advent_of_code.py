#  Usage: From root folder
#  $ python 2015/08/part_1.py 2015/08/input

import sys

if __name__ == "__main__":
    with open(sys.argv[1]) as file:
        strings = [s.strip() for s in file.readlines()]

    print(sum([len(s) - len(eval(s)) for s in strings]))
