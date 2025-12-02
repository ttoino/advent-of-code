import sys


def get_neighbors(i, grid):
    x, y = i % 100, i // 100
    return (
        (x != 0 and y != 0 and grid[i - 101] == "#")
        + (y != 0 and grid[i - 100] == "#")
        + (x != 99 and y != 0 and grid[i - 99] == "#")
        + (x != 0 and grid[i - 1] == "#")
        + (x != 99 and grid[i + 1] == "#")
        + (x != 0 and y != 99 and grid[i + 99] == "#")
        + (y != 99 and grid[i + 100] == "#")
        + (x != 99 and y != 99 and grid[i + 101] == "#")
    )


def solve(grid: list[str], part: int):
    for _ in range(100):
        if part == 1:
            grid = [
                "#"
                if (n := get_neighbors(i, grid)) == 3 or (n == 2 and c == "#")
                else "."
                for i, c in enumerate(grid)
            ]
        else:
            grid = [
                "#"
                if i == 0
                or i == 99
                or i == 9900
                or i == 9999
                or (n := get_neighbors(i, grid)) == 3
                or (n == 2 and c == "#")
                else "."
                for i, c in enumerate(grid)
            ]

    return grid.count("#")


if __name__ == "__main__":
    grid = [i for l in sys.stdin.readlines() for i in l.strip()]

    print(f"Part 1: {solve(grid.copy(), 1)}")
    print(f"Part 2: {solve(grid.copy(), 2)}")
