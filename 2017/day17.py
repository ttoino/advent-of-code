def part1(inp: int) -> int:
    buffer = [0]
    p = 0
    d = inp
    for i in range(1, 2018):
        p += d
        p %= len(buffer)
        buffer.insert((p := (p + 1)), i)
    return buffer[p + 1]


def part2(inp: int) -> int:
    l = 0
    p = 0
    d = inp
    a = 0
    for i in range(1, 50000001):
        if (p := ((p + d) % i)) == 0:
            a = i
        p += 1
    return a


if __name__ == "__main__":
    inp = int(input())

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
