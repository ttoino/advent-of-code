import json
import sys


def visit(o, part: int):
    match o:
        case int(o):
            return o
        case dict(o):
            return (
                0
                if part == 2 and "red" in o.values()
                else sum(visit(x, part) for x in o.values())
            )
        case list(o):
            return sum(visit(x, part) for x in o)
        case _:
            return 0


if __name__ == "__main__":
    inp = json.load(sys.stdin)

    print(f"Part 1: {visit(inp, 1)}")
    print(f"Part 2: {visit(inp, 2)}")
