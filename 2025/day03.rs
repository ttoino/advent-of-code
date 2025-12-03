use std::io;

fn get_input() -> Vec<Vec<usize>> {
    io::stdin()
        .lines()
        .map(|l| {
            l.unwrap()
                .chars()
                .map(|c| c.to_digit(10).unwrap() as usize)
                .collect()
        })
        .collect()
}

fn solve(input: &Vec<Vec<usize>>, digits: usize) -> usize {
    input
        .iter()
        .map(|bank| {
            let mut best = vec![usize::MIN; digits];

            for i in 0..(bank.len() - digits + 1) {
                for j in 0..digits {
                    if bank[i + j] > best[j] {
                        for k in j..digits {
                            best[k] = bank[i + k];
                        }
                        break;
                    }
                }
            }

            best.iter().fold(0, |acc, i| acc * 10 + i)
        })
        .sum()
}

fn main() {
    let input = get_input();

    let result1 = solve(&input, 2);
    println!("Part 1: {result1}");
    let result2 = solve(&input, 12);
    println!("Part 2: {result2}");
}
