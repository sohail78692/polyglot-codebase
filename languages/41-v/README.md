# V (Vlang) Reference Guide

> **Category**: Web3, Mobile & Modern  
> **Paradigm**: Static, procedural, safe systems language  
> **Initial Release**: 2019  
> **Created By**: Alexander Medvednikov  

---

## 1. Program 1: Hello World (`hello_world.v`)

```v
// ==========================================
// Program: Hello World in V (Vlang)
// ==========================================
fn main() {
    println('Hello, World!')
}
```

### Explanation
`println` writes text followed by newline.

### Run Hello World
```bash
v run hello_world.v
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.v`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```v
// ==========================================
// Program: Basic Operations in V (+, -, *, /, %)
// ==========================================
fn main() {
    a := 20
    b := 6

    println('a = $a, b = $b')
    println('Addition (a + b)        : ${a + b}')
    println('Subtraction (a - b)     : ${a - b}')
    println('Multiplication (a * b)  : ${a * b}')
    println('Integer Division (a / b): ${a / b}')
    println('Float Division (f64)    : ${f64(a) / f64(b)}')
    println('Modulo (a % b)          : ${a % b}')
}
```

### Explanation
V uses string interpolation `${...}` and `f64(a)` for float conversion.

### Run Basic Operations
```bash
v run basic_operations.v
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

- **Guide**: vlang.io
