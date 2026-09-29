# Forth Reference Guide

> **Category**: Classic & Foundational  
> **Paradigm**: Stack-oriented, concatenative, procedural  
> **Initial Release**: 1970  
> **Created By**: Charles H. Moore  

---

## 1. Program 1: Hello World (`hello_world.fs`)

```fs
\ ==========================================
\ Program: Hello World in Forth
\ ==========================================
: HELLO ( -- )
  ." Hello, World!" CR ;

HELLO
```

### Explanation
Word definition `: HELLO ... ;` and print `." ..."`.

### Run Hello World
```bash
gforth hello_world.fs -e bye
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.fs`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```fs
\ ==========================================
\ Program: Basic Operations in Forth (+, -, *, /, MOD)
\ ==========================================
: OPERATIONS ( -- )
  ." a = 20, b = 6" CR
  ." Addition: " 20 6 + . CR
  ." Subtraction: " 20 6 - . CR
  ." Multiplication: " 20 6 * . CR
  ." Division: " 20 6 / . CR
  ." Modulo: " 20 6 MOD . CR ;

OPERATIONS
```

### Explanation
Forth is stack-based: `20 6 +` pushes 20 and 6, pops them to add, and `.` prints the top of the stack.

### Run Basic Operations
```bash
gforth basic_operations.fs -e bye
```
**Expected Output**:
```text
a = 20, b = 6
Addition: 26
Subtraction: 14
Multiplication: 120
Division: 3
Modulo: 2
```

---

## 3. Prerequisites & Installation

- **Guide**: Gforth
