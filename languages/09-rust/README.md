# Rust Reference Guide

> **Category**: Mainstream & Systems  
> **Paradigm**: Multi-paradigm (Concurrent, functional, imperative, generic)  
> **Initial Release**: 2015  
> **Created By**: Graydon Hoare (Mozilla Research)  

---

## 1. Program 1: Hello World (`hello_world.rs`)

```rs
// ==========================================
// Program: Hello World in Rust
// ==========================================
fn main() {
    println!("Hello, World!");
}
```

### Explanation
`println!` macro handles formatting at compile time.

### Run Hello World
```bash
rustc hello_world.rs && ./hello_world
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.rs`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```rs
// ==========================================
// Program: Basic Operations in Rust (+, -, *, /, %)
// ==========================================
fn main() {
    let a: i32 = 20;
    let b: i32 = 6;

    println!("a = {}, b = {}", a, b);
    println!("Addition (a + b)        : {}", a + b);
    println!("Subtraction (a - b)     : {}", a - b);
    println!("Multiplication (a * b)  : {}", a * b);
    println!("Integer Division (a / b): {}", a / b);
    println!("Float Division (f64)    : {}", (a as f64) / (b as f64));
    println!("Modulo (a % b)          : {}", a % b);
}
```

### Explanation
Rust checks for overflow and requires explicit casting `(a as f64)` for type safety.

### Run Basic Operations
```bash
rustc basic_operations.rs && ./basic_operations
```
**Expected Output**:
```text
a = 20, b = 6
Addition (a + b)        : 26
Subtraction (a - b)     : 14
Multiplication (a * b)  : 120
Integer Division (a / b): 3
Float Division (f64)    : 3.3333333333333335
Modulo (a % b)          : 2
```

---

## 3. Prerequisites & Installation

- **Guide**: rustup.rs

---

## 3. Program 3: Control Flow & Logic (`control_flow.rs`)
*Demonstrates conditional branching (`if/else`), pattern matching / multi-way `switch`, `for` iteration loops, and `while` loop.*

```rs
// ==========================================
// Program: Control Flow in Rust
// ==========================================

fn main() {
    // 1. Conditionals
    println!("Conditionals:");
    let num = 15;
    if num > 0 {
        if num % 2 == 0 {
            println!("{} is Positive and Even", num);
        } else {
            println!("{} is Positive and Odd", num);
        }
    } else if num < 0 {
        println!("{} is Negative", num);
    } else {
        println!("Number is Zero");
    }

    println!("\nPattern Matching / Switch:");
    // 2. Pattern Matching
    let grade = "B";
    let message = match grade {
        "A" => "Grade A: Excellent!",
        "B" => "Grade B: Good Job!",
        "C" => "Grade C: Fair",
        _   => "Keep Trying!",
    };
    println!("{}", message);

    // 3. For Loop (1..=5 inclusive)
    println!("\nFor Loop (1 to 5):");
    for i in 1..=5 {
        if i == 5 {
            println!("{}", i);
        } else {
            print!("{} ", i);
        }
    }

    // 4. While Loop
    println!("\nWhile Loop (Countdown):");
    let mut count = 3;
    while count > 0 {
        print!("{} ", count);
        count -= 1;
    }
    println!("Blastoff!");
}
```

### Explanation
Demonstrates Rust's expression-based `if/else`, exhaustive pattern `match`, range-based `for i in 1..=5`, and `while` loop.

### Run Control Flow
```bash
rustc control_flow.rs && ./control_flow
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
