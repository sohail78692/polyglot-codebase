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
