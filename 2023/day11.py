import sys

import itertools as it


def part1(inp: list[str]) -> int:
    universe = inp
    expanded_universe = []
    for line in universe:
        if all((c == '.' for c in line)):
            expanded_universe.append(line)
        expanded_universe.append(line)
    universe = zip(*expanded_universe)
    expanded_universe = []
    for line in universe:
        if all((c == '.' for c in line)):
            expanded_universe.append(line)
        expanded_universe.append(line)
    galaxies = set()
    for i, l in enumerate(expanded_universe):
        for j, c in enumerate(l):
            if c == '#':
                galaxies.add((i, j))
    result = 0
    for g1, g2 in it.combinations(galaxies, 2):
        result += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
    return result


def part2(inp: list[str]) -> int:
    universe = inp
    expanded_rows = []
    for i, line in enumerate(universe):
        if all((c == '.' for c in line)):
            expanded_rows.append(i)
    expanded_cols = []
    for i, line in enumerate(zip(*universe)):
        if all((c == '.' for c in line)):
            expanded_cols.append(i)
    galaxies = set()
    for i, l in enumerate(universe):
        for j, c in enumerate(l):
            if c == '#':
                galaxies.add((i, j))
    result = 0
    expansion = 1000000
    for (g1_i, g1_j), (g2_i, g2_j) in it.combinations(galaxies, 2):
        for i in range(min(g1_i, g2_i) + 1, max(g1_i, g2_i) + 1):
            result += expansion if i in expanded_rows else 1
        for j in range(min(g1_j, g2_j) + 1, max(g1_j, g2_j) + 1):
            result += expansion if j in expanded_cols else 1
    return result


if __name__ == "__main__":
    inp = [line.strip() for line in sys.stdin.readlines()]

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
