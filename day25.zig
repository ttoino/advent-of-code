const std = @import("std");

const Input = struct {
    locks: std.ArrayList([5]u8),
    keys: std.ArrayList([5]u8),
};

fn getInput() Input {
    const stdin = std.io.getStdIn().reader();
    var result = Input{
        .locks = std.ArrayList([5]u8).init(std.heap.page_allocator),
        .keys = std.ArrayList([5]u8).init(std.heap.page_allocator),
    };
    var line = [_]u8{0} ** 6;
    var value = [_]u8{0} ** 5;

    while (true) {
        for (0..7) |_| {
            _ = stdin.read(&line) catch {
                return result; // Return early if reading fails
            };

            for (line, 0..) |char, j| {
                if (char == '#') {
                    value[j] += 1;
                }
            }
        }

        if (line[0] == '#') {
            result.keys.append(value) catch {
                return result; // Return early if appending fails
            };
        } else {
            result.locks.append(value) catch {
                return result; // Return early if appending fails
            };
        }

        value = [_]u8{0} ** 5;

        _ = stdin.readByte() catch {
            break;
        };
    }

    return result;
}

fn solve(input: Input) usize {
    var matching: usize = 0;

    for (input.locks.items) |lock| {
        loop: for (input.keys.items) |key| {
            for (0..5) |i| {
                if (lock[i] + key[i] > 7) {
                    continue :loop;
                }
            }

            matching += 1;
        }
    }

    return matching;
}

pub fn main() void {
    const input = getInput();
    const result = solve(input);
    std.debug.print("{}\n", .{result});
}
