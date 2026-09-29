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
