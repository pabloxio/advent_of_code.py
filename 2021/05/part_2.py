#  Usage: From root folder
#  $ python 2021/05/part_2.py 2021/05/input

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
        start, stop = sorted([int(num) for num in to_sort])
        return [
            f"{x1},{i}" if horizontal else f"{i},{y1}"
            for i in range(start, stop+1)
        ]

    right_dir = True
    down_dir = True
    if int(x1) > int(x2):
        right_dir = False
    if int(y1) > int(y2):
        down_dir = False

    # x_start, x_stop = sorted([int(num) for num in [x1, x2]])
    x_start = int(x1)
    x_stop = int(x2)
    x_step = 1 if right_dir else -1

    y = int(y1)
    y_stop = int(y2)
    y_step = 1 if down_dir else -1

    for x in range(x_start, x_stop + x_step, x_step):
        points.append(f"{x},{y}")

        # print(points)
        # print("{x},{y} == {x_stop},{y_stop}")
        # print("{x},{y}" == f"{x_stop},{y_stop}")
        # breakpoint()
        if f"{x},{y}" == f"{x_stop},{y_stop}":
            return points

        if right_dir and x > x_stop:
            return []
        if not right_dir and x < x_stop:
            return []
        if down_dir and y > y_stop:
            return []
        if not down_dir and y < y_stop:
            return []

        y += y_step

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
