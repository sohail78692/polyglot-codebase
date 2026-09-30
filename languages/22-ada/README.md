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

---

## 3. Program 3: Control Flow & Logic (`control_flow.adb`)
*Demonstrates conditional branching (`if/else`), pattern matching / multi-way `switch`, `for` iteration loops, and `while` loop.*

```adb
-- ==========================================
-- Program: Control Flow in Ada
-- ==========================================

with Ada.Text_IO; use Ada.Text_IO;
with Ada.Integer_Text_IO; use Ada.Integer_Text_IO;

procedure Control_Flow is
   Num   : Integer := 15;
   Grade : Character := 'B';
   Count : Integer := 3;
begin
   -- 1. Conditionals
   Put_Line ("Conditionals:");
   if Num > 0 then
      if Num mod 2 = 0 then
         Put (Num, Width => 0);
         Put_Line (" is Positive and Even");
      else
         Put (Num, Width => 0);
         Put_Line (" is Positive and Odd");
      end if;
   elsif Num < 0 then
      Put (Num, Width => 0);
      Put_Line (" is Negative");
   else
      Put_Line ("Number is Zero");
   end if;

   New_Line;
   Put_Line ("Pattern Matching / Switch:");
   -- 2. Case statement
   case Grade is
      when 'A' =>
         Put_Line ("Grade A: Excellent!");
      when 'B' =>
         Put_Line ("Grade B: Good Job!");
      when 'C' =>
         Put_Line ("Grade C: Fair");
      when others =>
         Put_Line ("Keep Trying!");
   end case;

   New_Line;
   Put_Line ("For Loop (1 to 5):");
   -- 3. For loop
   for I in 1 .. 5 loop
      Put (I, Width => 0);
      if I = 5 then
         New_Line;
      else
         Put (" ");
      end if;
   end loop;

   New_Line;
   Put_Line ("While Loop (Countdown):");
   -- 4. While loop
   while Count > 0 loop
      Put (Count, Width => 0);
      Put (" ");
      Count := Count - 1;
   end loop;
   Put_Line ("Blastoff!");
end Control_Flow;
```

### Explanation
Demonstrates Ada strongly typed `if/elsif/else`, exhaustive `case/when` statements, `for` range loops, and `while` loops.

### Run Control Flow
```bash
gnatmake control_flow.adb && ./control_flow
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
