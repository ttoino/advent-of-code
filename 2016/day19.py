def part1(inp: int) -> int:
    n = f"{inp:b}"
    return int(n[1:] + n[0], 2)


def part2(n: int) -> int:
    r = 1
    s = -1

    for i in range(1, n):
        if r == i:
            r = 1
            s += 1
        else:
            r += 1 + (r >= 3**s)

    return r


if __name__ == "__main__":
    inp = int(input())

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
