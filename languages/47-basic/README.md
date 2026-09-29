# BASIC Reference Guide

> **Category**: Classic & Foundational  
> **Paradigm**: Imperative, procedural  
> **Initial Release**: 1964  
> **Created By**: John G. Kemeny & Thomas E. Kurtz  

---

## 1. Program 1: Hello World (`hello_world.bas`)

```bas
10 REM ==========================================
20 REM Program: Hello World in Classic BASIC
30 REM ==========================================
40 PRINT "Hello, World!"
50 END
```

### Explanation
`PRINT` and numbered lines in classic Dartmouth/QuickBASIC.

### Run Hello World
```bash
fbc -lang qb hello_world.bas && ./hello_world
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.bas`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```bas
10 REM ==========================================
20 REM Program: Basic Operations in Classic BASIC (+, -, *, \, MOD)
30 REM ==========================================
40 A = 20
50 B = 6
60 PRINT "a = 20, b = 6"
70 PRINT "Addition: "; A + B; ", Subtraction: "; A - B; ", Multiplication: "; A * B; ", Division: "; A \ B; ", Modulo: "; A MOD B
80 END
```

### Explanation
BASIC uses `\` for integer division, `/` for floating division, and `MOD` for remainder.

### Run Basic Operations
```bash
fbc -lang qb basic_operations.bas && ./basic_operations
```
**Expected Output**:
```text
a = 20, b = 6
Addition: 26, Subtraction: 14, Multiplication: 120, Division: 3, Modulo: 2
```

---

## 3. Prerequisites & Installation

- **Guide**: FreeBASIC
