# Advent of Code

Hi! This a repository for archiving my solutions for the Advent of Code events I've participated in.

I do this mostly for fun, and as such don't expect any optimal solutions, just ones that work. In fact, I apologize in advance for any horrendous code you may find here.

## Events

| Year |              Language              | Completion |
| :--- | :--------------------------------: | ---------: |
| 2025 |          Rust / MiniZinc           |       24 ★ |
| 2024 | [It's complicated](2024#languages) |       37 ★ |
| 2023 |               Python               |       31 ★ |
| 2022 |               Python               |       31 ★ |
| 2021 |               Python               |       35 ★ |
| 2020 |                                    |            |
| 2019 |                                    |            |
| 2018 |               Python               |       26 ★ |
| 2017 |               Python               |       50 ★ |
| 2016 |               Python               |       50 ★ |
| 2015 |               Python               |       50 ★ |

## Running

I use Nix to manage my solutions, along with some helper scripts to automatically fetch the inputs/expected outputs of each day.

To run a specific day, use the following command:

```sh
nix run '.#<year>.day<day>'
```

This will ask you for your advent of code session cookie, which you can copy from your browser. It will then fetch the required input and cache it for future uses.

For example, running day 3 of 2021 would look like this:

```sh
nix run '.#2021.day03'
```

To check if the output matches the expected output, use the following command:

```sh
nix run '.#<year>.day<day>.verify'
```

This will return 0 if the solution is correct, and will show a diff if it's not.
