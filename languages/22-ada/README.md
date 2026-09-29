# Ada Reference Guide

> **Category**: Scientific & Data  
> **Paradigm**: Multi-paradigm (Strongly typed, concurrent, OOP)  
> **Initial Release**: 1980  
> **Created By**: Jean Ichbiah  

---

## 1. Program 1: Hello World (`hello_world.adb`)

```adb
-- ==========================================
-- Program: Hello World in Ada
-- ==========================================
with Ada.Text_IO; use Ada.Text_IO;

procedure Hello_World is
begin
    Put_Line ("Hello, World!");
end Hello_World;
```

### Explanation
`Put_Line` writes to stdout.

### Run Hello World
```bash
gnatmake hello_world.adb && ./hello_world
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.adb`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```adb
-- ==========================================
-- Program: Basic Operations in Ada (+, -, *, /, mod)
-- ==========================================
with Ada.Text_IO; use Ada.Text_IO;
with Ada.Integer_Text_IO; use Ada.Integer_Text_IO;

procedure Basic_Operations is
    A : Integer := 20;
    B : Integer := 6;
begin
    Put_Line ("a = 20, b = 6");
    Put ("Addition (a + b)        : "); Put (A + B); New_Line;
    Put ("Subtraction (a - b)     : "); Put (A - B); New_Line;
    Put ("Multiplication (a * b)  : "); Put (A * B); New_Line;
    Put ("Integer Division (a / b): "); Put (A / B); New_Line;
    Put ("Modulo (a mod b)        : "); Put (A mod B); New_Line;
end Basic_Operations;
```

### Explanation
Ada uses `mod` keyword for modulo and `Integer_Text_IO` for formatted integer output.

### Run Basic Operations
```bash
gnatmake basic_operations.adb && ./basic_operations
```
**Expected Output**:
```text
a = 20, b = 6
Addition (a + b)        :  26
Subtraction (a - b)     :  14
Multiplication (a * b)  :  120
Integer Division (a / b):  3
Modulo (a mod b)        :  2
```

---

## 3. Prerequisites & Installation

- **Guide**: GNAT Ada Compiler
