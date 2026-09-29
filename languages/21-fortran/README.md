# Fortran Reference Guide

> **Category**: Scientific & Data  
> **Paradigm**: Array, imperative, procedural  
> **Initial Release**: 1957  
> **Created By**: John Backus (IBM)  

---

## 1. Program 1: Hello World (`hello_world.f90`)

```f90
! ==========================================
! Program: Hello World in Modern Fortran (90+)
! ==========================================
program hello_world
    implicit none
    print *, "Hello, World!"
end program hello_world
```

### Explanation
`print *` formats and writes to stdout.

### Run Hello World
```bash
gfortran hello_world.f90 -o hello_world && ./hello_world
```
**Expected Output**:
```text
 Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.f90`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```f90
! ==========================================
! Program: Basic Operations in Modern Fortran (+, -, *, /, mod)
! ==========================================
program basic_operations
    implicit none
    integer :: a, b

    a = 20
    b = 6

    print *, "a = 20, b = 6"
    print *, "Addition (a + b)        : ", a + b
    print *, "Subtraction (a - b)     : ", a - b
    print *, "Multiplication (a * b)  : ", a * b
    print *, "Integer Division (a / b): ", a / b
    print *, "Float Division (real)   : ", real(a) / real(b)
    print *, "Modulo (mod(a, b))      : ", mod(a, b)
end program basic_operations
```

### Explanation
`mod(a, b)` calculates remainder; `real(a) / real(b)` performs floating-point division.

### Run Basic Operations
```bash
gfortran basic_operations.f90 -o basic_operations && ./basic_operations
```
**Expected Output**:
```text
 a = 20, b = 6
 Addition (a + b)        : 26
 Subtraction (a - b)     : 14
 Multiplication (a * b)  : 120
 Integer Division (a / b): 3
 Float Division (real)   : 3.33333325
 Modulo (mod(a, b))      : 2
```

---

## 3. Prerequisites & Installation

- **Guide**: GFortran
