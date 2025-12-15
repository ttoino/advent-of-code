from hashlib import md5
import itertools as it
import functools as ft
import re


@ft.cache
def hash_part1(salt, i):
    return md5(bytes(f"{salt}{i}", "ascii")).hexdigest()


@ft.cache
def hash_part2(salt, i):
    h = f"{salt}{i}"
    for _ in range(2017):
        h = md5(bytes(h, "ascii")).hexdigest()
    return h


def solve(salt: str, part2: bool) -> int:
    p = re.compile(r"(.)\1\1")
    hash = hash_part2 if part2 else hash_part1

    count = 0
    for i in it.count():
        if (m := p.search(hash(salt, i))) is not None and any(
            (m.group(1) * 5) in hash(salt, i + j) for j in range(1, 1001)
        ):
            count += 1

            if count == 64:
                return i

    return -1


if __name__ == "__main__":
    inp = input()

    print(f"Part 1: {solve(inp, False)}")
    print(f"Part 2: {solve(inp, True)}")
