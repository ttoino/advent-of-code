import itertools as it
import sys


def part1(inp: int):
    serial_number = inp
    d = {}
    max_power = 0
    coords = (0, 0)
    for x, y in list(it.product(range(1, 301), range(1, 301)))[::-1]:
        d[x, y] = ((x + 10) * y + serial_number) * (x + 10) // 100 % 10 - 5
        if x <= 298 and y <= 298:
            power = sum(
                (d[x + px, y + py] for px in range(3) for py in range(3))
            )
            if power > max_power:
                max_power = power
                coords = (x, y)
    return f"{coords[0]},{coords[1]}"


def part2(inp: int):
    serial_number = inp
    d = {}
    max_power = 0
    coords = (0, 0, 0)
    for size in range(1, 31):
        print(size, end="\r")
        for x, y in it.product(range(1, 302 - size), range(1, 302 - size)):
            if size == 1:
                d[x, y, size] = ((x + 10) * y + serial_number) * (
                    x + 10
                ) // 100 % 10 - 5
            else:
                d[x, y, size] = (
                    d[x, y, size - 1]
                    + sum((d[x + dx, y + size - 1, 1] for dx in range(size)))
                    + sum((d[x + size - 1, y + dy, 1] for dy in range(size)))
                    - d[x + size - 1, y + size - 1, 1]
                )
            if d[x, y, size] > max_power:
                max_power = d[x, y, size]
                coords = (x, y, size)
    return f"{coords[0]},{coords[1]},{coords[2]}"


if __name__ == "__main__":
    inp = int(sys.stdin.readline().strip())

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
