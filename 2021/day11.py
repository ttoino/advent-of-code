import itertools as it
import sys


def part1(inp: list[list[int]]) -> int:
    octopi = [list(line) for line in inp]
    w = len(octopi[0])
    h = len(octopi)
    result = 0
    for i in range(100):
        flashed: set[tuple[int, int]] = set()
        octopi = [[o + 1 for o in l] for l in octopi]
        f = True
        while f:
            f = False
            for x, y in it.product(range(w), range(h)):
                if octopi[y][x] > 9 and (x, y) not in flashed:
                    flashed.add((x, y))
                    f = True
                    for dx, dy in it.product(range(-1, 2), range(-1, 2)):
                        nx, ny = (x + dx, y + dy)
                        if 0 <= nx < w and 0 <= ny < h:
                            octopi[ny][nx] += 1
        octopi = [[0 if o > 9 else o for o in l] for l in octopi]
        result += len(flashed)
    return result


def part2(inp: list[list[int]]) -> int:
    octopi = [list(line) for line in inp]
    w = len(octopi[0])
    h = len(octopi)
    result = 0
    for i in it.count(1):
        flashed: set[tuple[int, int]] = set()
        octopi = [[o + 1 for o in l] for l in octopi]
        f = True
        while f:
            f = False
            for x, y in it.product(range(w), range(h)):
                if octopi[y][x] > 9 and (x, y) not in flashed:
                    flashed.add((x, y))
                    f = True
                    for dx, dy in it.product(range(-1, 2), range(-1, 2)):
                        nx, ny = (x + dx, y + dy)
                        if 0 <= nx < w and 0 <= ny < h:
                            octopi[ny][nx] += 1
        octopi = [[0 if o > 9 else o for o in l] for l in octopi]
        if len(flashed) == w * h:
            result = i
            break
    return result


if __name__ == "__main__":
    inp = [list(map(int, line.strip())) for line in sys.stdin]

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
