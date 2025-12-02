import sys


def solve(reindeer: list[tuple[int, int, int]]):
    dists = [0 for i in range(len(reindeer))]
    points = [0 for i in range(len(reindeer))]
    rest = [-t for _, t, _ in reindeer]

    for _ in range(2503):
        for i, (s, t, r) in enumerate(reindeer):
            if rest[i] < 0:
                dists[i] += s
            rest[i] += 1
            if rest[i] == r:
                rest[i] = -t

        m = max(dists)
        for i, d in enumerate(dists):
            if d == m:
                points[i] += 1

    return max(dists), max(points)


if __name__ == "__main__":
    reindeer = [
        (int(i[3]), int(i[6]), int(i[13]))
        for i in (i.split() for i in sys.stdin.readlines())
    ]

    part1, part2 = solve(reindeer)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
