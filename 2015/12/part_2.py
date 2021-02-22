#  Usage: From root folder
#  $ python 2015/12/part_2.py input_file.json
import json
import sys


def calc_sum(data):
    if type(data) == str:
        return 0

    if type(data) == int:
        return data

    if type(data) == list:
        return sum([calc_sum(e) for e in data])

    if type(data) == dict:
        return (
            0 if "red" in data.values() else sum([calc_sum(v) for v in data.values()])
        )


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        data = json.load(f)

    print(calc_sum(data))
