import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part2.out", "w+") as outf:
    graph = {}
    for i in inf:
        i = i.strip().removesuffix(".").split()
        a, b, np, h = i[0], i[-1], i[2], i[3]
        h = int(h)
        graph.setdefault(a, {})
        graph[a][b] = h if np == "gain" else -h

    outf.write(
        str(
            max(
                sum(graph[a][b] + graph[b][a]
                    for a, b in it.pairwise(p))
                for p in it.permutations(graph))))
