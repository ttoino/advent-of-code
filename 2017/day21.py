import sys

import more_itertools as mit


def rotate_and_flip(pattern):
    for p in rotate(pattern):
        yield tuple(("".join(l) for l in p))
        yield tuple(("".join(l) for l in reversed(p)))
        yield tuple(("".join(reversed(l)) for l in p))


def rotate(pattern):
    yield pattern
    for i in range(3):
        pattern = list(zip(*reversed(pattern)))
        yield pattern


def parse(lines: list[str]) -> dict[tuple[str, ...], tuple[str, ...]]:
    return {
        k: tuple(line.strip().split(" => ")[1].split("/"))
        for line in lines
        for k in rotate_and_flip(line.split(" => ")[0].split("/"))
    }


def part1(instructions: dict[tuple[str, ...], tuple[str, ...]]) -> int:
    pattern = ".#...####"
    size = 3
    for i in range(5):
        t = 2 + size % 2
        a = size // t
        pieces = (
            tuple(("".join(i) for i in l))
            for l in sum(
                (
                    list(zip(*mit.chunked(l, a)))
                    for l in mit.chunked(mit.chunked(pattern, t), size)
                ),
                start=[],
            )
        )
        new_pieces = list((instructions[p] for p in pieces))
        size += size // t
        pattern = "".join(
            ("".join(i) for l in mit.chunked(new_pieces, a) for i in zip(*l))
        )
        assert len(pattern) == size * size
    return pattern.count("#")


def part2(instructions: dict[tuple[str, ...], tuple[str, ...]]) -> int:
    pattern = ".#...####"
    size = 3
    for i in range(18):
        t = 2 + size % 2
        a = size // t
        pieces = (
            tuple(("".join(i) for i in l))
            for l in sum(
                (
                    list(zip(*mit.chunked(l, a)))
                    for l in mit.chunked(mit.chunked(pattern, t), size)
                ),
                start=[],
            )
        )
        new_pieces = list((instructions[p] for p in pieces))
        size += size // t
        pattern = "".join(
            ("".join(i) for l in mit.chunked(new_pieces, a) for i in zip(*l))
        )
        assert len(pattern) == size * size
    return pattern.count("#")


if __name__ == "__main__":
    instructions = parse(sys.stdin.read().splitlines())

    print(f"Part 1: {part1(instructions)}")
    print(f"Part 2: {part2(instructions)}")
