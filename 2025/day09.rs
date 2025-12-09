use std::io;

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
    0
}

pub fn main() {
    let input = get_input();

    println!("{input:?}");

    let result1 = part1(&input);
    println!("Part 1: {result1}");
    let result2 = part2(&input);
    println!("Part 2: {result2}");
}
