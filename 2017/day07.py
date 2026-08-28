import re
import sys
from collections import Counter


class FoundAnswer(Exception):
    pass


def check_weight(towers, tower):
    weight, children = towers[tower]
    if children is None:
        return int(weight)
    weights = [check_weight(towers, c) for c in children]
    counter = Counter(weights)
    for k, v in counter.items():
        if v == 1:
            for w, c in zip(weights, children):
                if w == k:
                    raise FoundAnswer(
                        int(towers[c][0]) - k + counter.most_common(1)[0][0]
                    )
    return int(weight) + sum(weights)


def parse(lines: list[str]) -> dict[str, tuple[int, list[str] | None]]:
    p = re.compile(r"(\w+) \((\d+)\)(?: -> ((?:\w+,? ?)+))?")
    return {
        g[0]: (int(g[1]), g[2].split(", ") if g[2] else None)
        for line in lines
        if (g := p.match(line).groups())
    }


def find_root(towers: dict[str, tuple[int, list[str] | None]]) -> str:
    names = {
        name for name, (_, children) in towers.items() if children is not None
    }
    children = {
        c
        for _, (_, children) in towers.items()
        if children is not None
        for c in children
    }
    return next(iter(names - children))


def part1(towers: dict[str, tuple[int, list[str] | None]]) -> str:
    return find_root(towers)


def part2(towers: dict[str, tuple[int, list[str] | None]]) -> int:
    root = find_root(towers)
    try:
        check_weight(towers, root)
    except FoundAnswer as e:
        return e.args[0]


if __name__ == "__main__":
    inp = parse(sys.stdin.read().splitlines())

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
