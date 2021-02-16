#  Usage: From root folder
#  $ python 2015/07/part_1_and_2.py 2015/07/input a

import sys
import re
from typing import Dict, Tuple

booklet = {}


def parse(line: str) -> Tuple[str, str]:
    return re.findall("^(.*) -> ([a-z]+)$", line.strip())[0]


def connect(wire: str, wires: Dict[str, int] = {}):
    #  Have I calculated this before?
    if wires.get(wire):
        return wires[wire]

    #  Is it just a digit?
    if wire.isdigit():
        wires[wire] = int(wire)
        return wires[wire]

    wire_elems = booklet[wire].split()

    if len(wire_elems) == 1:
        (a,) = wire_elems
        if wires.get(a):
            return wires[a]
        else:
            wires[a] = connect(a, wires)
            return wires[a]
    elif len(wire_elems) == 2:
        #  NOT wire
        _, a = wire_elems
        if wires.get(a):
            wires[wire] = ~wires[a]
            return wires[wire]
        else:
            wires[a] = ~connect(a, wires)
            return wires[a]
    elif len(wire_elems) == 3:
        a, op, b = wire_elems
        if wires.get(a):
            x = wires[a]
        else:
            x = connect(a, wires)
        if wires.get(b):
            y = wires[b]
        else:
            y = connect(b, wires)
        if op == "AND":
            wires[wire] = x & y
            return wires[wire]
        elif op == "OR":
            wires[wire] = x | y
            return wires[wire]
        elif op == "LSHIFT":
            wires[wire] = x << y
            return wires[wire]
        elif op == "RSHIFT":
            wires[wire] = x >> y
            return wires[wire]


if __name__ == "__main__":
    filename, wire = sys.argv[1:3]
    with open(filename) as file:
        booklet = {
            wire: signal for signal, wire in [parse(line) for line in file.readlines()]
        }

    day_1 = connect(wire)
    day_2 = connect(wire, {"b": day_1})

    print(f"day_1: {day_1}")
    print(f"day_2: {day_2}")
