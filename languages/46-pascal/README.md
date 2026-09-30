# Pascal Reference Guide

> **Category**: Classic & Foundational  
> **Paradigm**: Imperative, structured, procedural  
> **Initial Release**: 1970  
> **Created By**: Niklaus Wirth  

---

## 1. Program 1: Hello World (`hello_world.pas`)

```pas
(* ==========================================
   Program: Hello World in Pascal
   ========================================== *)
program HelloWorld;
begin
    writeln('Hello, World!');
end.
```

### Explanation
`writeln` formats output to next line.

### Run Hello World
```bash
fpc hello_world.pas && ./hello_world
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.pas`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```pas
(* ==========================================
   Program: Basic Operations in Pascal (+, -, *, /, div, mod)
   ========================================== *)
program BasicOperations;
var
    a, b: integer;
begin
    a := 20;
    b := 6;

    writeln('a = 20, b = 6');
    writeln('Addition (a + b)        : ', a + b);
    writeln('Subtraction (a - b)     : ', a - b);
    writeln('Multiplication (a * b)  : ', a * b);
    writeln('Integer Division (div)  : ', a div b);
    writeln('Float Division (/)      : ', (a / b):0:2);
    writeln('Modulo (mod)            : ', a mod b);
end.
```

### Explanation
Pascal uses `div` for integer quotient, `/` for real division, and `mod` for remainder.

### Run Basic Operations
```bash
fpc basic_operations.pas && ./basic_operations
```
**Expected Output**:
```text
a = 20, b = 6
Addition (a + b)        : 26
Subtraction (a - b)     : 14
Multiplication (a * b)  : 120
Integer Division (div)  : 3
Float Division (/)      : 3.33
Modulo (mod)            : 2
```

---

## 3. Prerequisites & Installation

- **Guide**: Free Pascal Compiler (FPC)

---

## 3. Program 3: Control Flow & Logic (`control_flow.pas`)
*Demonstrates conditional branching (`if/else`), pattern matching / multi-way `switch`, `for` iteration loops, and `while` loop.*

```pas
// ==========================================
// Program: Control Flow in Pascal
// ==========================================

program ControlFlow;

var
  Num, I, Count: Integer;
  Grade: Char;

begin
  // 1. Conditionals
  WriteLn('Conditionals:');
  Num := 15;
  if Num > 0 then
  begin
    if Num mod 2 = 0 then
      WriteLn(Num, ' is Positive and Even')
    else
      WriteLn(Num, ' is Positive and Odd');
  end
  else if Num < 0 then
    WriteLn(Num, ' is Negative')
  else
    WriteLn('Number is Zero');

  WriteLn;
  WriteLn('Pattern Matching / Switch:');
  // 2. Case Statement
  Grade := 'B';
  case Grade of
    'A': WriteLn('Grade A: Excellent!');
    'B': WriteLn('Grade B: Good Job!');
    'C': WriteLn('Grade C: Fair');
  else
    WriteLn('Keep Trying!');
  end;

  WriteLn;
  WriteLn('For Loop (1 to 5):');
  // 3. For Loop
  for I := 1 to 5 do
  begin
    Write(I);
    if I = 5 then
      WriteLn
    else
      Write(' ');
  end;

  WriteLn;
  WriteLn('While Loop (Countdown):');
  // 4. While Loop
  Count := 3;
  while Count > 0 do
  begin
    Write(Count, ' ');
    Count := Count - 1;
  end;
  WriteLn('Blastoff!');
end.
```

### Explanation
Demonstrates Pascal structured block `if/then/else`, `case ... of` selector, `for i := 1 to 5 do` loop, and `while` loop.

### Run Control Flow
```bash
fpc control_flow.pas && ./control_flow
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
