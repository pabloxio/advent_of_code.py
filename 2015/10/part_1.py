#  Usage: From root folder
#  $ python 2015/10/part_1.py 2015/10/input 40

import sys
from typing import List


def say(sequence: List[str]) -> str:
    control = sequence[0]
    count = 0
    result = ""
    for elem in sequence:
        if elem == control:
            count += 1
        else:
            result = f"{result}{count}{control}"
            control = elem
            count = 1
    result = f"{result}{count}{control}"
    return result


def lock_and_say(sequence: str, times: int) -> str:
    if times == 0:
        return sequence

    return lock_and_say(say(list(sequence)), times - 1)


if __name__ == "__main__":
    filename, times = sys.argv[1:3]

    with open(filename) as file:
        for s in file.readlines():
            print(len(lock_and_say(s.strip(), int(times))))
