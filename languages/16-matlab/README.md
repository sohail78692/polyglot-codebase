# MATLAB / GNU Octave Reference Guide

> **Category**: Scientific & Data  
> **Paradigm**: Array programming, procedural  
> **Initial Release**: 1984  
> **Created By**: Cleve Moler (MathWorks)  

---

## 1. Program 1: Hello World (`hello_world.m`)

```m
% ==========================================
% Program: Hello World in MATLAB / GNU Octave
% ==========================================
disp('Hello, World!');
```

### Explanation
`disp` prints values without variable names.

### Run Hello World
```bash
octave --silent hello_world.m
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.m`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```m
% ==========================================
% Program: Basic Operations in MATLAB / GNU Octave
% ==========================================
a = 20;
b = 6;

fprintf('a = %d, b = %d\n', a, b);
fprintf('Addition (a + b)        : %d\n', a + b);
fprintf('Subtraction (a - b)     : %d\n', a - b);
fprintf('Multiplication (a * b)  : %d\n', a * b);
fprintf('Division (a / b)        : %f\n', a / b);
fprintf('Integer Division (idiv) : %d\n', fix(a / b));
fprintf('Modulo (mod(a, b))      : %d\n', mod(a, b));
```

### Explanation
`fprintf` formats output; `fix(a / b)` truncates to integer; `mod(a, b)` calculates modulo.

### Run Basic Operations
```bash
octave --silent basic_operations.m
```
**Expected Output**:
```text
a = 20, b = 6
Addition (a + b)        : 26
Subtraction (a - b)     : 14
Multiplication (a * b)  : 120
Division (a / b)        : 3.333333
Integer Division (idiv) : 3
Modulo (mod(a, b))      : 2
```

---

## 3. Prerequisites & Installation

- **Guide**: MATLAB or GNU Octave
