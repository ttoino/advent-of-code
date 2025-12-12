#[derive(Debug)]
struct Machine {
    lights: Vec<bool>,
    buttons: Vec<Vec<usize>>,
    joltage: Vec<usize>,
}

type Input = Vec<Machine>;

fn get_input() -> Input {
    std::io::stdin()
    // .lines().collect::<Vec<_>>();
    // "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
// [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
// [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"
        .lines()
        .map(|line| {
            let line = line.unwrap();
            let parts: Vec<_> = line.split_whitespace().collect();

            let (lights, parts) = parts.split_first().unwrap();
            let (joltage, buttons) = parts.split_last().unwrap();

            let lights = lights[1..(lights.len() - 1)]
                .chars()
                .map(|light| light == '#')
                .collect();

            let buttons = buttons
                .iter()
                .map(|button| {
                    button[1..(button.len() - 1)]
                        .split(',')
                        .flat_map(str::parse)
                        .collect()
                })
                .collect();

            let joltage = joltage[1..(joltage.len() - 1)]
                .split(',')
                .flat_map(str::parse)
                .collect();

            Machine {
                lights,
                buttons,
                joltage,
            }
        })
        .collect()
}

fn write_array<T: std::fmt::Display>(name: &str, arr: &[T]) {
    print!("{name} = [");
    for (i, v) in arr.iter().enumerate() {
        if i != 0 {
            print!(", ");
        }
        print!("{v}");
    }
    println!("];");
}

fn write_dzn(input: Input) {
    println!("machine_id = _(1..{});", input.len());

    let mut current_light_offset = 0;
    let mut light_counts = vec![];
    let mut light_offsets = vec![];
    let mut lights = vec![];
    let mut joltages = vec![];

    let mut current_button_offset = 0;
    let mut button_counts = vec![];
    let mut button_offsets = vec![];
    let mut buttons = vec![];

    for machine in input {
        light_offsets.push(current_light_offset);
        let light_count = machine.lights.len();
        light_counts.push(light_count);
        current_light_offset += light_count;
        lights.extend(machine.lights.into_iter());
        joltages.extend(machine.joltage.into_iter());

        button_offsets.push(current_button_offset);
        button_counts.push(machine.buttons.len());
        current_button_offset += machine.buttons.len() * light_count;
        for button in machine.buttons {
            buttons.extend((0..light_count).map(|i| button.contains(&i)))
        }
    }

    write_array("light_counts", &light_counts);
    write_array("light_offsets", &light_offsets);
    write_array("lights", &lights);
    write_array("joltages", &joltages);

    write_array("button_counts", &button_counts);
    write_array("button_offsets", &button_offsets);
    write_array("buttons", &buttons);
}

pub fn main() {
    let input = get_input();
    write_dzn(input);
}
