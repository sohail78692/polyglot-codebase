# Smalltalk Reference Guide

> **Category**: Classic & Foundational  
> **Paradigm**: Pure object-oriented, message passing  
> **Initial Release**: 1972  
> **Created By**: Alan Kay et al. (Xerox PARC)  

---

## 1. Program 1: Hello World (`hello_world.st`)

```st
"==========================================
 Program: Hello World in Smalltalk
 =========================================="
Transcript show: 'Hello, World!'; cr.
```

### Explanation
`Transcript show: '...'; cr.` message sending.

### Run Hello World
```bash
gst hello_world.st
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.st`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```st
"==========================================
 Program: Basic Operations in Smalltalk (+, -, *, //, \\)
 =========================================="
| a b |
a := 20.
b := 6.

Transcript show: 'a = 20, b = 6'; cr.
Transcript show: 'Addition (a + b)        : ', (a + b) printString; cr.
Transcript show: 'Subtraction (a - b)     : ', (a - b) printString; cr.
Transcript show: 'Multiplication (a * b)  : ', (a * b) printString; cr.
Transcript show: 'Integer Division (//)   : ', (a // b) printString; cr.
Transcript show: 'Exact Fraction (/)      : ', (a / b) printString; cr.
Transcript show: 'Modulo (\\)             : ', (a \\ b) printString; cr.
```

### Explanation
In Smalltalk, `+`, `-`, `*` are binary messages sent to number objects. `//` is integer division, `/` yields a Fraction, and `\\` calculates modulo.

### Run Basic Operations
```bash
gst basic_operations.st
```
**Expected Output**:
```text
a = 20, b = 6
Addition (a + b)        : 26
Subtraction (a - b)     : 14
Multiplication (a * b)  : 120
Integer Division (//)   : 3
Exact Fraction (/)      : (10/3)
Modulo (\\)             : 2
```

---

## 3. Prerequisites & Installation

- **Guide**: GNU Smalltalk (gst)
