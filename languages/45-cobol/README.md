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
