# Nim Reference Guide

> **Category**: Scientific & Data  
> **Paradigm**: Multi-paradigm (Metaprogramming, functional, procedural)  
> **Initial Release**: 2008  
> **Created By**: Andreas Rumpf  

---

## 1. Program 1: Hello World (`hello_world.nim`)

```nim
# ==========================================
# Program: Hello World in Nim
# ==========================================
echo "Hello, World!"
```

### Explanation
`echo` outputs to stdout with a newline.

### Run Hello World
```bash
nim compile --run hello_world.nim
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.nim`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```nim
# ==========================================
# Program: Basic Operations in Nim (+, -, *, /, div, mod)
# ==========================================
let a = 20
let b = 6

echo "a = ", a, ", b = ", b
echo "Addition (a + b)        : ", a + b
echo "Subtraction (a - b)     : ", a - b
echo "Multiplication (a * b)  : ", a * b
echo "Float Division (a / b)  : ", a / b     # '/' returns a float
echo "Integer Division (div)  : ", a div b   # 'div' is integer division
echo "Modulo (mod)            : ", a mod b   # 'mod' is modulo
```

### Explanation
Nim uses `div` for integer division and `mod` for remainder.

### Run Basic Operations
```bash
nim compile --run basic_operations.nim
```
**Expected Output**:
```text
a = 20, b = 6
Addition (a + b)        : 26
Subtraction (a - b)     : 14
Multiplication (a * b)  : 120
Float Division (a / b)  : 3.333333333333334
Integer Division (div)  : 3
Modulo (mod)            : 2
```

---

## 3. Prerequisites & Installation

- **Guide**: nim-lang.org

---

## 3. Program 3: Control Flow & Logic (`control_flow.nim`)
*Demonstrates conditional branching (`if/else`), pattern matching / multi-way `switch`, `for` iteration loops, and `while` loop.*

```nim
# ==========================================
# Program: Control Flow in Nim
# ==========================================

proc main() =
    # 1. Conditionals
    echo "Conditionals:"
    let num = 15
    if num > 0:
        if num mod 2 == 0:
            echo $num & " is Positive and Even"
        else:
            echo $num & " is Positive and Odd"
    elif num < 0:
        echo $num & " is Negative"
    else:
        echo "Number is Zero"

    echo "\nPattern Matching / Switch:"
    # 2. Case Statement
    let grade = "B"
    case grade
    of "A":
        echo "Grade A: Excellent!"
    of "B":
        echo "Grade B: Good Job!"
    of "C":
        echo "Grade C: Fair"
    else:
        echo "Keep Trying!"

    # 3. For Loop with range 1..5
    echo "\nFor Loop (1 to 5):"
    for i in 1..5:
        stdout.write($i & (if i == 5: "\n" else: " "))

    # 4. While Loop
    echo "\nWhile Loop (Countdown):"
    var count = 3
    while count > 0:
        stdout.write($count & " ")
        count -= 1
    echo "Blastoff!"

main()
```

### Explanation
Demonstrates Nim indentation-based syntax, `case/of` statement with exhaustive checking, `countup` / `..` iterator, and `while` loop.

### Run Control Flow
```bash
nim r control_flow.nim
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
