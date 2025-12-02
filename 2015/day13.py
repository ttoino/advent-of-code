import itertools as it
import sys


def get_input():
    graph: dict[str, dict[str, int]] = {}

    for i in sys.stdin.readlines():
        i = i.strip().removesuffix(".").split()
        a, b, np, h = i[0], i[-1], i[2], i[3]
        h = int(h)
        graph.setdefault(a, {})
        graph[a][b] = h if np == "gain" else -h

    return graph


def part1(graph: dict[str, dict[str, int]]):
    nodes = iter(graph)
    starting_node = next(nodes)
    best = -100000

    for p in it.permutations(nodes):
        p = (starting_node,) + p + (starting_node,)
        best = max(best, sum(graph[a][b] + graph[b][a] for a, b in it.pairwise(p)))

    return best


def part2(graph: dict[str, dict[str, int]]):
    return max(
        sum(graph[a][b] + graph[b][a] for a, b in it.pairwise(p))
        for p in it.permutations(graph)
    )


if __name__ == "__main__":
    graph = get_input()

    print(f"Part 1: {part1(graph)}")
    print(f"Part 2: {part2(graph)}")
