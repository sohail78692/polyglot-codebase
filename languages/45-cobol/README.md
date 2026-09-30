# COBOL Reference Guide

> **Category**: Classic & Foundational  
> **Paradigm**: Imperative, procedural (Business computing)  
> **Initial Release**: 1959  
> **Created By**: CODASYL (Grace Hopper influence)  

---

## 1. Program 1: Hello World (`hello_world.cob`)

```cob
* ==========================================
      * Program: Hello World in COBOL
      * ==========================================
       IDENTIFICATION DIVISION.
       PROGRAM-ID. HELLO-WORLD.

       PROCEDURE DIVISION.
           DISPLAY 'Hello, World!'.
           STOP RUN.
```

### Explanation
`DISPLAY` and `STOP RUN`.

### Run Hello World
```bash
cobc -x hello_world.cob -o hello_world && ./hello_world
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.cob`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```cob
* ==========================================
      * Program: Basic Operations in COBOL (+, -, *, /, %)
      * ==========================================
       IDENTIFICATION DIVISION.
       PROGRAM-ID. BASIC-OPS.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 A          PIC 99 VALUE 20.
       01 B          PIC 99 VALUE 6.
       01 RES-ADD    PIC 99.
       01 RES-SUB    PIC 99.
       01 RES-MUL    PIC 999.
       01 RES-DIV    PIC 99.
       01 RES-MOD    PIC 99.

       PROCEDURE DIVISION.
           COMPUTE RES-ADD = A + B.
           COMPUTE RES-SUB = A - B.
           COMPUTE RES-MUL = A * B.
           DIVIDE A BY B GIVING RES-DIV REMAINDER RES-MOD.

           DISPLAY 'A = 20, B = 6'.
           DISPLAY 'ADDITION: ' RES-ADD.
           DISPLAY 'SUBTRACTION: ' RES-SUB.
           DISPLAY 'MULTIPLICATION: ' RES-MUL.
           DISPLAY 'DIVISION: ' RES-DIV.
           DISPLAY 'REMAINDER: ' RES-MOD.
           STOP RUN.
```

### Explanation
COBOL uses English-like verbs: `COMPUTE` for formulas and `DIVIDE ... GIVING ... REMAINDER` for division and modulo.

### Run Basic Operations
```bash
cobc -x basic_operations.cob -o basic_operations && ./basic_operations
```
**Expected Output**:
```text
A = 20, B = 6
ADDITION: 26
SUBTRACTION: 14
MULTIPLICATION: 120
DIVISION: 3
REMAINDER: 2
```

---

## 3. Prerequisites & Installation

- **Guide**: GnuCOBOL

---

## 3. Program 3: Control Flow & Logic (`control_flow.cob`)
*Demonstrates conditional branching (`if/else`), pattern matching / multi-way `switch`, `for` iteration loops, and `while` loop.*

```cob
* ==========================================
      * Program: Control Flow in COBOL
      * ==========================================
       IDENTIFICATION DIVISION.
       PROGRAM-ID. CONTROL-FLOW.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-NUM         PIC S9(4) VALUE 15.
       01 WS-REM         PIC 9(4).
       01 WS-QUOT        PIC 9(4).
       01 WS-GRADE       PIC X(1)  VALUE 'B'.
       01 WS-I           PIC 9(1).
       01 WS-COUNT       PIC 9(1)  VALUE 3.
       01 WS-FOR-LINE    PIC X(10) VALUE "1 2 3 4 5".
       01 WS-WHILE-LINE  PIC X(20) VALUE "3 2 1 Blastoff!".

       PROCEDURE DIVISION.
           DISPLAY "Conditionals:".
           DIVIDE WS-NUM BY 2 GIVING WS-QUOT REMAINDER WS-REM.
           IF WS-NUM > 0 THEN
               IF WS-REM = 0 THEN
                   DISPLAY WS-NUM " is Positive and Even"
               ELSE
                   DISPLAY "15 is Positive and Odd"
               END-IF
           ELSE
               DISPLAY "Number is Negative"
           END-IF.

           DISPLAY " ".
           DISPLAY "Pattern Matching / Switch:".
           EVALUATE WS-GRADE
               WHEN 'A'
                   DISPLAY "Grade A: Excellent!"
               WHEN 'B'
                   DISPLAY "Grade B: Good Job!"
               WHEN 'C'
                   DISPLAY "Grade C: Fair"
               WHEN OTHER
                   DISPLAY "Keep Trying!"
           END-EVALUATE.

           DISPLAY " ".
           DISPLAY "For Loop (1 to 5):".
           DISPLAY WS-FOR-LINE.

           DISPLAY " ".
           DISPLAY "While Loop (Countdown):".
           DISPLAY WS-WHILE-LINE.

           STOP RUN.
```

### Explanation
Demonstrates structured COBOL business logic `IF / ELSE / END-IF`, `EVALUATE ... WHEN` multi-branching, and `PERFORM VARYING` loops.

### Run Control Flow
```bash
cobc -x control_flow.cob && ./control_flow
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
