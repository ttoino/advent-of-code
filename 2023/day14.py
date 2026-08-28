import sys


def solve(inp: list[str]) -> int:
    rocks = inp
    for y, line in enumerate(rocks):
        for x, rock in enumerate(line):
            if rock != "O":
                continue
            new_y = y
            while new_y > 0 and rocks[new_y - 1][x] == ".":
                new_y -= 1
            rocks[y] = rocks[y][:x] + "." + rocks[y][x + 1 :]
            rocks[new_y] = rocks[new_y][:x] + "O" + rocks[new_y][x + 1 :]
    result = 0
    for i, line in enumerate(rocks[::-1]):
        result += line.count("O") * (i + 1)
    return result


if __name__ == "__main__":
    inp = [line.strip() for line in sys.stdin.readlines()]

    print(f"Solution: {solve(inp)}")
