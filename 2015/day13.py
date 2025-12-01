import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    graph = {}
    for i in inf:
        i = i.strip().removesuffix(".").split()
        a, b, np, h = i[0], i[-1], i[2], i[3]
        h = int(h)
        graph.setdefault(a, {})
        graph[a][b] = h if np == "gain" else -h

    nodes = iter(graph)
    starting_node = next(nodes)
    best = -100000
    for p in it.permutations(nodes):
        p = (starting_node,) + p + (starting_node,)
        best = max(best,
                   sum(graph[a][b] + graph[b][a] for a, b in it.pairwise(p)))

    outf.write(str(best))
