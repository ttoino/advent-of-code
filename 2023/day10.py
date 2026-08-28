import sys

DIR_MAP = {
    "|": {(0, 1), (0, -1)},
    "-": {(1, 0), (-1, 0)},
    "L": {(1, 0), (0, -1)},
    "J": {(-1, 0), (0, -1)},
    "7": {(-1, 0), (0, 1)},
    "F": {(1, 0), (0, 1)},
    ".": set(),
}

DIRS = {(0, 1), (0, -1), (1, 0), (-1, 0)}


def rotate_clockwise(dir):
    if dir == (0, -1):
        return (1, 0)
    if dir == (1, 0):
        return (0, 1)
    if dir == (0, 1):
        return (-1, 0)
    if dir == (-1, 0):
        return (0, -1)


def rotate_counterclockwise(dir):
    if dir == (0, -1):
        return (-1, 0)
    if dir == (-1, 0):
        return (0, 1)
    if dir == (0, 1):
        return (1, 0)
    if dir == (1, 0):
        return (0, -1)


def part1(inp: list[str]) -> int:
    pipemap = list(inp)
    start_y, _ = [l for l in enumerate(pipemap) if "S" in l[1]][0]
    start_x = pipemap[start_y].index("S")
    start_DIRS = set()
    for dir_x, dir_y in DIRS:
        x = start_x + dir_x
        y = start_y + dir_y
        reverse_dir = (-dir_x, -dir_y)
        if reverse_dir in DIR_MAP[pipemap[y][x]]:
            start_DIRS.add((dir_x, dir_y))
    start_char = [k for k, v in DIR_MAP.items() if start_DIRS == v][0]
    pipemap[start_y] = (
        pipemap[start_y][:start_x]
        + start_char
        + pipemap[start_y][start_x + 1 :]
    )
    length = 0
    x, y = (start_x, start_y)
    prev_dir = (0, 0)
    while True:
        length += 1
        dir = (DIR_MAP[pipemap[y][x]] - {(-prev_dir[0], -prev_dir[1])}).pop()
        x += dir[0]
        y += dir[1]
        prev_dir = dir
        if (x, y) == (start_x, start_y):
            break
    return length // 2


def part2(inp: list[str]) -> int:
    pipemap = list(inp)
    start_y, _ = [l for l in enumerate(pipemap) if "S" in l[1]][0]
    start_x = pipemap[start_y].index("S")
    start_DIRS = set()
    for dir_x, dir_y in DIRS:
        x = start_x + dir_x
        y = start_y + dir_y
        reverse_dir = (-dir_x, -dir_y)
        if reverse_dir in DIR_MAP[pipemap[y][x]]:
            start_DIRS.add((dir_x, dir_y))
    start_char = [k for k, v in DIR_MAP.items() if start_DIRS == v][0]
    pipemap[start_y] = (
        pipemap[start_y][:start_x]
        + start_char
        + pipemap[start_y][start_x + 1 :]
    )
    x, y = (start_x, start_y)
    prev_dir = (0, 0)
    main_loop: list[tuple[int, int]] = []
    main_loop_DIRS: list[tuple[int, int]] = []
    while True:
        main_loop.append((x, y))
        dir = (DIR_MAP[pipemap[y][x]] - {(-prev_dir[0], -prev_dir[1])}).pop()
        main_loop_DIRS.append(dir)
        x += dir[0]
        y += dir[1]
        prev_dir = dir
        if (x, y) == (start_x, start_y):
            break
    prev_main_loop_DIRS = main_loop_DIRS[-1:] + main_loop_DIRS[:-1]
    print("Main loop length:", len(main_loop))
    visited: set[tuple[int, int]] = set()
    queue = [(0, 0)]
    while len(queue) > 0:
        x, y = queue.pop(0)
        if (
            (x, y) in visited
            or (x, y) in main_loop
            or x < 0
            or (x >= len(pipemap[0]))
            or (y < 0)
            or (y >= len(pipemap))
        ):
            continue
        visited.add((x, y))
        for dir_x, dir_y in DIRS:
            queue.append((x + dir_x, y + dir_y))
    print("Visited:", len(visited))
    turn: callable = None
    for (x, y), (main_dir_x, main_dir_y) in zip(main_loop, main_loop_DIRS):
        for dir_x, dir_y in DIRS:
            if (x + dir_x, y + dir_y) in visited:
                if rotate_clockwise((dir_x, dir_y)) == (
                    main_dir_x,
                    main_dir_y,
                ):
                    turn = rotate_clockwise
                elif rotate_counterclockwise((dir_x, dir_y)) == (
                    main_dir_x,
                    main_dir_y,
                ):
                    turn = rotate_counterclockwise
                if turn != None:
                    break
        else:
            continue
        break
    print("Turn:", turn)
    inside_queue = []
    for (x, y), main_dir, prev_main_dir in zip(
        main_loop, main_loop_DIRS, prev_main_loop_DIRS
    ):
        rot = turn(main_dir)
        while rot != (-prev_main_dir[0], -prev_main_dir[1]):
            inside_queue.append((x + rot[0], y + rot[1]))
            rot = turn(rot)
    print("Inside queue length:", len(inside_queue))
    inside_visited = set()
    while len(inside_queue) > 0:
        x, y = inside_queue.pop(0)
        if (x, y) in visited:
            print("What", x, y)
            break
        if (
            (x, y) in inside_visited
            or (x, y) in main_loop
            or x < 0
            or (x >= len(pipemap[0]))
            or (y < 0)
            or (y >= len(pipemap))
        ):
            continue
        inside_visited.add((x, y))
        for dir_x, dir_y in DIRS:
            inside_queue.append((x + dir_x, y + dir_y))
    return len(inside_visited)


if __name__ == "__main__":
    inp = [line.strip() for line in sys.stdin.readlines()]

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
