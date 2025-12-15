import sys


class Robot:
    number: str
    give_low_to: str | None = None
    give_high_to: str | None = None
    v1: int | None = None
    v2: int | None = None

    def __init__(self, n: str):
        self.number = n

    def handle(self):
        if not (
            self.give_high_to is not None
            and self.give_low_to is not None
            and self.v1 is not None
            and self.v2 is not None
        ):
            return

        if (self.v1, self.v2) == (61, 17) or (self.v1, self.v2) == (17, 61):
            outputs["part1"] = int(self.number)

        if self.give_low_to.startswith("o"):
            outputs[self.give_low_to] = min(self.v1, self.v2)
        else:
            robots.setdefault(self.give_low_to, Robot(self.give_low_to))
            robots[self.give_low_to].give_value(min(self.v1, self.v2))

        if self.give_high_to.startswith("o"):
            outputs[self.give_high_to] = max(self.v1, self.v2)
        else:
            robots.setdefault(self.give_high_to, Robot(self.give_high_to))
            robots[self.give_high_to].give_value(max(self.v1, self.v2))

    def give_value(self, v: int):
        if self.v1 is None:
            self.v1 = v
        else:
            self.v2 = v

        self.handle()

    def set_low(self, r: str):
        self.give_low_to = r

        self.handle()

    def set_high(self, r: str):
        self.give_high_to = r

        self.handle()


robots: dict[str, Robot] = {}
outputs = {"part1": 0}


def solve(inp: list[list[str]]) -> tuple[int, int]:
    for i in inp:
        match i:
            case ["value", x, "goes", "to", "bot", y]:
                robots.setdefault(y, Robot(y))
                robots[y].give_value(int(x))
            case ["bot", x, "gives", "low", "to", obl, y, "and", "high", "to", obh, z]:
                robots.setdefault(x, Robot(x))
                robots[x].set_low(("" if obl == "bot" else "o") + y)
                robots[x].set_high(("" if obh == "bot" else "o") + z)

    return outputs["part1"], outputs["o0"] * outputs["o1"] * outputs["o2"]


if __name__ == "__main__":
    inp = [i.split() for i in sys.stdin.readlines()]

    part1, part2 = solve(inp)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
