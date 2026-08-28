import sys


def get_paths(path: list[str], graph: dict[str, set[str]]):
    current = path[-1]
    if current == 'end':
        return 1
    if current.islower():
        graph = {k: v - {current} for k, v in graph.items()}
    return sum((get_paths(path + [n], graph) for n in graph[current]))


def get_paths_p2(path: list[str], graph: dict[str, set[str]], visited_twice: bool):
    current = path[-1]
    if current == 'end':
        return 1
    if len(graph['end']) == 0:
        return 0
    if current.islower():
        if current.endswith(' '):
            visited_twice = True
            graph = {k: {x for x in v if not x.endswith(' ')} for k, v in graph.items()}
        elif visited_twice or current == 'start':
            graph = {k: v - {current} for k, v in graph.items()}
        else:
            graph = {k: {x + ' ' if x == current else x for x in v} for k, v in graph.items()}
    return sum((get_paths_p2(path + [n], graph, visited_twice) for n in graph[current.strip()]))


def parse(inp: str) -> dict[str, set[str]]:
    graph = dict()
    for l in inp.splitlines():
        n1, n2 = l.strip().split('-')
        if n1 not in graph:
            graph[n1] = set()
        if n2 not in graph:
            graph[n2] = set()
        graph[n1].add(n2)
        graph[n2].add(n1)
    return graph


def part1(inp: dict[str, set[str]]) -> int:
    return get_paths(['start'], inp)


def part2(inp: dict[str, set[str]]) -> int:
    return get_paths_p2(['start'], inp, False)


if __name__ == "__main__":
    inp = parse(sys.stdin.read())

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
