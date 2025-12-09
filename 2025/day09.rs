use std::{collections::BTreeMap, io, ops::Bound};

type Input = Vec<(usize, usize)>;

fn get_input() -> Input {
    io::stdin()
        .lines()
        .map(|line| {
            let line = line.unwrap();
            let mut iter = line.splitn(2, ',').flat_map(str::parse::<usize>);

            (iter.next().unwrap(), iter.next().unwrap())
        })
        .collect()
}

fn part1(input: &Input) -> usize {
    let mut max_area = 0;

    for i in 0..(input.len() - 1) {
        for j in (i + 1)..input.len() {
            let (x1, y1) = input[i];
            let (x2, y2) = input[j];

            max_area = max_area.max((x1.max(x2) - x1.min(x2) + 1) * (y1.max(y2) - y1.min(y2) + 1));
        }
    }

    max_area
}

fn part2(input: &Input) -> usize {
    let mut vertical_edges = BTreeMap::new();
    let mut horizontal_edges = BTreeMap::new();

    for i in 0..input.len() {
        let (x1, y1) = input[i];
        let (x2, y2) = input[(i + 1) % input.len()];

        if x1 == x2 {
            vertical_edges.insert(x1, (y1.min(y2), y1.max(y2)));
        } else {
            horizontal_edges.insert(y1, (x1.min(x2), x1.max(x2)));
        }
    }

    let mut max_area = 0;

    for i in 0..(input.len() - 1) {
        for j in (i + 1)..input.len() {
            let (x1, y1) = input[i];
            let (x2, y2) = input[j];

            let (x1, x2) = (x1.min(x2), x1.max(x2));
            let (y1, y2) = (y1.min(y2), y1.max(y2));

            if x2 > x1
                && vertical_edges
                    .range((Bound::Excluded(x1), Bound::Excluded(x2)))
                    .any(|(_, (edge_y1, edge_y2))| {
                        (*edge_y1 <= y1 && *edge_y2 > y1) || (*edge_y1 < y2 && *edge_y2 >= y2)
                    })
                || y2 > y1
                    && horizontal_edges
                        .range((Bound::Excluded(y1), Bound::Excluded(y2)))
                        .any(|(_, (edge_x1, edge_x2))| {
                            (*edge_x1 <= x1 && *edge_x2 > x1) || (*edge_x1 < x2 && *edge_x2 >= x2)
                        })
            {
                continue;
            }

            max_area = max_area.max((x2 - x1 + 1) * (y2 - y1 + 1));
        }
    }

    max_area
}

pub fn main() {
    let input = get_input();

    let result1 = part1(&input);
    println!("Part 1: {result1}");
    let result2 = part2(&input);
    println!("Part 2: {result2}");
}
