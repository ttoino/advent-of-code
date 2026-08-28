import re
import sys
from collections import Counter, defaultdict


def part1(inp: list[str]):
    pattern = re.compile(
        "\\[\\d{4}-\\d{2}-\\d{2} \\d{2}:(\\d{2})] (?:Guard #(\\d+) begins shift|(wakes up)|(falls asleep))"
    )
    l = sorted(inp)
    c = Counter()
    d = defaultdict(Counter)
    id = -1
    start = -1
    for i in l:
        match pattern.match(i).groups():
            case [mins, None, None, "falls asleep"]:
                start = int(mins)
            case [mins, None, "wakes up", None]:
                for m in range(start, int(mins)):
                    c[id] += 1
                    d[id][m] += 1
            case [_, _id, None, None]:
                id = int(_id)
    id = c.most_common(1)[0][0]
    return d[id].most_common(1)[0][0] * id


def part2(inp: list[str]):
    pattern = re.compile(
        "\\[\\d{4}-\\d{2}-\\d{2} \\d{2}:(\\d{2})] (?:Guard #(\\d+) begins shift|(wakes up)|(falls asleep))"
    )
    l = sorted(inp)
    c = Counter()
    id = -1
    start = -1
    for i in l:
        match pattern.match(i).groups():
            case [mins, None, None, "falls asleep"]:
                start = int(mins)
            case [mins, None, "wakes up", None]:
                for m in range(start, int(mins)):
                    c[id, m] += 1
            case [_, _id, None, None]:
                id = int(_id)
    id, m = c.most_common(1)[0][0]
    return id * m


if __name__ == "__main__":
    inp = sys.stdin.readlines()

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
