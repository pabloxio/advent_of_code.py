#  Usage: From root folder
#  $ python 2015/03/part_2.py 2015/03/input

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
        for directions in file.readlines():
            santa = Position()
            robo_santa = Position()
            houses = {santa.get_key(): True}

            for direction in directions.strip()[0::2]:
                santa.move(direction)
                houses[santa.get_key()] = True

            for direction in directions.strip()[1::2]:
                robo_santa.move(direction)
                houses[robo_santa.get_key()] = True

            print(len(houses))
