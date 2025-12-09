use std::{io, ops::RangeInclusive};

type Ranges = Vec<RangeInclusive<usize>>;
type IDs = Vec<usize>;

fn get_input() -> (Ranges, IDs) {
    let mut ranges = vec![];
    let mut ids = vec![];

    let mut split = false;

    for line in io::stdin().lines() {
        let line = line.unwrap();
        if line.is_empty() {
            split = true;
            continue;
        }

        if !split {
            let (start, end) = line.split_once('-').unwrap();
            ranges.push(start.parse().unwrap()..=end.parse().unwrap());
        } else {
            ids.push(line.parse().unwrap());
        }
    }

    (ranges, ids)
}

fn normalize_ranges(mut ranges: Ranges) -> Ranges {
    ranges.sort_by_key(|range| *range.start());

    let mut result: Vec<RangeInclusive<usize>> = vec![];

    for range in ranges {
        if let Some(last_range) = result.last_mut() && last_range.end() >= range.start() {
            *last_range = *last_range.start().min(range.start())..=*last_range.end().max(range.end());
        } else {
            result.push(range);
        }
    }

    result
}

fn part1(ranges: &Ranges, ids: &IDs) -> usize {
    ids.iter()
        .filter(|id| ranges.iter().any(|range| range.contains(id)))
        .count()
}

fn part2(ranges: &Ranges) -> usize {
    ranges.iter().map(|range| range.end() - range.start() + 1).sum()
}

pub fn main() {
    let (ranges, ids) = get_input();
    let ranges = normalize_ranges(ranges);

    let result1 = part1(&ranges, &ids);
    println!("Part 1: {result1}");
    let result2 = part2(&ranges);
    println!("Part 2: {result2}");
}
