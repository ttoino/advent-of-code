import sys

import re


FONT = {
    "●●●●\n●\n●●●\n●\n●\n●●●●": "E",
    " ●●\n●  ●\n●  ●\n●●●●\n●  ●\n●  ●": "A",
    "●  ●\n●  ●\n●●●●\n●  ●\n●  ●\n●  ●": "H",
    "●  ●\n● ●\n●●\n● ●\n● ●\n●  ●": "K",
    "●●●\n●  ●\n●  ●\n●●●\n● ●\n●  ●": "R",
    " ●●\n●  ●\n●\n●\n●  ●\n ●●": "C",
    "●●●\n●  ●\n●  ●\n●●●\n●\n●": "P",
}


def ocr(paper: str) -> str:
    lines = [line.rstrip() for line in paper.splitlines()]
    width = max(len(l) for l in lines)
    empty_cols = [all(len(l) <= c or l[c] == " " for l in lines) for c in range(width)]

    letters = []
    start = 0
    for c in range(width):
        if empty_cols[c]:
            if c > start:
                block = "\n".join(l[start:c].rstrip() for l in lines)
                letters.append(FONT.get(block, "?"))
            start = c + 1
    if start < width:
        block = "\n".join(l[start:].rstrip() for l in lines)
        letters.append(FONT.get(block, "?"))

    return "".join(letters)


def print_paper(points: set[tuple[int, int]]) -> str:
    max_x, max_y = map(max, zip(*points))
    lines = []
    for y in range(max_y + 1):
        line = []
        for x in range(max_x + 1):
            line.append("●" if (x, y) in points else " ")
        lines.append("".join(line))
    return "\n".join(lines)


def parse(inp: str) -> tuple[set[tuple[int, int]], list[tuple[bool, int]]]:
    lines = inp.splitlines()
    points = set()
    folds = []
    regex = re.compile(r"fold along (x|y)=(\d+)")
    parsing_points = True
    for line in lines:
        if not line:
            parsing_points = False
            continue
        if parsing_points:
            points.add(tuple(map(int, line.split(","))))
        else:
            m = regex.match(line)
            folds.append((m.group(1) == "x", int(m.group(2))))
    return points, folds


def part1(inp: tuple[set[tuple[int, int]], list[tuple[bool, int]]]) -> int:
    points, folds = inp
    axis, coord = folds[0]
    points = {(x, y) for x, y in points if (x if axis else y) < coord} | {
        (2 * coord - x if axis else x, 2 * coord - y if not axis else y)
        for x, y in points
        if (x if axis else y) > coord
    }
    return len(points)


def part2(inp: tuple[set[tuple[int, int]], list[tuple[bool, int]]]) -> str:
    points, folds = inp
    for axis, coord in folds:
        points = {(x, y) for x, y in points if (x if axis else y) < coord} | {
            (2 * coord - x if axis else x, 2 * coord - y if not axis else y)
            for x, y in points
            if (x if axis else y) > coord
        }
    return ocr(print_paper(points))


if __name__ == "__main__":
    inp = parse(sys.stdin.read())

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
