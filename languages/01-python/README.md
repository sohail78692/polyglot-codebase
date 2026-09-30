# Python Reference Guide

> **Category**: Mainstream & Systems  
> **Paradigm**: Multi-paradigm (Object-oriented, imperative, functional, procedural)  
> **Initial Release**: 1991  
> **Created By**: Guido van Rossum  

---

## 1. Program 1: Hello World (`hello_world.py`)

```py
# ==========================================
# Program: Hello World in Python
# ==========================================

# Step 1: Define our main entry function.
def main():
    # 'print()' sends text to the terminal and appends a newline.
    print("Hello, World!")

# Step 2: Run main() if executed directly.
if __name__ == "__main__":
    main()
```

### Explanation
Python uses `print()` to output text. `if __name__ == '__main__':` ensures the script executes only when directly run.

### Run Hello World
```bash
python hello_world.py
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.py`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```py
# ==========================================
# Program: Basic Operations in Python (+, -, *, /, //, %)
# ==========================================

def main():
    a = 20
    b = 6

    print(f"a = {a}, b = {b}")
    print(f"Addition (a + b)        : {a + b}")
    print(f"Subtraction (a - b)     : {a - b}")
    print(f"Multiplication (a * b)  : {a * b}")
    print(f"Division (a / b)        : {a / b}")       # Float division
    print(f"Integer Division (a // b): {a // b}")     # Truncating integer division
    print(f"Modulo (a % b)          : {a % b}")       # Remainder of division

if __name__ == "__main__":
    main()
```

### Explanation
Python supports standard arithmetic: `+`, `-`, `*`, `/` (float division), `//` (integer floor division), and `%` (modulo).

### Run Basic Operations
```bash
python basic_operations.py
```
**Expected Output**:
```text
a = 20, b = 6
Addition (a + b)        : 26
Subtraction (a - b)     : 14
Multiplication (a * b)  : 120
Division (a / b)        : 3.3333333333333335
Integer Division (a // b): 3
Modulo (a % b)          : 2
```

---

## 3. Prerequisites & Installation

- **Guide**: python.org or `winget install Python.Python.3.12` / `brew install python` / `apt install python3`

---

## 3. Program 3: Control Flow & Logic (`control_flow.py`)
*Demonstrates conditional branching (`if/else`), pattern matching / multi-way `switch`, `for` iteration loops, and `while` loop.*

```py
# ==========================================
# Program: Control Flow in Python
# ==========================================

def main():
    # 1. Conditionals (if / elif / else)
    print("Conditionals:")
    num = 15
    if num > 0:
        if num % 2 == 0:
            print(f"{num} is Positive and Even")
        else:
            print(f"{num} is Positive and Odd")
    elif num < 0:
        print(f"{num} is Negative")
    else:
        print("Number is Zero")

    print("\nPattern Matching:")
    # 2. Structural Pattern Matching (Python 3.10+)
    grade = "B"
    match grade:
        case "A":
            print("Grade A: Excellent!")
        case "B":
            print("Grade B: Good Job!")
        case "C":
            print("Grade C: Fair")
        case _:
            print("Keep Trying!")

    # 3. For Loop with range
    print("\nFor Loop (1 to 5):")
    for i in range(1, 6):
        print(i, end=" " if i < 5 else "\n")

    # 4. While Loop Countdown
    print("\nWhile Loop (Countdown):")
    count = 3
    while count > 0:
        print(count, end=" ")
        count -= 1
    print("Blastoff!")

if __name__ == "__main__":
    main()
```

### Explanation
Demonstrates `if/elif/else` branching, Python 3.10+ structural pattern matching (`match/case`), `for` loop with `range()`, and `while` loop.

### Run Control Flow
```bash
python control_flow.py
```
**Expected Output**:
```text
Conditionals:
15 is Positive and Odd

Pattern Matching:
Grade B: Good Job!

For Loop (1 to 5):
1 2 3 4 5

While Loop (Countdown):
3 2 1 Blastoff!
```
