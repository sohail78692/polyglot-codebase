# PowerShell Reference Guide

> **Category**: Shell & Scripting  
> **Paradigm**: Task-based command-line shell & scripting language  
> **Initial Release**: 2006  
> **Created By**: Jeffrey Snover (Microsoft)  

---

## 1. Program 1: Hello World (`hello_world.ps1`)

```ps1
# ==========================================
# Program: Hello World in PowerShell
# ==========================================
Write-Output "Hello, World!"
```

### Explanation
`Write-Output` sends objects to output pipeline.

### Run Hello World
```bash
powershell -ExecutionPolicy Bypass -File hello_world.ps1
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.ps1`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```ps1
# ==========================================
# Program: Basic Operations in PowerShell (+, -, *, /, %)
# ==========================================
$a = 20
$b = 6

Write-Output "a = $a, b = $b"
Write-Output "Addition (a + b)        : $($a + $b)"
Write-Output "Subtraction (a - b)     : $($a - $b)"
Write-Output "Multiplication (a * b)  : $($a * $b)"
Write-Output "Division (a / b)        : $($a / $b)"
Write-Output "Integer Division ([int]): $([Math]::Floor($a / $b))"
Write-Output "Modulo (a % b)          : $($a % $b)"
```

### Explanation
PowerShell embeds subexpressions using `$($a + $b)` and leverages .NET `[Math]::Floor`.

### Run Basic Operations
```bash
powershell -ExecutionPolicy Bypass -File basic_operations.ps1
```
**Expected Output**:
```text
a = 20, b = 6
Addition (a + b)        : 26
Subtraction (a - b)     : 14
Multiplication (a * b)  : 120
Division (a / b)        : 3.33333333333333
Integer Division ([int]): 3
Modulo (a % b)          : 2
```

---

## 3. Prerequisites & Installation

- **Guide**: Built-in Windows / pwsh

---

## 3. Program 3: Control Flow & Logic (`control_flow.ps1`)
*Demonstrates conditional branching (`if/else`), pattern matching / multi-way `switch`, `for` iteration loops, and `while` loop.*

```ps1
# ==========================================
# Program: Control Flow in PowerShell
# ==========================================

function Main {
    # 1. Conditionals
    Write-Host "Conditionals:"
    $num = 15
    if ($num -gt 0) {
        if ($num % 2 -eq 0) {
            Write-Host "$num is Positive and Even"
        } else {
            Write-Host "$num is Positive and Odd"
        }
    } elseif ($num -lt 0) {
        Write-Host "$num is Negative"
    } else {
        Write-Host "Number is Zero"
    }

    Write-Host "`nPattern Matching / Switch:"
    # 2. Switch Statement
    $grade = "B"
    switch ($grade) {
        "A" { Write-Host "Grade A: Excellent!" }
        "B" { Write-Host "Grade B: Good Job!" }
        "C" { Write-Host "Grade C: Fair" }
        default { Write-Host "Keep Trying!" }
    }

    # 3. For Loop
    Write-Host "`nFor Loop (1 to 5):"
    $forItems = for ($i = 1; $i -le 5; $i++) { $i }
    Write-Host ($forItems -join " ")

    # 4. While Loop
    Write-Host "`nWhile Loop (Countdown):"
    $count = 3
    $whileItems = while ($count -gt 0) {
        $count
        $count--
    }
    Write-Host (($whileItems -join " ") + " Blastoff!")
}

Main
```

### Explanation
Demonstrates PowerShell `if/elseif/else`, `switch` statement with scriptblock actions, `for` loops, and `while` loops.

### Run Control Flow
```bash
pwsh control_flow.ps1
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
