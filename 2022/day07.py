import sys

import more_itertools as mit



def visit(node: dict[str, dict | int] | int, small_dirs: list[int]):
    if isinstance(node, dict):
        s = sum(visit(v, small_dirs) for v in node.values())
        if s <= 100000:
            small_dirs.append(s)
        return s
    return node


def visit_p2(node: dict[str, dict | int] | int, dir_sizes: list[int]):
    if isinstance(node, dict):
        s = sum(visit_p2(v, dir_sizes) for v in node.values())
        dir_sizes.append(s)
        return s
    return node


def parse(s: str) -> dict:
    cmds = s.split('$ ')[1:]
    tree = {}
    curr = {}
    stack = []
    for cmd in cmds:
        cmd, *rest = cmd.split()
        if cmd == 'cd':
            arg = rest[0]
            if arg == '/':
                curr = tree
            elif arg == '..':
                curr = stack.pop()
            else:
                stack.append(curr)
                curr = curr[arg]
        if cmd == 'ls':
            for size, name in mit.chunked(rest, 2):
                if size == 'dir':
                    curr[name] = {}
                else:
                    curr[name] = int(size)
    return tree


def part1(inp: dict):
    small_dirs = []
    visit(inp, small_dirs)
    return sum(small_dirs)


def part2(inp: dict):
    dir_sizes = []
    total = visit_p2(inp, dir_sizes)
    needed_space = total - 40000000
    return min(filter(lambda x: x >= needed_space, dir_sizes))


if __name__ == "__main__":
    inp = parse(sys.stdin.read())

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
