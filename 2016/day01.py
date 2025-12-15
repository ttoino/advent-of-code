dir_map = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def part1(inp: list[tuple[str, int]]) -> int:
    direction = 0
    x, y = 0, 0

    for d, amount in inp:
        direction += d == "R"
        direction -= d == "L"
        dx, dy = dir_map[direction % 4]

        x, y = x + dx * amount, y + dy * amount

    return abs(x) + abs(y)


def part2(inp: list[tuple[str, int]]) -> int:
    direction = 0
    x, y = 0, 0
    visited = {(x, y)}

    for d, amount in inp:
        direction += d == "R"
        direction -= d == "L"
        dx, dy = dir_map[direction % 4]

        for _ in range(amount):
            x, y = x + dx, y + dy

            if (x, y) in visited:
                return abs(x) + abs(y)

            visited.add((x, y))

    return -1


if __name__ == "__main__":
    inp = [(i[0], int(i[1:])) for i in input().strip().split(", ")]

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
