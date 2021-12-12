#  Usage: From root folder
#  $ python 2021/05/part_1.py 2021/05/input

import fileinput as file
import re
from collections import defaultdict
from typing import List


def get_points(x1, y1, x2, y2) -> List[str]:
    points = []
    to_sort = []
    horizontal = True

    if x1 == x2:
        to_sort = [y1, y2]
    if y1 == y2:
        horizontal = False
        to_sort = [x1, x2]
    if len(to_sort) > 0:
        start, end = sorted([int(num) for num in to_sort])
        return [
            f"{x1},{i}" if horizontal else f"{i},{y1}"
            for i in range(start, end+1)
        ]

    return points


def view_diagram(diagram):
    for y in range(10):
        line = ""
        for x in range(10):
            if f"{x},{y}" in diagram:
                line += f'{diagram[f"{x},{y}"]}'
            else:
                line += "."

        print(line)


if __name__ == "__main__":
    vents = [line.strip() for line in file.input()]
    diagram = defaultdict(lambda: 0)
    for vent in vents:
        points = get_points(
            *re.findall("(\d+),(\d+) -> (\d+),(\d+)", vent)[0]
        )

        for point in points:
            diagram[point] += 1

    # view_diagram(diagram)
    print(sum([1 for v in list(diagram.values()) if v >= 2]))
