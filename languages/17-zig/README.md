# Zig Reference Guide

> **Category**: Scientific & Data  
> **Paradigm**: Imperative, Systems  
> **Initial Release**: 2016  
> **Created By**: Andrew Kelley  

---

## 1. Program 1: Hello World (`hello_world.zig`)

```zig
// ==========================================
// Program: Hello World in Zig
// ==========================================
const std = @import("std");

pub fn main() !void {
    const stdout = std.io.getStdOut().writer();
    try stdout.print("Hello, World!\n", .{});
}
```

### Explanation
Explicit error handling using `try` and `@import("std")`.

### Run Hello World
```bash
zig run hello_world.zig
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.zig`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```zig
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
```

### Explanation
Zig uses builtins like `@divTrunc` and `@rem` for integer division and remainder with no hidden overflow.

### Run Basic Operations
```bash
zig run basic_operations.zig
```
**Expected Output**:
```text
a = 20, b = 6
Addition (a + b)        : 26
Subtraction (a - b)     : 14
Multiplication (a * b)  : 120
Integer Division (div)  : 3
Float Division          : 3.3333333333333335
Modulo (@rem)           : 2
```

---

## 3. Prerequisites & Installation

- **Guide**: ziglang.org

---

## 3. Program 3: Control Flow & Logic (`control_flow.zig`)
*Demonstrates conditional branching (`if/else`), pattern matching / multi-way `switch`, `for` iteration loops, and `while` loop.*

```zig
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
```

### Explanation
Demonstrates Zig's compile-time enforced safety, exhaustive `switch`, `while` with continue expressions, and range loops.

### Run Control Flow
```bash
zig run control_flow.zig
```
**Expected Output**:
```text
Conditionals:
15 is Positive and Odd

Pattern Matching / Switch:
Grade B: Good Job!

For Loop (1 to 5):
1 2 3 4 5

While Loop (Countdown):
3 2 1 Blastoff!
```
