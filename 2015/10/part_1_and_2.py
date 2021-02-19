#  Usage: From root folder
#  $ python 2015/10/part_1_and_2.py 2015/10/input 50

import sys
import re


def lock_and_say(sequence: str, times: int) -> str:
    if times == 0:
        return sequence

    new_sequence = "".join(
        [
            f"{str(m.end() - m.start())}{m.group()[0]}"
            for m in re.finditer(r"(\d)\1*", sequence)
        ]
    )

    return lock_and_say(new_sequence, times - 1)


if __name__ == "__main__":
    with open(sys.argv[1]) as file:
        for line in file.readlines():
            print(f"{len(lock_and_say(line.strip(), int(sys.argv[2])))}")
