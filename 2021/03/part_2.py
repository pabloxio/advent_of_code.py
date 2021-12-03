#  Usage: From root folder
#  $ python 2021/03/part_1.py 2021/03/input

import sys
from typing import List


def generator_rating(
    numbers: List[str],
    keeper: str,
    bit: int = 0,
) -> str:
    if len(numbers) == 1:
        return numbers[0]

    count = [0, 0]
    for number in numbers:
        count[int(number[bit])] += 1

    keep = keeper
    if count[0] > count[1]:
        keep = "0" if keep == "1" else "1"

    return generator_rating([
        number for number in numbers if number[bit] == keep
    ], keeper, bit + 1)


if __name__ == "__main__":
    with open(sys.argv[1]) as file:
        numbers = [n.strip() for n in file.readlines()]

    oxigen = generator_rating(numbers, "1")
    co2 = generator_rating(numbers, "0")
    print(int(oxigen, 2) * int(co2, 2))
