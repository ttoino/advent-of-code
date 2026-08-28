import sys
from difflib import SequenceMatcher
from string import ascii_letters

import more_itertools as mit


def parse(s: str) -> list[str]:
    return s.splitlines()


def part1(inp: list[str]):
    return sum(
        (
            ascii_letters.index(
                i[
                    SequenceMatcher(
                        None, i[: len(i) // 2], i[len(i) // 2 :]
                    ).find_longest_match()[0]
                ]
            )
            + 1
            for i in inp
        )
    )


def part2(inp: list[str]):
    return sum(
        (
            ascii_letters.index(next(iter(set.intersection(*map(set, l))))) + 1
            for l in mit.chunked(inp, 3)
        )
    )


if __name__ == "__main__":
    inp = parse(sys.stdin.read())

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
