import itertools as it
import sys


def get_input():
    graph: dict[str, dict[str, int]] = {}

    for i in sys.stdin.readlines():
        start, _, end, _, dist = i.strip().split()

        graph.setdefault(start, {})
        graph.setdefault(end, {})

        graph[start][end] = int(dist)
        graph[end][start] = int(dist)

    return graph


def solve(graph: dict[str, dict[str, int]], part: int):
    m = 1000000000 if part == 1 else 0

    for p in it.permutations(graph.keys(), 8):
        s = 0
        for start, end in it.pairwise(p):
            s += graph[start][end]
        m = min(s, m) if part == 1 else max(s, m)

    return m


if __name__ == "__main__":
    graph = get_input()

    print(f"Part 1: {solve(graph, 1)}")
    print(f"Part 2: {solve(graph, 2)}")
