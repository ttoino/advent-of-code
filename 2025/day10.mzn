enum machine_id;

array[machine_id] of int: light_counts;
array[machine_id] of int: light_offsets;
array[int] of bool: lights;
array[int] of int: joltages;

array[machine_id] of int: button_counts;
array[machine_id] of int: button_offsets;
array[int] of bool: buttons;

array[machine_id] of var int: part1_clicks;
var int: part1_result = sum(part1_clicks);

constraint forall(id in machine_id) (
    let {
        int: light_count = light_counts[id];
        int: light_offset = light_offsets[id];
        int: button_count = button_counts[id];
        int: button_offset = button_offsets[id];
        array[1..button_count] of var bool: my_clicks;
    } in (
        (
            part1_clicks[id] = sum(my_clicks)
        ) /\ (
            forall(j in 1..light_count) (
                lights[light_offset + j] <-> (xorall(i in 1..button_count) (
                    my_clicks[i] /\ buttons[button_offset + ((i - 1) * light_count + j)]
                ))
            )
        )
    )
);

array[machine_id] of var int: part2_clicks;
var int: part2_result = sum(part2_clicks);

constraint forall(click in part2_clicks) (click >= 0);

constraint forall(id in machine_id) (
    let {
        int: light_count = light_counts[id];
        int: light_offset = light_offsets[id];
        int: button_count = button_counts[id];
        int: button_offset = button_offsets[id];
        array[1..button_count] of var int: my_clicks;
    } in (
        (
            part2_clicks[id] = sum(my_clicks)
        ) /\ (
            forall(click in my_clicks) (click >= 0)
        ) /\ (
            forall(j in 1..light_count) (
                joltages[light_offset + j] = sum(i in 1..button_count) (
                    my_clicks[i] * buttons[button_offset + ((i - 1) * light_count + j)]
                )
            )
        )
    )
);

solve minimize part1_result + part2_result;

output [
    "Part 1: \(part1_result)\n",
    "Part 2: \(part2_result)\n"
];
