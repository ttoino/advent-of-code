import sys



def turn(them, us):
    them = ord(them) - ord('A') + 1
    us = ord(us) - ord('X') + 1
    score = (us - them + 1) % 3 * 3
    return us + score


def turn_p2(them, score):
    them = ord(them) - ord('A') + 1
    score = ord(score) - ord('X')
    us = (score + them + 1) % 3 + 1
    return us + score * 3


def parse(s: str) -> list[tuple[str, str]]:
    return [(i[0], i[2]) for i in s.splitlines()]


def part1(inp: list[tuple[str, str]]):
    return sum((turn(them, us) for them, us in inp))


def part2(inp: list[tuple[str, str]]):
    return sum((turn_p2(them, score) for them, score in inp))


if __name__ == "__main__":
    inp = parse(sys.stdin.read())

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
