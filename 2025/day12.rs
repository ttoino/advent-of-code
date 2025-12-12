const SHAPES: usize = 6;
const SHAPE_WIDTH: usize = 3;
const SHAPE_HEIGHT: usize = 3;

type Shape = [bool; SHAPE_WIDTH * SHAPE_HEIGHT];

struct Region {
    width: usize,
    height: usize,
    shapes: [usize; SHAPES],
}

struct Input {
    shapes: [Shape; SHAPES],
    regions: Vec<Region>,
}

fn get_input() -> Input {
    let mut lines = std::io::stdin().lines().flatten();

    let mut shapes = [[false; SHAPE_WIDTH * SHAPE_HEIGHT]; SHAPES];
    for i in 0..SHAPES {
        let line = lines
            .by_ref()
            .take(SHAPE_HEIGHT + 2)
            .skip(1)
            .flat_map(|line| line.chars().collect::<Vec<_>>());

        for (j, c) in line.enumerate() {
            shapes[i][j] = if c == '#' { true } else { false };
        }
    }

    let regions = lines
        .map(|line| {
            let (size, counts) = line.split_once(": ").unwrap();
            let (width, height) = size.split_once('x').unwrap();
            let mut counts = counts.split_whitespace().flat_map(str::parse);

            let mut shapes = [0; SHAPES];
            for i in 0..SHAPES {
                shapes[i] = counts.next().unwrap();
            }

            Region {
                width: width.parse().unwrap(),
                height: height.parse().unwrap(),
                shapes,
            }
        })
        .collect();

    Input { shapes, regions }
}

fn solve(input: Input) -> usize {
    let shapes = input
        .shapes
        .map(|shape| shape.into_iter().map(|b| b as usize).sum());

    input
        .regions
        .into_iter()
        .map(|region| {
            (shapes
                .iter()
                .zip(region.shapes)
                .map(|(area, count)| area * count)
                .sum::<usize>()
                <= region.width * region.height) as usize
        })
        .sum()
}

pub fn main() {
    let input = get_input();

    let result = solve(input);
    println!("Solution: {result}");
}
