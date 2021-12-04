#  Usage: From root folder
#  $ python 2021/04/part_1.py 2021/04/input

import sys
from typing import List


def final_score(
    board: List[List[int]],
    numbers: List[int]
) -> int:
    board_numbers = []
    for line in board:
        board_numbers.extend(line)

    return sum(set(board_numbers).difference(numbers)) * numbers[-1]


def is_board_winner(
    board: List[List[int]],
    numbers: List[int],
) -> bool:
    # Horizontal
    for line in board:
        if set(line).issubset(numbers):
            return True

    # Vertical
    for i in range(len(board)):
        vertical = [line[i] for line in board]
        if set(vertical).issubset(numbers):
            return True

    return False


if __name__ == "__main__":
    with open(sys.argv[1]) as file:
        bingo = [line.strip() for line in file.readlines()]

    numbers = [int(number) for number in bingo[0].split(",")]
    boards = []
    board = []
    for line in bingo[2:]:
        if line == "":
            boards.append(board)
            board = []
            continue
        board.append([int(n) for n in line.split()])

    stop = False
    for i in range(len(numbers)):
        for board in boards:
            if is_board_winner(board, numbers[:i]):
                print(final_score(board, numbers[:i]))
                stop = True

        if stop:
            break
