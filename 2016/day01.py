import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    dir_map = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction = 0
    pos = 0, 0

    for i in inf.readline().strip().split(", "):
        direction += (i[0] == "R") - (i[0] == "L")
        amount = int(i[1:])
        d = dir_map[direction % 4]
        pos = pos[0] + d[0] * amount, pos[1] + d[1] * amount

    outf.write(str(abs(pos[0]) + abs(pos[1])))
