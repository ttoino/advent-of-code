import functools as ft
import operator as op
import sys


def parse_packet(packet, count=-1):
    if packet == "" or int(packet, 2) == 0:
        return 0
    if count == 0:
        return parse_packet(packet, count - 1)
    v = int(packet[:3], 2)
    t = int(packet[3:6], 2)
    if t == 4:
        i = 6
        done = False
        number = ""
        while not done:
            if packet[i] == "0":
                done = True
            number += packet[i + 1 : i + 5]
            i += 5
        number = int(number, 2)
        return v + parse_packet(packet[i:], count - 1)
    i = packet[6]
    if i == "1":
        l = int(packet[7:18], 2)
        return v + parse_packet(packet[18:], l)
    else:
        l = int(packet[7:22], 2)
        return (
            v
            + parse_packet(packet[22 : 22 + l], -1)
            + parse_packet(packet[22 + l :], count - 1)
        )


def operate(t, values):
    match t:
        case 0:
            return sum(values)
        case 1:
            return ft.reduce(op.mul, values)
        case 2:
            return min(values)
        case 3:
            return max(values)
        case 5:
            return int(values[0] > values[1])
        case 6:
            return int(values[0] < values[1])
        case 7:
            return int(values[0] == values[1])


def parse_packet_p2(packet, start, end=-1) -> tuple[int | None, int | None]:
    if start == end:
        return (None, None)
    if packet[start:end] == "" or int(packet[start:end], 2) == 0:
        return (None, None)
    v = int(packet[start : start + 3], 2)
    t = int(packet[start + 3 : start + 6], 2)
    if t == 4:
        start += 6
        done = False
        number = ""
        while not done:
            if packet[start] == "0":
                done = True
            number += packet[start + 1 : start + 5]
            start += 5
        number = int(number, 2)
        return (number, start)
    values = []
    next_start = None
    i = packet[start + 6]
    if i == "1":
        l = int(packet[start + 7 : start + 18], 2)
        index = start + 18
        while l > 0:
            x, index = parse_packet_p2(packet, index)
            l -= 1
            values.append(x)
        next_start = index
    else:
        l = int(packet[start + 7 : start + 22], 2)
        end = start + 22 + l
        index = start + 22
        prev_index = None
        while index != None:
            prev_index = index
            x, index = parse_packet_p2(packet, index, end)
            values.append(x)
        values = values[:-1]
        next_start = prev_index
    return (operate(t, values), next_start)


def parse(inp: str) -> str:
    return "".join(f"{int(x, 16):04b}" for x in inp.strip())


def part1(inp: str) -> int:
    return parse_packet(inp)


def part2(inp: str) -> int:
    return parse_packet_p2(inp, 0)[0]


if __name__ == "__main__":
    inp = parse(sys.stdin.read())

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
