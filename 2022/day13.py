import sys

import functools as ft



def cmp(l1: list[list | int] | int, l2: list[list | int] | int):
    if type(l1) == type(l2) == int:
        return l1 - l2 and (l1 - l2) // abs(l1 - l2)
    elif type(l1) == type(l2) == list:
        for i, j in zip(l1, l2):
            if cmp(i, j) == -1:
                return -1
            elif cmp(i, j) == 1:
                return 1
        return len(l1) - len(l2) and (len(l1) - len(l2)) // abs(len(l1) - len(l2))
    elif type(l1) == int:
        return cmp([l1], l2)
    else:
        return cmp(l1, [l2])


def parse(s: str) -> list[tuple[list | int, list | int]]:
    return [tuple(map(eval, pair.splitlines())) for pair in s.strip().split('\n\n')]


def part1(inp: list[tuple[list | int, list | int]]):
    return sum((i + 1 for i, (l1, l2) in enumerate(inp) if cmp(l1, l2) == -1))


def part2(inp: list[tuple[list | int, list | int]]):
    l = sorted([p for pair in inp for p in pair] + [[[2]], [[6]]], key=ft.cmp_to_key(cmp))
    return (l.index([[2]]) + 1) * (l.index([[6]]) + 1)


if __name__ == "__main__":
    inp = parse(sys.stdin.read())

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
