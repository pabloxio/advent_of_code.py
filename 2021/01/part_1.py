#  Usage: From root folder
#  $ python 2021/01/part_1.py 2021/01/input

import sys


if __name__ == "__main__":
    with open(sys.argv[1]) as file:
        measurements = [int(m) for m in file.readlines()]

    before = measurements[0]
    count = 0
    for measurement in measurements:
        if measurement > before:
            count += 1
        before = measurement

    print(count)
