import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part2.out", "w+") as outf:
    dir_map = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction = 0
    pos = 0, 0
    visited = {pos}

    for i in inf.readline().strip().split(", "):
        direction += (i[0] == "R") - (i[0] == "L")
        amount = int(i[1:])
        d = dir_map[direction % 4]
        for _ in range(amount):
            pos = pos[0] + d[0], pos[1] + d[1]
            if pos in visited:
                outf.write(str(abs(pos[0]) + abs(pos[1])))
                exit()
            visited.add(pos)
