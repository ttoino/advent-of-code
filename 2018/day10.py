import itertools as it
import re
import sys

import more_itertools as mit

FONT = {
    "#    #\n#    #\n #  #\n #  #\n  ##\n  ##\n #  #\n #  #\n#    #\n#    #": "X",
    "#####\n#    #\n#    #\n#    #\n#####\n#\n#\n#\n#\n#": "P",
    "######\n#\n#\n#\n#####\n#\n#\n#\n#\n#": "F",
    "#    #\n#   #\n#  #\n# #\n##\n##\n# #\n#  #\n#   #\n#    #": "K",
    "#\n#\n#\n#\n#\n#\n#\n#\n#\n######": "L",
}


def ocr(message: str) -> str:
    lines = [line.rstrip() for line in message.splitlines()]
    # Find columns that are entirely spaces
    width = max(len(l) for l in lines)
    empty_cols = [
        all(len(l) <= c or l[c] == " " for l in lines) for c in range(width)
    ]

    # Split into letter blocks
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


def part1(inp: list[tuple[int, int, int, int]]):
    points = [list(p) for p in inp]
    while True:
        min_x = 1000000
        min_y = 1000000
        max_x = -1000000
        max_y = -1000000
        for i, (x, y, vx, vy) in enumerate(points):
            points[i] = [x + vx, y + vy, vx, vy]
            min_y = min(min_y, y + vy)
            min_x = min(min_x, x + vx)
            max_y = max(max_y, y + vy)
            max_x = max(max_x, x + vx)
        w = max_x - min_x + 1
        h = max_y - min_y + 1
        if max_y - min_y <= 10:
            message = [" " for _ in range(w * h)]
            for x, y, _, _ in points:
                x -= min_x
                y -= min_y
                message[x + y * w] = "#"
            return ocr("\n".join("".join(l) for l in mit.chunked(message, w)))


def part2(inp: list[tuple[int, int, int, int]]):
    points = [list(p) for p in inp]
    for s in it.count():
        min_x = 1000000
        min_y = 1000000
        max_x = -1000000
        max_y = -1000000
        for i, (x, y, vx, vy) in enumerate(points):
            points[i] = [x + vx, y + vy, vx, vy]
            min_y = min(min_y, y + vy)
            min_x = min(min_x, x + vx)
            max_y = max(max_y, y + vy)
            max_x = max(max_x, x + vx)
        if max_y - min_y <= 10:
            return s + 1


if __name__ == "__main__":
    pattern = re.compile(
        "position=<\\s?(-?\\d+),\\s*(-?\\d+)> velocity=<\\s?(-?\\d+),\\s*(-?\\d+)>"
    )
    inp = [
        tuple(map(int, pattern.match(i).groups()))
        for i in sys.stdin.readlines()
    ]

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
