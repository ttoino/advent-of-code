from hashlib import md5
import heapq as hq


def part1(passcode: str) -> str:
    heap = [(0, "")]

    while len(heap) > 0:
        d, p = hq.heappop(heap)

        if p.count("D") - p.count("U") == 3 and p.count("R") - p.count("L") == 3:
            return p

        for di, c in zip("UDLR", md5(bytes(passcode + p, "ascii")).hexdigest()):
            if ord("b") <= ord(c) <= ord("f"):
                hq.heappush(heap, (d + 1, p + di))

    return ""


def part2(passcode: str) -> int:
    heap = [(0, "", 1, 1)]
    paths = set()

    while len(heap) > 0:
        d, p, x, y = hq.heappop(heap)

        if p.count("D") - p.count("U") == 3 and p.count("R") - p.count("L") == 3:
            paths.add(p)
            continue

        for di, c in zip("UDLR", md5(bytes(passcode + p, "ascii")).hexdigest()):
            nx = x + (di == "R") - (di == "L")
            ny = y + (di == "D") - (di == "U")
            if 0 < nx <= 4 and 0 < ny <= 4 and ord("b") <= ord(c) <= ord("f"):
                hq.heappush(heap, (d + 1, p + di, nx, ny))

    return max(map(len, paths))


if __name__ == "__main__":
    inp = input()

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
