import sys



CYCLES = {20, 60, 100, 140, 180, 220}

FONT = {
    "████\n█\n███\n█\n█\n████": "E",
    "█  █\n█  █\n████\n█  █\n█  █\n█  █": "H",
    "████\n   █\n  █\n █\n█\n████": "Z",
    "████\n█\n███\n█\n█\n█": "F",
    " ██\n█  █\n█\n█\n█  █\n ██": "C",
}


def ocr(paper: str) -> str:
    lines = [line.rstrip() for line in paper.splitlines()]
    width = max(len(l) for l in lines)
    empty_cols = [all(len(l) <= c or l[c] == " " for l in lines) for c in range(width)]

    letters = []
    start = 0
    for c in range(width):
        if empty_cols[c]:
            if c > start:
                block = "\n".join(l[start:c].rstrip() for l in lines)
                letters.append(FONT.get(block, "?"))
            start = c + 1
    if start < width:
        block = "\n".join(l[start:].rstrip() for l in lines)
        letters.append(FONT.get(block, "?"))

    return "".join(letters)


def parse(s: str) -> list[str]:
    return s.splitlines()


def part1(inp: list[str]):
    x = 1
    cycle = 0
    vals = []

    def inc_cycle():
        nonlocal cycle
        cycle += 1
        if cycle in CYCLES:
            vals.append(cycle * x)

    for i in inp:
        if i.startswith('noop'):
            inc_cycle()
        elif i.startswith('addx'):
            inc_cycle()
            inc_cycle()
            x += int(i.split()[1])
    return sum(vals)


def part2(inp: list[str]):
    x = 1
    cycle = 0
    lines = []
    line = []

    def inc_cycle():
        nonlocal x, cycle
        pos = cycle % 40
        line.append('█' if x - 1 <= pos <= x + 1 else ' ')
        if pos == 39:
            lines.append(''.join(line))
            line.clear()
        cycle += 1

    for i in inp:
        if i.startswith('noop'):
            inc_cycle()
        elif i.startswith('addx'):
            inc_cycle()
            inc_cycle()
            x += int(i.split()[1])

    return ocr('\n'.join(lines))


if __name__ == "__main__":
    inp = parse(sys.stdin.read())

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
