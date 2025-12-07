use std::io;

#[derive(PartialEq, Eq)]
enum Cell {
    Splitter,
    Beam(usize),
}

impl Cell {
    fn from_byte(byte: u8) -> Cell {
        match byte {
            b'^' => Cell::Splitter,
            b'S' | b'|' => Cell::Beam(1),
            _ => Cell::Beam(0),
        }
    }

    fn increase(&mut self, amount: usize) {
        if let Cell::Beam(beam) = self {
            *self = Cell::Beam(*beam + amount);
        }
    }

    fn value(&self) -> usize {
        if let Cell::Beam(beam) = self {
            *beam
        } else {
            0
        }
    }
}

type Input = Vec<Vec<Cell>>;

fn get_input() -> Input {
    io::stdin()
        .lines()
        .map(|line| line.unwrap().bytes().map(Cell::from_byte).collect())
        .collect()
}

fn solve(mut input: Input) -> (usize, usize) {
    let mut splits = 0;

    for i in 1..input.len() {
        let (prev, current) = input.split_at_mut(i);
        let prev = prev.last().unwrap();
        let current = current.first_mut().unwrap();

        for j in 0..prev.len() {
            let prev = prev[j].value();

            if current[j] == Cell::Splitter && prev > 0 {
                current[j - 1].increase(prev);
                current[j + 1].increase(prev);
                splits += 1;
            } else {
                current[j].increase(prev);
            }
        }
    }

    (splits, input.last().unwrap().iter().map(Cell::value).sum())
}

fn main() {
    let input = get_input();

    let (result1, result2) = solve(input);
    println!("Part 1: {result1}");
    println!("Part 2: {result2}");
}
