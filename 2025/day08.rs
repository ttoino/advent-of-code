use std::{
    collections::{BinaryHeap, HashSet},
    io,
    rc::Rc,
};

type Input = Vec<(usize, usize, usize)>;

fn get_input() -> Input {
    io::stdin()
        .lines()
        .map(|line| {
            let line = line.unwrap();
            let mut iter = line.splitn(3, ',').flat_map(str::parse::<usize>);

            (
                iter.next().unwrap(),
                iter.next().unwrap(),
                iter.next().unwrap(),
            )
        })
        .collect()
}

fn distance((x1, y1, z1): (usize, usize, usize), (x2, y2, z2): (usize, usize, usize)) -> f64 {
    let dx = x1.max(x2) - x1.min(x2);
    let dy = y1.max(y2) - y1.min(y2);
    let dz = z1.max(z2) - z1.min(z2);

    ((dx * dx + dy * dy + dz * dz) as f64).sqrt()
}

type Edges = Vec<(usize, usize)>;

fn sorted_edges(input: &Input) -> Edges {
    let mut edges = vec![];

    for i in 0..(input.len() - 1) {
        for j in (i + 1)..input.len() {
            edges.push((i, j));
        }
    }

    edges.sort_by(|(i1, j1), (i2, j2)| {
        distance(input[*i1], input[*j1])
            .partial_cmp(&distance(input[*i2], input[*j2]))
            .unwrap()
    });

    edges
}

fn part1(input: &Input, edges: &Edges) -> usize {
    let mut graph = vec![HashSet::new(); input.len()];

    for (i, j) in edges.iter().take(1000) {
        graph[*i].insert(*j);
        graph[*j].insert(*i);
    }

    let mut circuits = BinaryHeap::new();
    let mut visited = HashSet::new();

    for i in 0..input.len() {
        if visited.contains(&i) {
            continue;
        }

        let mut stack = vec![i];
        let mut circuit = 0;

        while let Some(current) = stack.pop() {
            if visited.contains(&current) {
                continue;
            }
            visited.insert(current);

            circuit += 1;
            stack.extend(&graph[current]);
        }

        circuits.push(circuit);
    }

    circuits.pop().unwrap() * circuits.pop().unwrap() * circuits.pop().unwrap()
}

fn part2(input: &Input, edges: &Edges) -> usize {
    let mut circuits: Vec<_> = (0..input.len())
        .map(|i| {
            let mut set = HashSet::new();
            set.insert(i);
            Rc::new(set)
        })
        .collect();

    for (i, j) in edges {
        let union = {
            let left = circuits[*i].clone();
            let right = circuits[*j].clone();

            let mut union = (*left).clone();
            union.extend(right.iter());

            Rc::new(union)
        };

        for k in union.iter() {
            circuits[*k] = union.clone();
        }

        if circuits.first().unwrap().len() >= input.len() {
            return input[*i].0 * input[*j].0;
        }
    }

    0
}

pub fn main() {
    let input = get_input();
    let edges = sorted_edges(&input);

    let result1 = part1(&input, &edges);
    println!("Part 1: {result1}");
    let result2 = part2(&input, &edges);
    println!("Part 2: {result2}");
}
