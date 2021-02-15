#  Usage: From root folder
#  $ python 2015/02/part_1.py 2015/02/input

import sys
from itertools import combinations


class Present:
    def __init__(self, dimensions: str):
        self.dimensions = [int(d) for d in dimensions.split("x")]

    def required_paper(self):
        return sum([2 * a * b for a, b in self._sides()]) + self._smallest_side_area()

    def _smallest_side_area(self):
        return min([a * b for a, b in self._sides()])

    def _sides(self):
        return combinations(self.dimensions, 2)

    @classmethod
    def required_paper_for_all(cls, presents):
        return sum([cls(p.strip()).required_paper() for p in presents])


if __name__ == "__main__":
    with open(sys.argv[1]) as file:
        print(Present.required_paper_for_all(file.readlines()))
