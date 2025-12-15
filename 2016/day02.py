import sys


def part1(inp: list[str]) -> str:
    btn = 5
    result = ""

    for line in inp:
        for d in line:
            match d:
                case "U":
                    if btn > 3:
                        btn -= 3
                case "R":
                    if btn % 3 != 0:
                        btn += 1
                case "D":
                    if btn < 7:
                        btn += 3
                case "L":
                    if btn % 3 != 1:
                        btn -= 1

        result += str(btn)

    return result


def part2(inp: list[str]) -> str:
    btns = {
        (0, -2): "1",
        (-1, -1): "2",
        (0, -1): "3",
        (1, -1): "4",
        (-2, 0): "5",
        (-1, 0): "6",
        (0, 0): "7",
        (1, 0): "8",
        (2, 0): "9",
        (-1, 1): "A",
        (0, 1): "B",
        (1, 1): "C",
        (0, 2): "D",
    }
    btn = (-2, 0)
    result = ""

    for line in inp:
        for d in line:
            match d:
                case "U":
                    if btn[1] - abs(btn[0]) != -2:
                        btn = btn[0], btn[1] - 1
                case "R":
                    if btn[0] + abs(btn[1]) != 2:
                        btn = btn[0] + 1, btn[1]
                case "D":
                    if btn[1] + abs(btn[0]) != 2:
                        btn = btn[0], btn[1] + 1
                case "L":
                    if btn[0] - abs(btn[1]) != -2:
                        btn = btn[0] - 1, btn[1]

        result += btns[btn]

    return result


if __name__ == "__main__":
    inp = sys.stdin.readlines()

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
