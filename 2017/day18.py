import sys
from collections import defaultdict, deque


def part1(inp: list[list[str]]) -> int:
    registers = defaultdict(lambda: 0)
    last_freq = -1
    ip = 0

    def get(r: str):
        return registers[r] if r.isalpha() else int(r)

    instructions = inp
    while len(instructions) > ip >= 0:
        match instructions[ip]:
            case ["snd", x]:
                last_freq = get(x)
            case ["set", x, y]:
                registers[x] = get(y)
            case ["add", x, y]:
                registers[x] = get(x) + get(y)
            case ["mul", x, y]:
                registers[x] = get(x) * get(y)
            case ["mod", x, y]:
                registers[x] = get(x) % get(y)
            case ["rcv", x]:
                if get(x) != 0:
                    return last_freq
            case ["jgz", x, y]:
                if get(x) > 0:
                    ip += get(y)
                    continue
        ip += 1


def part2(inp: list[list[str]]) -> int:
    registers = [defaultdict(lambda: 0), defaultdict(lambda: 1)]
    ip = [0, 0]
    instructions = inp
    pipes = [deque(), deque()]
    sent = [0, 0]

    def process(id: 0 | 1):
        def get(r: str):
            return registers[id][r] if r.isalpha() else int(r)

        while len(instructions) > ip[id] >= 0:
            match instructions[ip[id]]:
                case ["snd", x]:
                    pipes[id - 1].append(get(x))
                    sent[id] += 1
                case ["set", x, y]:
                    registers[id][x] = get(y)
                case ["add", x, y]:
                    registers[id][x] = get(x) + get(y)
                case ["mul", x, y]:
                    registers[id][x] = get(x) * get(y)
                case ["mod", x, y]:
                    registers[id][x] = get(x) % get(y)
                case ["rcv", x]:
                    if len(pipes[id]) == 0:
                        return False
                    else:
                        registers[id][x] = pipes[id].popleft()
                case ["jgz", x, y]:
                    if get(x) > 0:
                        ip[id] += get(y)
                        continue
            ip[id] += 1
        return True

    while True:
        if process(0) & process(1) or len(pipes[0]) == len(pipes[1]) == 0:
            return sent[1]
            break


if __name__ == "__main__":
    inp = [line.split() for line in sys.stdin.read().splitlines()]

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
