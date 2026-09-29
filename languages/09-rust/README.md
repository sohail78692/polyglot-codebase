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
