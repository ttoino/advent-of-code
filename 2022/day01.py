import sys



def parse(s: str) -> list[int]:
    return [sum(map(int, e.splitlines())) for e in s.split('\n\n')]


def part1(inp: list[int]):
    return max(inp)


def part2(inp: list[int]):
    return sum(sorted(inp)[-3:])


if __name__ == "__main__":
    inp = parse(sys.stdin.read())

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
