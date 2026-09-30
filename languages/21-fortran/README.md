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

---

## 3. Program 3: Control Flow & Logic (`control_flow.f90`)
*Demonstrates conditional branching (`if/else`), pattern matching / multi-way `switch`, `for` iteration loops, and `while` loop.*

```f90
! ==========================================
! Program: Control Flow in Fortran
! ==========================================

program control_flow
    implicit none
    integer :: num, i, count
    character(len=1) :: grade

    ! 1. Conditionals
    print *, "Conditionals:"
    num = 15
    if (num > 0) then
        if (mod(num, 2) == 0) then
            print '(I0, A)', num, " is Positive and Even"
        else
            print '(I0, A)', num, " is Positive and Odd"
        end if
    else if (num < 0) then
        print '(I0, A)', num, " is Negative"
    else
        print *, "Number is Zero"
    end if

    print *, ""
    print *, "Pattern Matching / Switch:"
    ! 2. Select Case
    grade = 'B'
    select case (grade)
        case ('A')
            print *, "Grade A: Excellent!"
        case ('B')
            print *, "Grade B: Good Job!"
        case ('C')
            print *, "Grade C: Fair"
        case default
            print *, "Keep Trying!"
    end select

    print *, ""
    print *, "For Loop (1 to 5):"
    ! 3. Do Loop (For Loop equivalent)
    do i = 1, 5
        if (i == 5) then
            write(*, '(I0)') i
        else
            write(*, '(I0, 1X)', advance='no') i
        end if
    end do

    print *, ""
    print *, "While Loop (Countdown):"
    ! 4. Do While Loop
    count = 3
    do while (count > 0)
        write(*, '(I0, 1X)', advance='no') count
        count = count - 1
    end do
    print *, "Blastoff!"

end program control_flow
```

### Explanation
Demonstrates modern Fortran `if/else if/else`, `select case` construct, `do` loops with stride, and `do while` loops.

### Run Control Flow
```bash
gfortran control_flow.f90 -o control_flow && ./control_flow
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
