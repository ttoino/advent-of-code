import itertools as it
from time import sleep
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter


def print_code(code):
    print("\x1b[H\x1b[J" + "\n".join("".join("#" if c else " " for c in line) for line in mit.chunked(code, 50)))
    sleep(.1)


def get(code: list, x: int, y: int):
    return code[(x % 50) + (y % 6) * 50]


def set(code: list, x: int, y: int, v):
    code[(x % 50) + (y % 6) * 50] = v


with open("input") as inf, open("part2.out", "w+") as outf:
    p = re.compile(r" |=")

    code = [0 for _ in range(50 * 6)]

    for i in inf:
        new_code = [i for i in code]
        match p.split(i.strip()):
            case ["rect", size]:
                w, h = map(int, size.split("x"))
                for x in range(w):
                    for y in range(h):
                        set(new_code, x, y, 1)
            case ["rotate", "row", "y", y, "by", b]:
                y = int(y)
                b = int(b)
                for x in range(50):
                    set(new_code, x, y, get(code, x - b, y))
            case ["rotate", "column", "x", x, "by", b]:
                x = int(x)
                b = int(b)
                for y in range(6):
                    set(new_code, x, y, get(code, x, y - b))
        code = new_code
        print_code(code)


    outf.write(input("What is the code? "))
