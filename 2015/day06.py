import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    a = [False for i in range(1000 * 1000)]

    for i in inf:
        action, start, _, end = i.removeprefix("turn ").split()
        sx, sy = map(int, start.split(","))
        ex, ey = map(int, end.split(","))

        for x in range(sx, ex + 1):
            for y in range(sy, ey + 1):
                match action:
                    case "on":
                        a[x + y * 1000] = True
                    case "off":
                        a[x + y * 1000] = False
                    case "toggle":
                        a[x + y * 1000] = not a[x + y * 1000]
    
    outf.write(str(sum(a)))
