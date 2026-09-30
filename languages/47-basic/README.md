# BASIC Reference Guide

> **Category**: Classic & Foundational  
> **Paradigm**: Imperative, procedural  
> **Initial Release**: 1964  
> **Created By**: John G. Kemeny & Thomas E. Kurtz  

---

## 1. Program 1: Hello World (`hello_world.bas`)

```bas
10 REM ==========================================
20 REM Program: Hello World in Classic BASIC
30 REM ==========================================
40 PRINT "Hello, World!"
50 END
```

### Explanation
`PRINT` and numbered lines in classic Dartmouth/QuickBASIC.

### Run Hello World
```bash
fbc -lang qb hello_world.bas && ./hello_world
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.bas`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```bas
10 REM ==========================================
20 REM Program: Basic Operations in Classic BASIC (+, -, *, \, MOD)
30 REM ==========================================
40 A = 20
50 B = 6
60 PRINT "a = 20, b = 6"
70 PRINT "Addition: "; A + B; ", Subtraction: "; A - B; ", Multiplication: "; A * B; ", Division: "; A \ B; ", Modulo: "; A MOD B
80 END
```

### Explanation
BASIC uses `\` for integer division, `/` for floating division, and `MOD` for remainder.

### Run Basic Operations
```bash
fbc -lang qb basic_operations.bas && ./basic_operations
```
**Expected Output**:
```text
a = 20, b = 6
Addition: 26, Subtraction: 14, Multiplication: 120, Division: 3, Modulo: 2
```

---

## 3. Prerequisites & Installation

- **Guide**: FreeBASIC

---

## 3. Program 3: Control Flow & Logic (`control_flow.bas`)
*Demonstrates conditional branching (`if/else`), pattern matching / multi-way `switch`, `for` iteration loops, and `while` loop.*

```bas
REM ==========================================
REM Program: Control Flow in BASIC (FreeBASIC)
REM ==========================================

Sub Main()
    ' 1. Conditionals
    Print "Conditionals:"
    Dim num As Integer = 15
    If num > 0 Then
        If num Mod 2 = 0 Then
            Print num; " is Positive and Even"
        Else
            Print num; " is Positive and Odd"
        End If
    ElseIf num < 0 Then
        Print num; " is Negative"
    Else
        Print "Number is Zero"
    End If

    Print ""
    Print "Pattern Matching / Switch:"
    ' 2. Select Case
    Dim grade As String = "B"
    Select Case grade
        Case "A"
            Print "Grade A: Excellent!"
        Case "B"
            Print "Grade B: Good Job!"
        Case "C"
            Print "Grade C: Fair"
        Case Else
            Print "Keep Trying!"
    End Select

    Print ""
    Print "For Loop (1 to 5):"
    ' 3. For Loop
    For i As Integer = 1 To 5
        If i = 5 Then
            Print Str(i)
        Else
            Print Str(i) + " ";
        End If
    Next i

    Print ""
    Print "While Loop (Countdown):"
    ' 4. While Loop
    Dim count As Integer = 3
    While count > 0
        Print Str(count) + " ";
        count = count - 1
    Wend
    Print "Blastoff!"
End Sub

Main()
```

### Explanation
Demonstrates FreeBASIC / classic BASIC `IF / THEN / ELSE`, `SELECT CASE` multi-branching, `FOR / NEXT` range loops, and `WHILE / WEND` countdown.

### Run Control Flow
```bash
fbc control_flow.bas && ./control_flow
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
