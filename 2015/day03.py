def solve(inp: str, part: int):
    s = {(0, 0)}
    curr = (0, 0)
    curr_r = (0, 0)

    for i, d in enumerate(inp):
        match d:
            case ">":
                if part == 1 or i % 2:
                    curr = curr[0] + 1, curr[1]
                else:
                    curr_r = curr_r[0] + 1, curr_r[1]
            case "<":
                if part == 1 or i % 2:
                    curr = curr[0] - 1, curr[1]
                else:
                    curr_r = curr_r[0] - 1, curr_r[1]
            case "^":
                if part == 1 or i % 2:
                    curr = curr[0], curr[1] + 1
                else:
                    curr_r = curr_r[0], curr_r[1] + 1
            case "v":
                if part == 1 or i % 2:
                    curr = curr[0], curr[1] - 1
                else:
                    curr_r = curr_r[0], curr_r[1] - 1

        if part == 1 or i % 2:
            s.add(curr)
        else:
            s.add(curr_r)

    return len(s)


if __name__ == "__main__":
    inp = input()

    print(f"Part 1: {solve(inp, 1)}")
    print(f"Part 2: {solve(inp, 2)}")
