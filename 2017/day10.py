import functools as ft
import operator as op

import more_itertools as mit


def part1(inp: str) -> int:
    l = list(range(256))
    skip_size = 0
    index = 0
    for i in inp.split(","):
        i = int(i)
        l[:i] = l[:i][::-1]
        l = l[(i + skip_size) % 256 :] + l[: (i + skip_size) % 256]
        index += i + skip_size
        skip_size += 1
    index %= 256
    l = l[-index:] + l[:-index]
    return l[0] * l[1]


def part2(inp: str) -> str:
    lengths = [ord(i) for i in inp] + [17, 31, 73, 47, 23]
    l = list(range(256))
    skip_size = 0
    index = 0
    for _ in range(64):
        for i in lengths:
            i = int(i)
            l[:i] = l[:i][::-1]
            l = l[(i + skip_size) % 256 :] + l[: (i + skip_size) % 256]
            index += i + skip_size
            skip_size += 1
    index %= 256
    l = l[-index:] + l[:-index]
    return "".join((f"{ft.reduce(op.xor, c):02x}" for c in mit.chunked(l, 16)))


if __name__ == "__main__":
    inp = input().strip()

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
