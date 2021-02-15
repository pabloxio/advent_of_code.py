#  Usage: From root folder
#  $ python 2015/03/part_1.py 2015/03/input

import sys


class Position:
    def __init__(self):
        self.x, self.y = 0, 0

    def get_key(self):
        return f"{self.x}{self.y}"

    def move(self, direction):
        if direction == "<":
            self.x -= 1
        elif direction == ">":
            self.x += 1
        elif direction == "^":
            self.y += 1
        elif direction == "v":
            self.y -= 1


if __name__ == "__main__":
    with open(sys.argv[1]) as file:
        santa = Position()
        houses = {santa.get_key(): True}
        for directions in file.readlines():
            for direction in directions.strip():
                santa.move(direction)
                houses[santa.get_key()] = True
            print(len(houses))
