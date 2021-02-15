#  Usage: From root folder
#  $ python 2015/02/part_2.py 2015/02/input

import sys
from itertools import combinations
from functools import reduce


class Present:
    def __init__(self, dimensions: str):
        self.dimensions = [int(d) for d in dimensions.split("x")]

    def required_ribbon(self):
        return self._smallest_perimeter() + self._volume()

    def _smallest_perimeter(self):
        return min([2 * a + 2 * b for a, b in self._sides()])

    def _volume(self):
        return reduce((lambda x, y: x * y), self.dimensions)

    def _sides(self):
        return combinations(self.dimensions, 2)

    @classmethod
    def required_ribbon_for_all(cls, presents):
        return sum([cls(p.strip()).required_ribbon() for p in presents])


if __name__ == "__main__":
    with open(sys.argv[1]) as file:
        print(Present.required_ribbon_for_all(file.readlines()))
