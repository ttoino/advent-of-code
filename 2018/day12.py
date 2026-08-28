import sys

import more_itertools as mit

ITERS = 50_000_000_000


def parse(
    inp: list[str],
) -> tuple[tuple[bool, ...], dict[tuple[bool, ...], bool]]:
    pots = tuple((c == "#" for c in inp[0].strip().split()[-1]))
    patterns = {
        tuple(
            (c == "#" for c in line.strip().split(" => ")[0])
        ): line.strip().split(" => ")[1] == "#"
        for line in inp[2:]
    }
    return pots, patterns


def part1(inp: tuple[tuple[bool, ...], dict[tuple[bool, ...], bool]]):
    pots, patterns = inp
    offset = 0
    for _ in range(20):
        pots = (False, False, False, False, *pots, False, False, False, False)
        offset -= 2
        pots = tuple(
            (
                patterns[window]
                for window in mit.windowed(pots, 5, fillvalue=False)
            )
        )
        while not pots[0]:
            pots = pots[1:]
            offset += 1
        while not pots[-1]:
            pots = pots[:-1]
    return sum((i + offset for i, pot in enumerate(pots) if pot))


def part2(inp: tuple[tuple[bool, ...], dict[tuple[bool, ...], bool]]):
    pots, patterns = inp
    offset = 0
    for i in range(ITERS):
        print(i, end="\r")
        oldpots = pots
        oldoffset = offset
        pots = tuple(
            (
                patterns[window]
                for window in mit.windowed(
                    (
                        False,
                        False,
                        False,
                        False,
                        *pots,
                        False,
                        False,
                        False,
                        False,
                    ),
                    5,
                    fillvalue=False,
                )
            )
        )
        offset -= 2
        while not pots[0]:
            pots = pots[1:]
            offset += 1
        while not pots[-1]:
            pots = pots[:-1]
        if oldpots == pots:
            offset += (offset - oldoffset) * (ITERS - i - 1)
            break
    return sum((i + offset for i, pot in enumerate(pots) if pot))


if __name__ == "__main__":
    inp = parse(sys.stdin.readlines())

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
