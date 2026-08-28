import sys


def hash(code: str) -> int:
    result = 0
    for char in code:
        result += ord(char)
        result *= 17
        result %= 256
    return result


def parse(i: str) -> list[str]:
    return i.strip().split(",")


def part1(inp: list[str]) -> int:
    result = 0
    for code in inp:
        hash = 0
        for char in code:
            hash += ord(char)
            hash *= 17
            hash %= 256
        result += hash
    return result


def part2(inp: list[str]) -> int:
    codes = inp
    hashmap = tuple(({} for _ in range(256)))
    for code in codes:
        if code[-1] == "-":
            hashmap[hash(code[:-1])].pop(code[:-1], None)
        else:
            hashmap[hash(code[:-2])][code[:-2]] = int(code[-1])
    result = 0
    for i, hashmap in enumerate(hashmap):
        for j, (code, value) in enumerate(list(hashmap.items())):
            print(f"{i} {j} {code} {value}")
            result += (i + 1) * (j + 1) * value
    return result


if __name__ == "__main__":
    inp = parse(sys.stdin.read())

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
