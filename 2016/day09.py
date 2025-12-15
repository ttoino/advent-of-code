import re


def part1(inp: str) -> int:
    s = inp
    p = re.compile(r"(.*?)\((\d+)x(\d+)\)(.*)")
    r = ""

    while m := p.match(s):
        r += m[1]
        chars = int(m[2])
        times = int(m[3])
        r += m[4][:chars] * times
        s = m[4][chars:]

    r += s

    return len(r)


def part2(inp: str) -> int:
    s = inp
    r = 0

    while "(" in s:
        ms, me = s.find("("), s.find(")")
        r += ms
        chars, times = map(int, s[ms + 1 : me].split("x"))
        s = s[me + 1 : me + chars + 1] * times + s[me + chars + 1 :]

    r += len(s)

    return r


if __name__ == "__main__":
    inp = input()

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
