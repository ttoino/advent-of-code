import sys



def score(trees: list[list[int]], col: int, row: int, width: int, height: int):
    val = trees[row][col]
    up = 0
    for y in range(row - 1, -1, -1):
        up += 1
        if trees[y][col] >= val:
            break
    left = 0
    for x in range(col - 1, -1, -1):
        left += 1
        if trees[row][x] >= val:
            break
    down = 0
    for y in range(row + 1, height):
        down += 1
        if trees[y][col] >= val:
            break
    right = 0
    for x in range(col + 1, width):
        right += 1
        if trees[row][x] >= val:
            break
    return up * left * down * right


def parse(s: str) -> list[list[int]]:
    return [[int(i) for i in l] for l in s.splitlines()]


def part1(inp: list[list[int]]):
    trees = inp
    height = len(trees)
    width = len(trees[0])
    visible = set()
    for l in range(height):
        highest = -1
        for i in range(width):
            if trees[l][i] > highest:
                visible.add((i, l))
                highest = trees[l][i]
        highest = -1
        for i in range(width - 1, -1, -1):
            if trees[l][i] > highest:
                visible.add((i, l))
                highest = trees[l][i]
    for i in range(width):
        highest = -1
        for l in range(height):
            if trees[l][i] > highest:
                visible.add((i, l))
                highest = trees[l][i]
        highest = -1
        for l in range(height - 1, -1, -1):
            if trees[l][i] > highest:
                visible.add((i, l))
                highest = trees[l][i]
    return len(visible)


def part2(inp: list[list[int]]):
    trees = inp
    height = len(trees)
    width = len(trees[0])
    s = lambda x, y: score(trees, x, y, width, height)
    return max((s(x, y) for x in range(width) for y in range(height)))


if __name__ == "__main__":
    inp = parse(sys.stdin.read())

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
