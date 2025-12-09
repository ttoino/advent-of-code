use std::io;

type Input = Vec<Vec<bool>>;
type Neighbors = Vec<Vec<usize>>;

fn get_input() -> Input {
    io::stdin()
        .lines()
        .map(|l| l.unwrap().chars().map(|c| c == '@').collect())
        .collect()
}

fn neighbors(input: &Input) -> Neighbors {
    let mut result = vec![vec![0; input[0].len()]; input.len()];

    for i in 0..input.len() {
        let row = &input[i];

        for j in 0..row.len() {
            let mut acc = 0;
            for ii in (0.max(i as isize - 1))..=((input.len() as isize - 1).min(i as isize + 1)) {
                for jj in (0.max(j as isize - 1))..=((row.len() as isize - 1).min(j as isize + 1)) {
                    acc += input[ii as usize][jj as usize] as usize;
                }
            }

            result[i][j] = acc;
        }
    }

    result
}

fn part1(input: &Input, neighbors: &Neighbors) -> usize {
    let mut result = 0;

    for i in 0..input.len() {
        let row = &input[i];

        for j in 0..row.len() {
            if row[j] && neighbors[i][j] <= 4 {
                result += 1;
            }
        }
    }

    result
}

fn part2(mut input: Input, mut neighbors: Neighbors) -> usize {
    let len = input.len();
    let row_len = input[0].len();

    let mut result = 0;

    loop {
        let mut add = 0;

        for i in 0..len {
            let row = &mut input[i];

            for j in 0..row_len {
                if row[j] && neighbors[i][j] <= 4 {
                    row[j] = false;
                    add += 1;

                    for ii in (0.max(i as isize - 1))..=((len as isize - 1).min(i as isize + 1)) {
                        for jj in
                            (0.max(j as isize - 1))..=((row_len as isize - 1).min(j as isize + 1))
                        {
                            neighbors[ii as usize][jj as usize] -= 1;
                        }
                    }
                }
            }
        }

        if add == 0 {
            break;
        }

        result += add;
    }

    result
}

pub fn main() {
    let input = get_input();
    let neighbors = neighbors(&input);

    let result1 = part1(&input, &neighbors);
    println!("Part 1: {result1}");
    let result2 = part2(input, neighbors);
    println!("Part 2: {result2}");
}
