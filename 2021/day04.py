import itertools as it
import sys

import more_itertools as mit


def verify_solved(boards: list[tuple[tuple[int, ...], ...]]):
    for b in boards:
        for r in it.chain(b, zip(*b)):
            if sum(r) == 5 * 255:
                return b
    return False


def verify_solved_p2(board: tuple[tuple[int, ...], ...]):
    for r in it.chain(board, zip(*board)):
        if sum(r) == 5 * 255:
            return True
    return False


def parse(inp: str) -> tuple[list[int], list[tuple[tuple[int, ...], ...]]]:
    lines = inp.splitlines()
    numbers = list(map(int, lines[0].split(",")))
    boards = [
        tuple(tuple(int(i) for i in line.split()) for line in b if line)
        for b in mit.grouper(lines[1:], 6)
    ]
    return numbers, boards


def part1(inp: tuple[list[int], list[tuple[tuple[int, ...], ...]]]) -> int:
    numbers, boards = inp
    numbers = iter(numbers)
    b = False
    n = 0
    while not (b := verify_solved(boards)):
        n = next(numbers)
        boards = [
            tuple(tuple(255 if i == n else i for i in r) for r in b)
            for b in boards
        ]
    return n * sum(filter(lambda x: x != 255, sum(b, ())))


def part2(inp: tuple[list[int], list[tuple[tuple[int, ...], ...]]]) -> int:
    numbers, boards = inp
    numbers = iter(numbers)
    b = ()
    n = 0
    while len(boards) > 0:
        n = next(numbers)
        boards = [
            tuple(tuple(255 if i == n else i for i in r) for r in b)
            for b in boards
        ]
        b = boards[0]
        boards = [b for b in boards if not verify_solved_p2(b)]
    return n * sum(filter(lambda x: x != 255, sum(b, ())))


if __name__ == "__main__":
    inp = parse(sys.stdin.read())

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
