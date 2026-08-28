import sys

import more_itertools as mit


def parse(i: str) -> tuple[list[int], list[list[tuple[int, int, int]]]]:
    paragraphs = i.split('\n\n')
    seeds = list(map(int, paragraphs[0].split(':')[1].split()))
    maps = [
        [tuple(map(int, l.split())) for l in m.strip().split('\n')[1:]]
        for m in paragraphs[1:]
    ]
    return seeds, maps


def part1(inp: tuple[list[int], list[list[tuple[int, int, int]]]]) -> int:
    seeds = list(inp[0])
    maps = inp[1]
    for m in maps:
        for i, seed in enumerate(seeds):
            for startvalue, startkey, length in m:
                if startkey <= seed < startkey + length:
                    seeds[i] = startvalue + seed - startkey
                    break
    return min(seeds)


def part2(inp: tuple[list[int], list[list[tuple[int, int, int]]]]) -> int:
    seedRanges = list(map(tuple, mit.chunked(inp[0], 2)))
    maps = inp[1]
    nextRanges = []
    for m in maps:
        while len(seedRanges) > 0:
            sstart, slength = seedRanges.pop(0)
            for l in m:
                vstart, kstart, length = l
                if sstart + slength <= kstart or kstart + length <= sstart:
                    continue
                if kstart <= sstart and sstart + slength <= kstart + length:
                    nextRanges.append((vstart + sstart - kstart, slength))
                    break
                if kstart <= sstart:
                    nlength = kstart + length - sstart
                    nextRanges.append((vstart + sstart - kstart, nlength))
                    seedRanges.insert(0, (sstart + nlength, slength - nlength))
                    break
                nlength = sstart + slength - kstart
                nextRanges.append((vstart - kstart + (sstart + slength - nlength), nlength))
                seedRanges.insert(0, (sstart, slength - nlength))
                break
            else:
                nextRanges.append((sstart, slength))
        seedRanges = nextRanges
        nextRanges = []
    return min(map(lambda x: x[0], seedRanges))


if __name__ == "__main__":
    inp = parse(sys.stdin.read())

    print(f"Part 1: {part1(inp)}")
    print(f"Part 2: {part2(inp)}")
