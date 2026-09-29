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
