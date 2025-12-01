import itertools as it
from time import sleep
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter


def get_neighbors(i, grid):
    x, y = i % 100, i // 100
    return (x != 0 and y != 0 and grid[i - 101] == '#') + (
        y != 0 and
        grid[i - 100] == '#') + (x != 99 and y != 0 and grid[i - 99] == '#') + (
            x != 0 and
            grid[i - 1] == '#') + (x != 99 and grid[i + 1] == '#') + (
                x != 0 and y != 99 and grid[i + 99] == '#') + (
                    y != 99 and grid[i + 100] == '#') + (x != 99 and y != 99 and
                                                         grid[i + 101] == '#')


def print_grid(grid):
    print("\x1b[H\x1b[J", end="")
    for i, c in enumerate(grid):
        print(c, end="")
        if i % 100 == 99:
            print()
    sleep(.25)


with open("input") as inf, open("part1.out", "w+") as outf:
    grid = [i for l in inf for i in l.strip()]
    # print_grid(grid)

    for _ in range(100):
        grid = [
            '#' if (n := get_neighbors(i, grid)) == 3 or
            (n == 2 and c == '#') else '.' for i, c in enumerate(grid)
        ]
        # print_grid(grid)

    outf.write(str(grid.count('#')))
