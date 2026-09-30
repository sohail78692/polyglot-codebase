// ==========================================
// Program: Control Flow in Zig
// ==========================================

const std = @import("std");

pub fn main() !void {
    const stdout = std.io.getStdOut().writer();

    // 1. Conditionals
    try stdout.print("Conditionals:\n", .{});
    const num: i32 = 15;
    if (num > 0) {
        if (@mod(num, 2) == 0) {
            try stdout.print("{d} is Positive and Even\n", .{num});
        } else {
            try stdout.print("{d} is Positive and Odd\n", .{num});
        }
    } else if (num < 0) {
        try stdout.print("{d} is Negative\n", .{num});
    } else {
        try stdout.print("Number is Zero\n", .{});
    }

    try stdout.print("\nPattern Matching / Switch:\n", .{});
    // 2. Exhaustive Switch
    const grade: u8 = 'B';
    switch (grade) {
        'A' => try stdout.print("Grade A: Excellent!\n", .{}),
        'B' => try stdout.print("Grade B: Good Job!\n", .{}),
        'C' => try stdout.print("Grade C: Fair\n", .{}),
        else => try stdout.print("Keep Trying!\n", .{}),
    }

    // 3. For Loop with range
    try stdout.print("\nFor Loop (1 to 5):\n", .{});
    var i: usize = 1;
    while (i <= 5) : (i += 1) {
        try stdout.print("{d}{s}", .{ i, if (i == 5) "\n" else " " });
    }

    // 4. While Loop Countdown
    try stdout.print("\nWhile Loop (Countdown):\n", .{});
    var count: i32 = 3;
    while (count > 0) : (count -= 1) {
        try stdout.print("{d} ", .{count});
    }
    try stdout.print("Blastoff!\n", .{});
}
