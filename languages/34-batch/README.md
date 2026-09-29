# Windows Batch Reference Guide

> **Category**: Shell & Scripting  
> **Paradigm**: Command script  
> **Initial Release**: 1981  
> **Created By**: Microsoft  

---

## 1. Program 1: Hello World (`hello_world.bat`)

```bat
@echo off
rem ==========================================
rem Program: Hello World in Windows Batch
rem ==========================================
echo Hello, World!
```

### Explanation
`@echo off` and `echo` print directly.

### Run Hello World
```bash
hello_world.bat
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.bat`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```bat
@echo off
rem ==========================================
rem Program: Basic Operations in Windows Batch (+, -, *, /, %%)
rem ==========================================
set a=20
set b=6

set /a add=a+b
set /a sub=a-b
set /a mul=a*b
set /a div=a/b
set /a mod=a%%b

echo a = %a%, b = %b%
echo Addition (a + b)        : %add%
echo Subtraction (a - b)     : %sub%
echo Multiplication (a * b)  : %mul%
echo Integer Division (a / b): %div%
echo Modulo (a %%%% b)          : %mod%
```

### Explanation
Batch uses `set /a` for arithmetic evaluations. Modulo inside batch scripts is escaped as `%%`.

### Run Basic Operations
```bash
basic_operations.bat
```
**Expected Output**:
```text
a = 20, b = 6
Addition (a + b)        : 26
Subtraction (a - b)     : 14
Multiplication (a * b)  : 120
Integer Division (a / b): 3
Modulo (a %% b)          : 2
```

---

## 3. Prerequisites & Installation

- **Guide**: Built-in Windows
