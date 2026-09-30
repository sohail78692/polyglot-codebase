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

---

## 3. Program 3: Control Flow & Logic (`control_flow.fs`)
*Demonstrates conditional branching (`if/else`), pattern matching / multi-way `switch`, `for` iteration loops, and `while` loop.*

```fs
\ ==========================================
\ Program: Control Flow in Forth
\ ==========================================

: check-num ( n -- )
    dup 0 > if
        dup 2 mod 0 = if
            . ." is Positive and Even" cr
        else
            . ." is Positive and Odd" cr
        then
    else
        drop ." Not positive" cr
    then ;

: check-grade ( c -- )
    case
        [char] A of ." Grade A: Excellent!" cr endof
        [char] B of ." Grade B: Good Job!" cr endof
        [char] C of ." Grade C: Fair" cr endof
        ." Keep Trying!" cr
    endcase ;

: for-loop ( -- )
    6 1 do
        i .
    loop cr ;

: while-countdown ( -- )
    3
    begin
        dup 0 >
    while
        dup .
        1 -
    repeat
    drop ." Blastoff!" cr ;

: main ( -- )
    ." Conditionals:" cr
    15 check-num
    cr
    ." Pattern Matching / Switch:" cr
    [char] B check-grade
    cr
    ." For Loop (1 to 5):" cr
    for-loop
    cr
    ." While Loop (Countdown):" cr
    while-countdown ;

main
```

### Explanation
Demonstrates Forth postfix stack branching `IF ... ELSE ... THEN`, `CASE ... OF ... ENDOF ... ENDCASE`, `DO ... LOOP`, and `BEGIN ... WHILE ... REPEAT`.

### Run Control Flow
```bash
gforth control_flow.fs -e bye
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
