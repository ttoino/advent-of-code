import sys


def part1(inp: list[list[str]]) -> int:
    return sum((len(set(a)) == len(a) for a in inp))


def part2(inp: list[list[str]]) -> int:
    return sum(
        (
            len(set(a)) == len(a)
            for a in (["".join(sorted(x)) for x in line] for line in inp)
        )
    )


if __name__ == "__main__":
    inp = [line.split() for line in sys.stdin.read().splitlines()]

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
