#  Usage: From root folder
#  $ python 2015/09/part_1_and_2.py 2015/09/input

import sys
import re
from itertools import permutations
from typing import Dict, List, Tuple


def parse(s):
    return re.findall("([a-zA-Z]+) to ([a-zA-Z]+) = ([0-9]+)", s)[0]


def step_cost(cities: List[str], distances: Tuple[str, Dict[str, int]]) -> int:
    start, end = cities
    try:
        return distances[start][end]
    except KeyError:
        return distances[end][start]


def route_cost(
    cities: List[str], distances: Tuple[str, Dict[str, int]], memo: Dict[str, int] = {}
) -> int:
    route = "".join(cities)

    if memo.get(route):
        return memo[route]

    start, end = cities[0:2]
    if len(cities) == 2:
        return step_cost([start, end], distances)

    memo[route] = step_cost([start, end], distances) + route_cost(
        cities[1:], distances, memo
    )

    return memo[route]


if __name__ == "__main__":
    distances = {}
    cities = set()

    with open(sys.argv[1]) as file:
        for s in file.readlines():
            start, end, distance = parse(s.strip())
            cities.add(start)
            cities.add(end)
            if not distances.get(start):
                distances[start] = {end: int(distance)}
            else:
                distances[start][end] = int(distance)

    route_costs = [
        route_cost(list(route), distances) for route in list(permutations(cities))
    ]

    print(f"day_1: {min(route_costs)}")
    print(f"day_2: {max(route_costs)}")
