import sys
from math import ceil, sqrt


def part1(inp: int) -> int:
    n = inp
    s = ceil(sqrt(n))
    s += s % 2 == 0
    i = n - (s - 2) ** 2
    i %= s**2 - (s - 2) ** 2
    return i


def part2(inp: int) -> int:
    n = inp
    d = {(0, 0): 1}
    current = (0, 0)
    dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    while True:
        current = (current[0] + 1, current[1])
        d[current] = sum(
            (
                d.get((current[0] + dx, current[1] + dy), 0)
                for dx in range(-1, 2)
                for dy in range(-1, 2)
            )
        )
        if d[current] > n:
            return d[current]
        for i in range(4):
            while True:
                current = (current[0] + dirs[i][0], current[1] + dirs[i][1])
                d[current] = sum(
                    (
                        d.get((current[0] + dx, current[1] + dy), 0)
                        for dx in range(-1, 2)
                        for dy in range(-1, 2)
                    )
                )
                if d[current] > n:
                    return d[current]
                if abs(current[0]) == abs(current[1]):
                    break


if __name__ == "__main__":
    inp = int(sys.stdin.readline())

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
