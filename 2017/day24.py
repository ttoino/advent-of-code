import sys


def brute_force(
    components: set[tuple[int, int]], n: int = 0, total: int = 0
) -> int:
    available = {c for c in components if n in c}
    if len(available) == 0:
        return total
    return max(
        (
            brute_force(
                components - {c}, c[0] if c[1] == n else c[1], total + sum(c)
            )
            for c in available
        )
    )


def part1(inp: set[tuple[int, int]]) -> int:
    return brute_force(inp)


def brute_force_length(
    components: set[tuple[int, int]],
    n: int = 0,
    total: int = 0,
    length: int = 0,
) -> tuple[int, int]:
    available = {c for c in components if n in c}
    if len(available) == 0:
        return (length, total)
    return max(
        (
            brute_force_length(
                components - {c},
                c[0] if c[1] == n else c[1],
                total + sum(c),
                length + 1,
            )
            for c in available
        )
    )


def part2(inp: set[tuple[int, int]]) -> int:
    return brute_force_length(inp)[1]


if __name__ == "__main__":
    inp = {
        tuple(map(int, line.split("/")))
        for line in sys.stdin.read().splitlines()
    }

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
