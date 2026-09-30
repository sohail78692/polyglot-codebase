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

---

## 3. Program 3: Control Flow & Logic (`control_flow.sh`)
*Demonstrates conditional branching (`if/else`), pattern matching / multi-way `switch`, `for` iteration loops, and `while` loop.*

```sh
#!/usr/bin/env bash
# ==========================================
# Program: Control Flow in Bash
# ==========================================

main() {
    # 1. Conditionals
    echo "Conditionals:"
    num=15
    if (( num > 0 )); then
        if (( num % 2 == 0 )); then
            echo "${num} is Positive and Even"
        else
            echo "${num} is Positive and Odd"
        fi
    elif (( num < 0 )); then
        echo "${num} is Negative"
    else
        echo "Number is Zero"
    fi

    echo ""
    echo "Pattern Matching / Switch:"
    # 2. Case statement
    grade="B"
    case "$grade" in
        "A") echo "Grade A: Excellent!" ;;
        "B") echo "Grade B: Good Job!" ;;
        "C") echo "Grade C: Fair" ;;
        *)   echo "Keep Trying!" ;;
    esac

    echo ""
    echo "For Loop (1 to 5):"
    # 3. For loop
    for (( i = 1; i <= 5; i++ )); do
        if (( i == 5 )); then
            echo "$i"
        else
            printf "%d " "$i"
        fi
    done

    echo ""
    echo "While Loop (Countdown):"
    # 4. While loop
    count=3
    while (( count > 0 )); do
        printf "%d " "$count"
        (( count-- ))
    done
    echo "Blastoff!"
}

main
```

### Explanation
Demonstrates Bash `if [[ ... ]]; then / elif / else`, `case ... in` pattern matching, C-style and range `for` loops, and `while` loop.

### Run Control Flow
```bash
bash control_flow.sh
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
