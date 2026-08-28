import sys


MIRROR_MAP = {
    '.': {
        (1, 0): [(1, 0)],
        (-1, 0): [(-1, 0)],
        (0, 1): [(0, 1)],
        (0, -1): [(0, -1)],
    },
    '/': {
        (1, 0): [(0, -1)],
        (0, -1): [(1, 0)],
        (-1, 0): [(0, 1)],
        (0, 1): [(-1, 0)],
    },
    '\\': {
        (1, 0): [(0, 1)],
        (0, 1): [(1, 0)],
        (-1, 0): [(0, -1)],
        (0, -1): [(-1, 0)],
    },
    '-': {
        (1, 0): [(1, 0)],
        (-1, 0): [(-1, 0)],
        (0, 1): [(1, 0), (-1, 0)],
        (0, -1): [(1, 0), (-1, 0)],
    },
    '|': {
        (0, 1): [(0, 1)],
        (0, -1): [(0, -1)],
        (1, 0): [(0, 1), (0, -1)],
        (-1, 0): [(0, 1), (0, -1)],
    },
}


def part1(inp: list[str]) -> int:
    mirrors = inp
    visited = set()
    beams = [((0, 0), (1, 0))]
    while len(beams) > 0:
        beam = beams.pop()
        (beam_x, beam_y), beam_dir = beam
        if beam in visited or beam_x < 0 or beam_x >= len(mirrors[0]) or (beam_y < 0) or (beam_y >= len(mirrors)):
            continue
        visited.add(beam)
        mirror = mirrors[beam_y][beam_x]
        beam_dirs = MIRROR_MAP[mirror][beam_dir]
        beams += [((beam_x + d[0], beam_y + d[1]), d) for d in beam_dirs]
    return len({v[0] for v in visited})


def part2(inp: list[str]) -> int:
    mirrors = inp
    solutions = {}

    def solve(start):
        if start in solutions:
            return
        visited = set()
        beams = [start]
        ends = {start}
        while len(beams) > 0:
            beam = beams.pop()
            (beam_x, beam_y), beam_dir = beam
            if beam in visited:
                continue
            if beam_x < 0:
                ends.add(((0, beam_y), (-beam_dir[0], -beam_dir[1])))
                continue
            elif beam_x >= len(mirrors[0]):
                ends.add(((len(mirrors[0]) - 1, beam_y), (-beam_dir[0], -beam_dir[1])))
                continue
            elif beam_y < 0:
                ends.add(((beam_x, 0), (-beam_dir[0], -beam_dir[1])))
                continue
            elif beam_y >= len(mirrors):
                ends.add((beam_x, len(mirrors) - 1, (-beam_dir[0], -beam_dir[1])))
                continue
            visited.add(beam)
            mirror = mirrors[beam_y][beam_x]
            beam_dirs = MIRROR_MAP[mirror][beam_dir]
            beams += [((beam_x + d[0], beam_y + d[1]), d) for d in beam_dirs]
        solution = len({v[0] for v in visited})
        for e in ends:
            solutions[e] = solution
    for x in range(len(mirrors[0])):
        solve(((x, 0), (0, 1)))
        solve(((x, len(mirrors) - 1), (0, -1)))
    for y in range(len(mirrors[0])):
        solve(((0, y), (1, 0)))
        solve(((len(mirrors[0]) - 1, y), (-1, 0)))
    return max(solutions.values())


if __name__ == "__main__":
    inp = [line.strip() for line in sys.stdin.readlines()]

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
