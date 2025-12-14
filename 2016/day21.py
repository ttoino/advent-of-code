import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    s = list("abcdefgh")

    for i in inf:
        match i.strip().split():
            case ["swap", "position", x, "with", "position", y]:
                x = int(x)
                y = int(y)
                s[x], s[y] = s[y], s[x]
            case ["swap", "letter", x, "with", "letter", y]:
                x = s.index(x)
                y = s.index(y)
                s[x], s[y] = s[y], s[x]
            case ["rotate", "left", x, "steps" | "step"]:
                x = int(x)
                s = s[x:] + s[:x]
            case ["rotate", "right", x, "steps" | "step"]:
                x = int(x)
                s = s[-x:] + s[:-x]
            case ["rotate", "based", "on", "position", "of", "letter", x]:
                x = s.index(x)
                x = (1 + x + (x >= 4)) % len(s)
                s = s[-x:] + s[:-x]
            case ["reverse", "positions", x, "through", y]:
                x = int(x)
                y = int(y)
                x, y = min(x, y), max(x, y)
                s[x:y+1] = s[x:y+1][::-1]
            case ["move", "position", x, "to", "position", y]:
                x = int(x)
                y = int(y)
                c = s[x]
                del s[x]
                s.insert(y, c)
    
    outf.write("".join(s))
