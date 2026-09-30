# D Reference Guide

> **Category**: Scientific & Data  
> **Paradigm**: Multi-paradigm (OOP, generic, functional, imperative)  
> **Initial Release**: 2001  
> **Created By**: Walter Bright (Digital Mars)  

---

## 1. Program 1: Hello World (`hello_world.d`)

```d
// ==========================================
// Program: Hello World in D
// ==========================================
import std.stdio;

void main() {
    writeln("Hello, World!");
}
```

### Explanation
`writeln` writes to stdout.

### Run Hello World
```bash
dmd -run hello_world.d
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.d`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```d
// ==========================================
// Program: Basic Operations in D (+, -, *, /, %)
// ==========================================
import std.stdio;

void main() {
    int a = 20;
    int b = 6;

    writefln("a = %d, b = %d", a, b);
    writefln("Addition (a + b)        : %d", a + b);
    writefln("Subtraction (a - b)     : %d", a - b);
    writefln("Multiplication (a * b)  : %d", a * b);
    writefln("Integer Division (a / b): %d", a / b);
    writefln("Float Division (double) : %f", cast(double)a / b);
    writefln("Modulo (a % b)          : %d", a % b);
}
```

### Explanation
`cast(double)a` explicitly casts to double for floating-point division.

### Run Basic Operations
```bash
dmd -run basic_operations.d
```
**Expected Output**:
```text
a = 20, b = 6
Addition (a + b)        : 26
Subtraction (a - b)     : 14
Multiplication (a * b)  : 120
Integer Division (a / b): 3
Float Division (double) : 3.33333
Modulo (a % b)          : 2
```

---

## 3. Prerequisites & Installation

- **Guide**: dlang.org

---

## 3. Program 3: Control Flow & Logic (`control_flow.d`)
*Demonstrates conditional branching (`if/else`), pattern matching / multi-way `switch`, `for` iteration loops, and `while` loop.*

```d
// ==========================================
// Program: Control Flow in D
// ==========================================

import std.stdio;

void main() {
    // 1. Conditionals
    writeln("Conditionals:");
    int num = 15;
    if (num > 0) {
        if (num % 2 == 0) {
            writefln("%d is Positive and Even", num);
        } else {
            writefln("%d is Positive and Odd", num);
        }
    } else if (num < 0) {
        writefln("%d is Negative", num);
    } else {
        writeln("Number is Zero");
    }

    writeln("\nPattern Matching / Switch:");
    // 2. Switch Statement
    char grade = 'B';
    switch (grade) {
        case 'A':
            writeln("Grade A: Excellent!");
            break;
        case 'B':
            writeln("Grade B: Good Job!");
            break;
        case 'C':
            writeln("Grade C: Fair");
            break;
        default:
            writeln("Keep Trying!");
            break;
    }

    // 3. For Loop
    writeln("\nFor Loop (1 to 5):");
    foreach (i; 1 .. 6) {
        write(i, i == 5 ? "\n" : " ");
    }

    // 4. While Loop
    writeln("\nWhile Loop (Countdown):");
    int count = 3;
    while (count > 0) {
        write(count, " ");
        count--;
    }
    writeln("Blastoff!");
}
```

### Explanation
Demonstrates D language static typing with `if/else`, `switch/case` with `final switch`, `foreach` loops, and `while` loop.

### Run Control Flow
```bash
dmd -run control_flow.d
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
