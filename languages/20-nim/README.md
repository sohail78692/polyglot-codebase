# Nim Reference Guide

> **Category**: Scientific & Data  
> **Paradigm**: Multi-paradigm (Metaprogramming, functional, procedural)  
> **Initial Release**: 2008  
> **Created By**: Andreas Rumpf  

---

## 1. Program 1: Hello World (`hello_world.nim`)

```nim
# ==========================================
# Program: Hello World in Nim
# ==========================================
echo "Hello, World!"
```

### Explanation
`echo` outputs to stdout with a newline.

### Run Hello World
```bash
nim compile --run hello_world.nim
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.nim`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```nim
# ==========================================
# Program: Basic Operations in Nim (+, -, *, /, div, mod)
# ==========================================
let a = 20
let b = 6

echo "a = ", a, ", b = ", b
echo "Addition (a + b)        : ", a + b
echo "Subtraction (a - b)     : ", a - b
echo "Multiplication (a * b)  : ", a * b
echo "Float Division (a / b)  : ", a / b     # '/' returns a float
echo "Integer Division (div)  : ", a div b   # 'div' is integer division
echo "Modulo (mod)            : ", a mod b   # 'mod' is modulo
```

### Explanation
Nim uses `div` for integer division and `mod` for remainder.

### Run Basic Operations
```bash
nim compile --run basic_operations.nim
```
**Expected Output**:
```text
a = 20, b = 6
Addition (a + b)        : 26
Subtraction (a - b)     : 14
Multiplication (a * b)  : 120
Float Division (a / b)  : 3.333333333333334
Integer Division (div)  : 3
Modulo (mod)            : 2
```

---

## 3. Prerequisites & Installation

- **Guide**: nim-lang.org
