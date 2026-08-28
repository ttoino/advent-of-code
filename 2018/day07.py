import sys

import functools as ft
import heapq as hq
import itertools as it
import operator as op
from collections import defaultdict


def parse(inp: list[str]) -> dict[str, set[str]]:
    graph = defaultdict(set)
    for i in inp:
        a = i.split()
        graph[a[1]].add(a[7])
    return graph


def part1(inp: dict[str, set[str]]):
    graph = defaultdict(set, {k: set(v) for k, v in inp.items()})

    def not_ready():
        return ft.reduce(op.or_, graph.values(), set())
    q = list(graph.keys() - not_ready())
    hq.heapify(q)
    result = ''
    while len(q) > 0:
        n = hq.heappop(q)
        result += n
        edges = graph[n]
        del graph[n]
        for o in edges:
            if o not in not_ready():
                hq.heappush(q, o)
    return result


def part2(inp: dict[str, set[str]]):
    graph = defaultdict(set, {k: set(v) for k, v in inp.items()})

    def not_ready():
        return ft.reduce(op.or_, graph.values(), set())
    q = list(graph.keys() - not_ready())
    hq.heapify(q)
    visited = set()
    workers = [(None, 0) for _ in range(5)]
    for second in it.count():
        for i, (n, t) in enumerate(workers):
            if n is None:
                continue
            workers[i] = (n, t + 1)
            if t == 60 + ord(n) - ord('A'):
                edges = graph[n]
                del graph[n]
                for o in edges:
                    if o not in not_ready():
                        hq.heappush(q, o)
                workers[i] = (None, 0)
        free_workers = len([w for w in workers if w[0] is None])
        if free_workers == 5 and len(q) == 0:
            return second
        while len(q) > 0 and free_workers > 0:
            n = hq.heappop(q)
            for i, worker in enumerate(workers):
                if worker[0] is None:
                    workers[i] = (n, 0)
                    free_workers -= 1
                    break


if __name__ == "__main__":
    inp = parse(sys.stdin.readlines())

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
