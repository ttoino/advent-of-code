import itertools as it
import re
import sys
from math import lcm

pattern = re.compile(r"(\w{3}) = \((\w{3}), (\w{3})\)")


def parse(i: str) -> tuple[str, dict[str, dict[str, str]]]:
    instructions, nodes = i.split("\n\n")
    return instructions, {
        (r := pattern.match(n)).group(1): {"L": r.group(2), "R": r.group(3)}
        for n in nodes.splitlines()
    }


def part1(inp: tuple[str, dict[str, dict[str, str]]]) -> int:
    instructions, nodes = inp
    current_node = "AAA"
    for i, direction in enumerate(it.cycle(instructions)):
        if current_node == "ZZZ":
            return i
            break
        current_node = nodes[current_node][direction]


def part2(inp: tuple[str, dict[str, dict[str, str]]]) -> int:
    instructions, nodes = inp
    current_nodes = [k for k in nodes.keys() if k[-1] == "A"]
    times = []
    for current_node in current_nodes:
        for i, direction in enumerate(it.cycle(instructions)):
            if current_node[-1] == "Z":
                times.append(i)
                break
            current_node = nodes[current_node][direction]
    return lcm(*times)


if __name__ == "__main__":
    inp = parse(sys.stdin.read())

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
