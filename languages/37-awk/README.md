# AWK Reference Guide

> **Category**: Shell & Scripting  
> **Paradigm**: Data-driven, pattern scanning and processing  
> **Initial Release**: 1977  
> **Created By**: Alfred Aho et al.  

---

## 1. Program 1: Hello World (`hello_world.awk`)

```awk
# ==========================================
# Program: Hello World in AWK
# ==========================================
BEGIN {
    print "Hello, World!"
}
```

### Explanation
`BEGIN` block executes prior to input processing.

### Run Hello World
```bash
awk -f hello_world.awk /dev/null
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.awk`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```awk
# ==========================================
# Program: Basic Operations in AWK (+, -, *, /, %)
# ==========================================
BEGIN {
    a = 20
    b = 6

    printf "a = %d, b = %d\n", a, b
    printf "Addition (a + b)        : %d\n", a + b
    printf "Subtraction (a - b)     : %d\n", a - b
    printf "Multiplication (a * b)  : %d\n", a * b
    printf "Division (a / b)        : %f\n", a / b
    printf "Integer Division (int)  : %d\n", int(a / b)
    printf "Modulo (a %%%% b)          : %d\n", a % b
}
```

### Explanation
AWK performs floating division by default; `int(a / b)` yields the integer quotient.

### Run Basic Operations
```bash
awk -f basic_operations.awk /dev/null
```
**Expected Output**:
```text
a = 20, b = 6
Addition (a + b)        : 26
Subtraction (a - b)     : 14
Multiplication (a * b)  : 120
Division (a / b)        : 3.33333
Integer Division (int)  : 3
Modulo (a % b)          : 2
```

---

## 3. Prerequisites & Installation

- **Guide**: gawk
