import itertools as it
import sys
from typing import cast
import re


# Alternative solution: solve the system of modular equations of the type
#   t + n + p = 0 mod k
def solve(discs: list[tuple[int, int, int]], part2: bool) -> int:
    if part2:
        discs += [(len(discs) + 1, 11, 0)]

    for t in it.count():
        b = True

        for n, k, p in discs:
            b &= (t + n + p) % k == 0

        if b:
            return t

    return -1


if __name__ == "__main__":
    p = re.compile(
        r"Disc #(\d) has (\d+) positions; at time=0, it is at position (\d+)\."
    )
    discs = [
        cast("tuple[int, int, int]", tuple(map(int, m.groups())))
        for i in sys.stdin.readlines()
        if (m := p.match(i))
    ]

    print(f"Part 1: {solve(discs, False)}")
    print(f"Part 2: {solve(discs, True)}")
