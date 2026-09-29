// ==========================================
// Program: Basic Operations in Zig (+, -, *, @divTrunc, @rem)
// ==========================================
const std = @import("std");

pub fn main() !void {
    const stdout = std.io.getStdOut().writer();
    const a: i32 = 20;
    const b: i32 = 6;

    try stdout.print("a = {d}, b = {d}\n", .{a, b});
    try stdout.print("Addition (a + b)        : {d}\n", .{a + b});
    try stdout.print("Subtraction (a - b)     : {d}\n", .{a - b});
    try stdout.print("Multiplication (a * b)  : {d}\n", .{a * b});
    try stdout.print("Integer Division (div)  : {d}\n", .{@divTrunc(a, b)});
    try stdout.print("Float Division          : {d}\n", .{@as(f64, @floatFromInt(a)) / @as(f64, @floatFromInt(b))});
    try stdout.print("Modulo (@rem)           : {d}\n", .{@rem(a, b)});
}
