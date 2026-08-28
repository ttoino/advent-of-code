import re
import sys

import more_itertools as mit


def part1(inp: str):
    return re.search(
        "(?<=(.)(.)(.).)(?<!\\1..)(?<!\\1.)(?<!\\1)(?<!\\2.)(?<!\\2)(?<!\\3).",
        inp,
    ).start()


def part2(inp: str):
    return (
        next(
            iter(
                filter(
                    lambda x: len(set(x[1])) == 14,
                    enumerate(mit.windowed(inp, 14)),
                )
            )
        )[0]
        + 14
    )


if __name__ == "__main__":
    inp = sys.stdin.read().strip()

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
