import sys
from collections import deque


def part1(inp: list[list[int]]) -> int:
    graph = inp
    q = deque([0])
    visited = set()
    while len(q) > 0:
        n = q.pop()
        if n in visited:
            continue
        visited.add(n)
        q.extend(graph[n])
    return len(visited)


def part2(inp: list[list[int]]) -> int:
    graph = inp
    ng = 0
    nodes = set(range(len(graph)))
    while len(nodes) > 0:
        ng += 1
        q = deque([next(iter(nodes))])
        visited = set()
        while len(q) > 0:
            n = q.pop()
            if n in visited:
                continue
            visited.add(n)
            q.extend(graph[n])
        nodes -= visited
    return ng


if __name__ == "__main__":
    inp = [[int(n) for n in line.split(' <-> ')[1].split(', ')] for line in sys.stdin.read().splitlines()]

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
