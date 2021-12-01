#  Usage: From root folder
#  $ python 2021/01/part_2.py 2021/01/input

import sys


if __name__ == "__main__":
    with open(sys.argv[1]) as file:
        measurements = [int(m) for m in file.readlines()]

    before = sum(measurements[0:3])
    count = 0
    for i in range(len(measurements)-2):
        current = sum(measurements[i:i+3])
        if current > before:
            count += 1
        before = current

    print(count)
