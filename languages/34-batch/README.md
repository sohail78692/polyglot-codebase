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

---

## 3. Program 3: Control Flow & Logic (`control_flow.bat`)
*Demonstrates conditional branching (`if/else`), pattern matching / multi-way `switch`, `for` iteration loops, and `while` loop.*

```bat
@echo off
setlocal enabledelayedexpansion

:: ==========================================
:: Program: Control Flow in Windows Batch
:: ==========================================

echo Conditionals:
set num=15
set /a rem=num %% 2
if %num% GTR 0 (
    if !rem! EQU 0 (
        echo %num% is Positive and Even
    ) else (
        echo %num% is Positive and Odd
    )
) else (
    echo %num% is Not Positive
)

echo.
echo Pattern Matching / Switch:
set grade=B
if "%grade%"=="A" (
    echo Grade A: Excellent!
) else if "%grade%"=="B" (
    echo Grade B: Good Job!
) else (
    echo Keep Trying!
)

echo.
echo For Loop (1 to 5):
set for_line=
for /L %%i in (1,1,5) do (
    set for_line=!for_line!%%i 
)
echo !for_line:~0,-1!

echo.
echo While Loop (Countdown):
set count=3
set while_line=
:while_loop
if !count! GTR 0 (
    set while_line=!while_line!!count! 
    set /a count=!count!-1
    goto while_loop
)
echo !while_line!Blastoff!

endlocal
```

### Explanation
Demonstrates classic Windows Batch `IF / ELSE` logic, label jump pseudo-switch, `FOR /L` numeric loops, and `GOTO` countdown loop.

### Run Control Flow
```bash
control_flow.bat
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
