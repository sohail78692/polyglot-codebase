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
