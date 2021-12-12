# Usage: From root folder
# python 2021/06/part_1.py path/to/your/input_file


import fileinput as file
from typing import List


def simulation(
    lanternfish: List[int],
    remaining_days: int,
    cache: dict = {},
) -> int:
    """
    >>> simulation([3, 4, 3, 1, 2], 18)
    26
    >>> simulation([3, 4, 3, 1, 2], 80)
    5934
    >>> simulation([3, 4, 3, 1, 2], 256)
    26984457539
    """
    if remaining_days == 0:
        return len(lanternfish)

    length = 0
    for value in lanternfish:
        key = f"{value},{remaining_days}"
        if key in cache:
            length += cache[key]
        else:
            temp = simulation(
                [6, 8] if value == 0 else [value-1],
                remaining_days-1,
                cache
            )
            cache[key] = temp
            length += temp

    return length


if __name__ == "__main__":
    initial_state = [
        int(n)
        for state in [line.strip() for line in file.input()]
        for n in state.split(",")
    ]

    for day in [80, 256]:
        print(f"day {day} {simulation(initial_state, day)}")
