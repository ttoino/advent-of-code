import sys



DIRS = {'R': (1, 0), 'L': (-1, 0), 'U': (0, -1), 'D': (0, 1)}


def sign(x: int):
    return x and x // abs(x)


def parse(s: str) -> list[tuple[str, int]]:
    return [(dir, int(amount)) for dir, amount in (line.split() for line in s.splitlines())]


def part1(inp: list[tuple[str, int]]):
    tail_pos = (0, 0)
    head_pos = (0, 0)
    tail_poss = set()
    for dir, amount in inp:
        d = DIRS[dir]
        for _ in range(amount):
            head_pos = (head_pos[0] + d[0], head_pos[1] + d[1])
            tail_d = (head_pos[0] - tail_pos[0], head_pos[1] - tail_pos[1])
            if abs(tail_d[0]) > 1 or abs(tail_d[1]) > 1:
                tail_pos = (tail_pos[0] + sign(tail_d[0]), tail_pos[1] + sign(tail_d[1]))
            tail_poss.add(tail_pos)
    return len(tail_poss)


def part2(inp: list[tuple[str, int]]):
    pos = [(0, 0) for _ in range(10)]
    tail_poss = set()
    for dir, amount in inp:
        d = DIRS[dir]
        for _ in range(amount):
            for j, p in enumerate(pos):
                if j == 0:
                    pos[j] = (p[0] + d[0], p[1] + d[1])
                else:
                    d2 = (pos[j - 1][0] - p[0], pos[j - 1][1] - p[1])
                    if abs(d2[0]) > 1 or abs(d2[1]) > 1:
                        pos[j] = (p[0] + sign(d2[0]), p[1] + sign(d2[1]))
            tail_poss.add(pos[-1])
    return len(tail_poss)


if __name__ == "__main__":
    inp = parse(sys.stdin.read())

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
