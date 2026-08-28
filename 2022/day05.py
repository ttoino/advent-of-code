import sys


def parse(s: str) -> tuple[list[list[str]], list[tuple[int, int, int]]]:
    crates_inp, instructions = s.split("\n\n")
    crates_inp = reversed(crates_inp.splitlines()[:-1])
    crates = [list() for _ in range(9)]
    for l in crates_inp:
        for i, c in enumerate(crates):
            crate = l[i * 4 + 1]
            if crate != " ":
                c.append(crate)
    moves = []
    for i in instructions.splitlines():
        _, count, _, start, _, end = i.split()
        moves.append((int(count), int(start), int(end)))
    return crates, moves


def part1(inp: tuple[list[list[str]], list[tuple[int, int, int]]]):
    crates, moves = inp
    crates = [list(c) for c in crates]
    for count, start, end in moves:
        for _ in range(count):
            crates[end - 1].append(crates[start - 1].pop())
    return "".join((c[-1] for c in crates))


def part2(inp: tuple[list[list[str]], list[tuple[int, int, int]]]):
    crates, moves = inp
    crates = [list(c) for c in crates]
    for count, start, end in moves:
        crates[end - 1].extend(crates[start - 1][-count:])
        for _ in range(count):
            crates[start - 1].pop()
    return "".join((c[-1] for c in crates))


if __name__ == "__main__":
    inp = parse(sys.stdin.read())

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
