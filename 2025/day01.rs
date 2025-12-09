use std::io;

type Input = Vec<isize>;

fn get_input() -> Input {
    io::stdin()
        .lines()
        .map(|l| {
            let mut line = l.unwrap();
            let num = line.split_off(1);
            num.parse::<isize>().unwrap() * if line == "L" { -1 } else { 1 }
        })
        .collect()
}

fn part1(input: &Input) -> isize {
    input
        .iter()
        .scan(50, |total, i| {
            *total = (*total + i).rem_euclid(100);
            Some(if *total == 0 { 1 } else { 0 })
        })
        .sum()
}

fn part2(input: &Input) -> isize {
    input
        .iter()
        .scan(50, |total, i| {
            *total = *total + i;
            let mut result = (*total / 100).abs();
            if *i < 0 && *total <= 0 && total != i {
                result += 1
            };
            *total = total.rem_euclid(100);
            Some(result)
        })
        .sum()
}

pub fn main() {
    let input = get_input();

    let result1 = part1(&input);
    println!("Part 1: {result1}");
    let result2 = part2(&input);
    println!("Part 2: {result2}");
}
