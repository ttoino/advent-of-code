def part1(inp: str) -> int:
    s = inp
    score = 0
    depth = 0
    in_garbage = False
    i = 0
    while i < len(s):
        c = s[i]
        match c:
            case "!" if in_garbage:
                i += 1
            case ">" if in_garbage:
                in_garbage = False
            case _ if in_garbage:
                pass
            case "{":
                depth += 1
            case "}":
                score += depth
                depth -= 1
            case "<":
                in_garbage = True
        i += 1
    return score


def part2(inp: str) -> int:
    s = inp
    garbage = 0
    score = 0
    depth = 0
    in_garbage = False
    i = 0
    while i < len(s):
        c = s[i]
        match c:
            case "!" if in_garbage:
                i += 1
            case ">" if in_garbage:
                in_garbage = False
            case _ if in_garbage:
                garbage += 1
            case "{":
                depth += 1
            case "}":
                score += depth
                depth -= 1
            case "<":
                in_garbage = True
        i += 1
    return garbage


if __name__ == "__main__":
    inp = input().strip()

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
