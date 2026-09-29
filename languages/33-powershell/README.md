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
