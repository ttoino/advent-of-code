import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    graph = {}

    for i in inf:
        start, _, end, _, dist = i.strip().split()

        graph.setdefault(start, {})
        graph.setdefault(end, {})

        graph[start][end] = int(dist)
        graph[end][start] = int(dist)

    m = 1000000000
    for p in it.permutations(graph.keys(), 8):
        s = 0
        for start, end in it.pairwise(p):
            s += graph[start][end]
        m = min(s, m)

    outf.write(str(m))
