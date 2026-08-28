import sys


def diff(a, b):
    return sum((1 for x, y in zip(a, b) for u, v in zip(x, y) if u != v))


def parse(i: str) -> list[str]:
    return i.splitlines()


def part1(inp: list[list[str]]) -> int:
    result = 0
    for p in inp:
        for y in range(1, len(p)):
            above, below = (p[:y], p[y:])
            minlength = min(len(above), len(below))
            if above[-minlength:] == below[:minlength][::-1]:
                result += 100 * len(above)
                break
        else:
            p = list(zip(*p))
            for x in range(1, len(p)):
                left, right = (p[:x], p[x:])
                minlength = min(len(left), len(right))
                if left[-minlength:] == right[:minlength][::-1]:
                    result += len(left)
                    break
            else:
                print('no match')
    return result


def part2(inp: list[list[str]]) -> int:
    result = 0
    for p in inp:
        for y in range(1, len(p)):
            above, below = (p[:y], p[y:])
            minlength = min(len(above), len(below))
            if diff(above[-minlength:], below[:minlength][::-1]) == 1:
                result += 100 * len(above)
                break
        else:
            p = list(zip(*p))
            for x in range(1, len(p)):
                left, right = (p[:x], p[x:])
                minlength = min(len(left), len(right))
                if diff(left[-minlength:], right[:minlength][::-1]) == 1:
                    result += len(left)
                    break
            else:
                print('no match')
    return result


if __name__ == "__main__":
    inp = [parse(p) for p in sys.stdin.read().strip().split('\n\n')]

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
