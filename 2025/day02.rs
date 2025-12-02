use std::io;

fn get_input() -> Vec<(usize, usize)> {
    io::stdin()
        .lines()
        .next()
        .unwrap()
        .unwrap()
        .split(",")
        .map(|s| {
            let (start, end) = s.split_once("-").unwrap();
            let start = start.parse::<usize>().unwrap();
            let end = end.parse::<usize>().unwrap();
            (start, end)
        })
        .collect()
}

fn part1(input: &Vec<(usize, usize)>) -> usize {
    input.iter().fold(0, |acc, (start, end)| {
        let mut result = acc;

        let start_str = start.to_string();
        let start_str = &start_str[..(start_str.len() / 2).max(1)];
        let start_prefix = start_str.parse::<usize>().unwrap();

        for i in start_prefix.. {
            let num = i.to_string().repeat(2).parse::<usize>().unwrap();

            if num > *end {
                break;
            }
            if num < *start {
                continue;
            }

            result += num;
        }

        result
    })
}

fn part2(input: &Vec<(usize, usize)>) -> usize {
    input.iter().fold(0, |acc, (start, end)| {
        let mut result = acc;

        for i in *start..=*end {
            let num = i.to_string();

            for j in 2..=num.len() {
                if num.len() % j != 0 {
                    continue;
                }

                if num == num[..(num.len() / j)].repeat(j) {
                    result += i;
                    break;
                }
            }
        }

        result
    })
}

fn main() {
    let input = get_input();

    let result1 = part1(&input);
    println!("Part 1: {result1}");
    let result2 = part2(&input);
    println!("Part 2: {result2}");
}
