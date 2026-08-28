import functools as ft
import operator as op
import sys


def parse(inp: str) -> list[tuple[list[str], list[str]]]:
    return [
        tuple(map(lambda x: x.split(), line.split("|")))
        for line in inp.splitlines()
    ]


def part1(inp: list[tuple[list[str], list[str]]]) -> int:
    easy_lens = (2, 3, 4, 7)
    lines = map(lambda x: x[1], inp)
    return ft.reduce(
        lambda x, y: x + (len(y) in easy_lens), ft.reduce(op.add, lines), 0
    )


def part2(inp: list[tuple[list[str], list[str]]]) -> int:
    o = 0
    for samples, outputs in inp:
        samples = sorted(samples, key=len)
        digits = {1: samples[0], 7: samples[1], 4: samples[2], 8: samples[-1]}
        len5 = samples[3:6]
        len6 = samples[6:-1]
        middle_bit = set(digits[4]) - set(digits[1])
        for i in len5:
            if set(i).issuperset(set(digits[1])):
                digits[3] = i
                len5.remove(i)
                break
        for i in len6:
            if set(i).issuperset(set(digits[3])):
                digits[9] = i
                len6.remove(i)
                break
        for i in len6:
            if set(i).issuperset(set(digits[1])):
                digits[0] = i
                len6.remove(i)
                break
        digits[6] = len6[0]
        for i in len5:
            if set(i).issubset(set(digits[6])):
                digits[5] = i
                len5.remove(i)
                break
        digits[2] = len5[0]
        digits = dict(((frozenset(y), str(x)) for x, y in digits.items()))
        o += int("".join((digits[frozenset(d)] for d in outputs)))
    return o


if __name__ == "__main__":
    inp = parse(sys.stdin.read())

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
