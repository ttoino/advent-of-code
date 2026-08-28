import operator as op
import sys

XMAS = {"x": 0, "m": 1, "a": 2, "s": 3}
OPS = {"<": op.lt, ">": op.gt}


def parse(i: str) -> tuple[dict[str, list], set[tuple[int, int, int, int]]]:
    rules, parts = i.split("\n\n")
    rules = {
        l[: l.index("{")]: [
            r
            if ":" not in r
            else (
                XMAS[r[0]],
                OPS[r[1]],
                int(r[2 : r.index(":")]),
                r[r.index(":") + 1 :],
            )
            for r in l[l.index("{") + 1 : l.index("}")].split(",")
        ]
        for l in rules.splitlines()
    }
    parts = {
        tuple((int(n.split("=")[1]) for n in part[1:-1].split(",")))
        for part in parts.splitlines()
    }
    return rules, parts


def solve(inp: tuple[dict[str, list], set[tuple[int, int, int, int]]]) -> int:
    rules, parts = inp
    result = 0
    for part in parts:
        current = "in"
        while current not in "AR":
            for rule in rules[current]:
                if isinstance(rule, str):
                    current = rule
                    break
                elif rule[1](part[rule[0]], rule[2]):
                    current = rule[3]
                    break
        if current == "A":
            result += sum(part)
    return result


if __name__ == "__main__":
    inp = parse(sys.stdin.read())

    print(f"Solution: {solve(inp)}")
