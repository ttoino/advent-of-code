def add_tuples(a, b):
    return tuple((i + j for i, j in zip(a, b)))


def part1(inp: list[str]) -> int:
    current = (0, 0, 0)
    dirs = {'n': (0, -1, 1), 'ne': (1, -1, 0), 'se': (1, 0, -1), 's': (0, 1, -1), 'sw': (-1, 1, 0), 'nw': (-1, 0, 1)}
    for d in inp:
        current = add_tuples(current, dirs[d])
    return (abs(current[0]) + abs(current[1]) + abs(current[2])) // 2


def part2(inp: list[str]) -> int:
    current = (0, 0, 0)
    furthest = 0
    dirs = {'n': (0, -1, 1), 'ne': (1, -1, 0), 'se': (1, 0, -1), 's': (0, 1, -1), 'sw': (-1, 1, 0), 'nw': (-1, 0, 1)}
    for d in inp:
        current = add_tuples(current, dirs[d])
        furthest = max(furthest, (abs(current[0]) + abs(current[1]) + abs(current[2])) // 2)
    return furthest


if __name__ == "__main__":
    inp = input().strip().split(',')

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
