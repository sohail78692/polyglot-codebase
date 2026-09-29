# Bash Reference Guide

> **Category**: Shell & Scripting  
> **Paradigm**: Command Language, Scripting  
> **Initial Release**: 1989  
> **Created By**: Brian Fox  

---

## 1. Program 1: Hello World (`hello_world.sh`)

```sh
#!/usr/bin/env bash
# ==========================================
# Program: Hello World in Bash
# ==========================================
echo "Hello, World!"
```

### Explanation
`echo` outputs to stdout.

### Run Hello World
```bash
bash hello_world.sh
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.sh`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```sh
#!/usr/bin/env bash
# ==========================================
# Program: Basic Operations in Bash (+, -, *, /, %)
# ==========================================
a=20
b=6

echo "a = $a, b = $b"
echo "Addition (a + b)        : $((a + b))"
echo "Subtraction (a - b)     : $((a - b))"
echo "Multiplication (a * b)  : $((a * b))"
echo "Integer Division (a / b): $((a / b))"
echo "Modulo (a % b)          : $((a % b))"
```

### Explanation
Bash evaluates arithmetic inside `$(( ... ))` using standard operators.

### Run Basic Operations
```bash
bash basic_operations.sh
```
**Expected Output**:
```text
a = 20, b = 6
Addition (a + b)        : 26
Subtraction (a - b)     : 14
Multiplication (a * b)  : 120
Integer Division (a / b): 3
Modulo (a % b)          : 2
```

---

## 3. Prerequisites & Installation

- **Guide**: Built-in / Git Bash
