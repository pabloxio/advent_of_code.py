#  Usage: From root folder
#  $ python 2015/08/part_2.py 2015/08/input

import sys


def parse(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')


if __name__ == "__main__":
    with open(sys.argv[1]) as file:
        print(
            sum(
                [(len(parse(s.strip())) + 2) - len(s.strip()) for s in file.readlines()]
            )
        )
