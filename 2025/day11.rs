use std::{
    collections::{HashMap, HashSet},
    io,
};

type Input = HashMap<String, HashSet<String>>;

fn get_input() -> Input {
    io::stdin()
        .lines()
        .map(|line| {
            let line = line.unwrap();
            let (label, outputs) = line.split_once(": ").unwrap();
            let outputs = outputs.split_whitespace().map(str::to_string).collect();

            (label.to_string(), outputs)
        })
        .collect()
}

fn part1(input: &Input, label: &str) -> usize {
    if label == "out" {
        return 1;
    }

    input
        .get(label)
        .unwrap()
        .iter()
        .map(|output| part1(&input, output.as_str()))
        .sum()
}

fn part2(
    input: &Input,
    label: &str,
    visited: &mut HashSet<String>,
    memo: &mut HashMap<(String, bool, bool), usize>,
) -> usize {
    if visited.contains(label) {
        return 0;
    }

    let has_dac = visited.contains("dac");
    let has_fft = visited.contains("fft");

    if let Some(result) = memo.get(&(label.to_string(), has_dac, has_fft)) {
        return *result;
    }

    if label == "out" {
        return (has_dac && has_fft) as usize;
    }

    visited.insert(label.to_string());

    let result = input
        .get(label)
        .unwrap()
        .iter()
        .map(|output| part2(&input, output.as_str(), visited, memo))
        .sum();

    visited.remove(label);
    memo.insert((label.to_string(), has_dac, has_fft), result);

    result
}

pub fn main() {
    let input = get_input();

    let result1 = part1(&input, "you");
    println!("Part 1: {result1}");
    let result2 = part2(&input, "svr", &mut HashSet::new(), &mut HashMap::new());
    println!("Part 2: {result2}");
}
