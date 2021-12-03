#  Usage: From root folder
#  $ python 2021/03/part_1.py 2021/03/input

import sys


if __name__ == "__main__":
    with open(sys.argv[1]) as file:
        lines = [line.strip() for line in file.readlines()]

    gama = ""
    epsilon = ""
    for i in range(len(lines[0])):
        count = [0, 0]
        for line in lines:
            count[int(line[i])] += 1

        if count[0] > count[1]:
            gama += "0"
            epsilon += "1"
        else:
            gama += "1"
            epsilon += "0"

    print(int(gama, 2) * int(epsilon, 2))
