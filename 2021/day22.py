import itertools as it
import re
import sys


def parse(inp: str) -> list[tuple[int, int, int, int, int, int, str]]:
    regex = re.compile(
        r"(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)"
    )
    return [
        (*map(int, m.group(2, 3, 4, 5, 6, 7)), m.group(1))
        for m in (regex.match(s) for s in inp.splitlines())
        if m
    ]


def solve(inp: list[tuple[int, int, int, int, int, int, str]]) -> int:
    cubes = set()
    for line in inp:
        min_x, max_x, min_y, max_y, min_z, max_z, action = line
        if (
            min_x > 50
            or min_y > 50
            or min_z > 50
            or (max_x < -50)
            or (max_y < -50)
            or (max_z < -50)
        ):
            continue
        new_cubes = set(
            it.product(
                range(min_x, max_x + 1),
                range(min_y, max_y + 1),
                range(min_z, max_z + 1),
            )
        )
        if action == "on":
            cubes |= new_cubes
        else:
            cubes -= new_cubes
    return len(cubes)


if __name__ == "__main__":
    inp = parse(sys.stdin.read())

    print(f"Solution: {solve(inp)}")
