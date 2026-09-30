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

---

## 3. Program 3: Control Flow & Logic (`control_flow.v`)
*Demonstrates conditional branching (`if/else`), pattern matching / multi-way `switch`, `for` iteration loops, and `while` loop.*

```v
// ==========================================
// Program: Control Flow in V (Vlang)
// ==========================================

fn main() {
    // 1. Conditionals
    println("Conditionals:")
    num := 15
    if num > 0 {
        if num % 2 == 0 {
            println("${num} is Positive and Even")
        } else {
            println("${num} is Positive and Odd")
        }
    } else if num < 0 {
        println("${num} is Negative")
    } else {
        println("Number is Zero")
    }

    println("\nPattern Matching / Switch:")
    // 2. Match Expression
    grade := "B"
    msg := match grade {
        "A" { "Grade A: Excellent!" }
        "B" { "Grade B: Good Job!" }
        "C" { "Grade C: Fair" }
        else { "Keep Trying!" }
    }
    println(msg)

    // 3. For Loop
    println("\nFor Loop (1 to 5):")
    for i in 1 .. 6 {
        print("${i}${if i == 5 { "\n" } else { " " }}")
    }

    // 4. While Loop (using 'for condition')
    println("\nWhile Loop (Countdown):")
    mut count := 3
    for count > 0 {
        print("${count} ")
        count--
    }
    println("Blastoff!")
}
```

### Explanation
Demonstrates V language fast compilation, `match` expressions, range `for` loops, and condition-only `for` (while).

### Run Control Flow
```bash
v run control_flow.v
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
