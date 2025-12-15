import shutil
from time import sleep
import functools as ft
import heapq as hq


@ft.cache
def is_wall(x, y, n):
    return f"{x * x + 3 * x + 2 * x * y + y + y * y + n:b}".count("1") % 2


def part1(n: int) -> int:
    visited = set()
    heap = [(0, (1, 1))]

    while len(heap) > 0:
        d, p = hq.heappop(heap)

        if p in visited:
            continue

        visited.add(p)

        if p == (31, 39):
            return d

        for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
            if not is_wall(p[0] + dx, p[1] + dy, n):
                hq.heappush(heap, (d + 1, (p[0] + dx, p[1] + dy)))

    return -1


def part2(n: int) -> int:
    tw, th = shutil.get_terminal_size()

    print(
        "\n".join(
            "".join("#" if is_wall(x, y, n) else " " for x in range(tw))
            for y in range(th)
        ),
        end="",
    )

    visited = set()
    heap = [(0, (1, 1))]

    while len(heap) > 0:
        d, p = hq.heappop(heap)

        if p in visited or d > 50 or p[0] < 0 or p[1] < 0:
            continue

        print(f"\x1b[{p[1] + 1};{p[0] + 1}HO", end="", flush=True)
        sleep(0.1)

        visited.add(p)

        for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
            if not is_wall(p[0] + dx, p[1] + dy, n):
                hq.heappush(heap, (d + 1, (p[0] + dx, p[1] + dy)))

    print(f"\x1b[{th};{1}H")

    return len(visited)


if __name__ == "__main__":
    n = int(input())

    print(f"Part 1: {part1(n)}")
    print(f"Part 2: {part2(n)}")
