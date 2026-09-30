# AWK Reference Guide

> **Category**: Shell & Scripting  
> **Paradigm**: Data-driven, pattern scanning and processing  
> **Initial Release**: 1977  
> **Created By**: Alfred Aho et al.  

---

## 1. Program 1: Hello World (`hello_world.awk`)

```awk
# ==========================================
# Program: Hello World in AWK
# ==========================================
BEGIN {
    print "Hello, World!"
}
```

### Explanation
`BEGIN` block executes prior to input processing.

### Run Hello World
```bash
awk -f hello_world.awk /dev/null
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.awk`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```awk
# ==========================================
# Program: Basic Operations in AWK (+, -, *, /, %)
# ==========================================
BEGIN {
    a = 20
    b = 6

    printf "a = %d, b = %d\n", a, b
    printf "Addition (a + b)        : %d\n", a + b
    printf "Subtraction (a - b)     : %d\n", a - b
    printf "Multiplication (a * b)  : %d\n", a * b
    printf "Division (a / b)        : %f\n", a / b
    printf "Integer Division (int)  : %d\n", int(a / b)
    printf "Modulo (a %%%% b)          : %d\n", a % b
}
```

### Explanation
AWK performs floating division by default; `int(a / b)` yields the integer quotient.

### Run Basic Operations
```bash
awk -f basic_operations.awk /dev/null
```
**Expected Output**:
```text
a = 20, b = 6
Addition (a + b)        : 26
Subtraction (a - b)     : 14
Multiplication (a * b)  : 120
Division (a / b)        : 3.33333
Integer Division (int)  : 3
Modulo (a % b)          : 2
```

---

## 3. Prerequisites & Installation

- **Guide**: gawk

---

## 3. Program 3: Control Flow & Logic (`control_flow.awk`)
*Demonstrates conditional branching (`if/else`), pattern matching / multi-way `switch`, `for` iteration loops, and `while` loop.*

```awk
# ==========================================
# Program: Control Flow in AWK
# ==========================================

BEGIN {
    # 1. Conditionals
    print "Conditionals:"
    num = 15
    if (num > 0) {
        if (num % 2 == 0) {
            print num " is Positive and Even"
        } else {
            print num " is Positive and Odd"
        }
    } else if (num < 0) {
        print num " is Negative"
    } else {
        print "Number is Zero"
    }

    print "\nPattern Matching / Switch:"
    # 2. Multi-way Branching
    grade = "B"
    if (grade == "A") {
        print "Grade A: Excellent!"
    } else if (grade == "B") {
        print "Grade B: Good Job!"
    } else if (grade == "C") {
        print "Grade C: Fair"
    } else {
        print "Keep Trying!"
    }

    # 3. For Loop
    print "\nFor Loop (1 to 5):"
    out_for = ""
    for (i = 1; i <= 5; i++) {
        out_for = (i == 1) ? i : out_for " " i
    }
    print out_for

    # 4. While Loop
    print "\nWhile Loop (Countdown):"
    count = 3
    out_while = ""
    while (count > 0) {
        out_while = (out_while == "") ? count : out_while " " count
        count--
    }
    print out_while " Blastoff!"
}
```

### Explanation
Demonstrates AWK pattern-action conditionals `if/else`, `switch/case` (gawk) or conditional ladders, `for` loops, and `while` loops.

### Run Control Flow
```bash
awk -f control_flow.awk /dev/null
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
