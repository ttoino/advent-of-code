import itertools as it
import sys
import functools as ft
import operator as op


def get_group(weights, remaining, groups, target):
    for i in range(1, len(weights)):
        for c in sorted(
            (c for c in it.combinations(weights, i) if sum(c) == target),
            key=lambda x: ft.reduce(op.mul, x),
        ):
            if remaining == 2:
                return True
            if remaining < groups:
                return get_group(weights - set(c), remaining - 1, groups, target)

            return ft.reduce(op.mul, c)


def solve(weights, part: int):
    groups = 2 + part
    return get_group(weights, groups, groups, sum(weights) // groups)


if __name__ == "__main__":
    weights = {int(i.strip()) for i in sys.stdin.readlines()}

    print(f"Part 1: {solve(weights, 1)}")
    print(f"Part 2: {solve(weights, 2)}")
