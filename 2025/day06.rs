use std::io;

type Input = Vec<String>;

fn get_input() -> Input {
    io::stdin().lines().flatten().collect()
}

fn part1(input: &Input) -> usize {
    let operations = input.last().unwrap().split_whitespace().collect::<Vec<_>>();

    input[..(input.len() - 1)]
        .iter()
        .map(|line| {
            line.split_whitespace()
                .flat_map(&str::parse::<usize>)
                .collect::<Vec<_>>()
        })
        .reduce(|mut acc, line| {
            for ((i, number), op) in acc.iter_mut().zip(line).zip(operations.iter()) {
                if *op == "+" {
                    *i += number;
                } else {
                    *i *= number;
                }
            }

            acc
        })
        .unwrap()
        .into_iter()
        .sum()
}

fn part2(input: &Input) -> usize {
    let operations = input.last().unwrap().split_whitespace().collect::<Vec<_>>();

    let mut result = 0;
    let mut current_op = 0;
    let mut current = if operations[current_op] == "+" { 0 } else { 1 };

    for i in 0..input[0].len() {
        let number = input[..(input.len() - 1)].iter().fold(0, |acc, line| {
            let n = line.as_bytes()[i];

            if n == b' ' {
                acc
            } else {
                acc * 10 + (n - b'0') as usize
            }
        });

        if number == 0 {
            result += current;
            current_op += 1;
            current = if operations[current_op] == "+" { 0 } else { 1 };
        } else if operations[current_op] == "+" {
            current += number;
        } else {
            current *= number;
        }
    }

    result + current
}

pub fn main() {
    let input = get_input();

    let result1 = part1(&input);
    println!("Part 1: {result1}");
    let result2 = part2(&input);
    println!("Part 2: {result2}");
}
