import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter
from string import ascii_lowercase

p1 = re.compile(r"([a-z])\1")


def is_valid(n: str) -> bool:
    b = False
    for c1, c2, c3 in mit.sliding_window(n, 3):
        b = b or (ord(c1) == ord(c2) - 1 and ord(c2) == ord(c3) - 1)

    return b and 'i' not in n and 'o' not in n and 'l' not in n and len(
        p1.findall(n)) >= 2


def to_int(n: str) -> int:
    return sum((ord(c) - ord('a')) * (26**i) for i, c in enumerate(n[::-1]))


def to_str(n: int) -> str:
    return "".join(ascii_lowercase[(n // 26**i) % 26] for i in range(7, -1, -1))


with open("input") as inf, open("part2.out", "w+") as outf:
    n = inf.readline().strip()
    b = False

    for i in it.count(to_int(n) + 1):
        i = to_str(i)
        if is_valid(i):
            if b:
                outf.write(i)
                break
            else:
                b = True
