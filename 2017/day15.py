def part1(inp: tuple[int, int]) -> int:
    a, b = inp
    s = 0
    for _ in range(40000000):
        a *= 16807
        a %= 2147483647
        b *= 48271
        b %= 2147483647
        s += a & 65535 == b & 65535
    return s


def part2(inp: tuple[int, int]) -> int:
    a, b = inp
    s = 0
    for i in range(5000000):
        print(f"{i}/5000000", end="\r")
        while True:
            a *= 16807
            a %= 2147483647
            if a % 4 == 0:
                break
        while True:
            b *= 48271
            b %= 2147483647
            if b % 8 == 0:
                break
        s += a & 65535 == b & 65535
    return s


if __name__ == "__main__":
    a = int(input().split()[-1])
    b = int(input().split()[-1])
    inp = (a, b)

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
