# C++ Reference Guide

> **Category**: Mainstream & Systems  
> **Paradigm**: Multi-paradigm (OOP, generic, procedural, functional)  
> **Initial Release**: 1985  
> **Created By**: Bjarne Stroustrup  

---

## 1. Program 1: Hello World (`hello_world.cpp`)

```cpp
/*
 * ==========================================
 * Program: Hello World in C++
 * ==========================================
 */
#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
```

### Explanation
`std::cout` and `<<` send data to standard output stream.

### Run Hello World
```bash
g++ -std=c++17 hello_world.cpp -o hello_world && ./hello_world
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.cpp`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```cpp
/*
 * ==========================================
 * Program: Basic Operations in C++ (+, -, *, /, %)
 * ==========================================
 */
#include <iostream>

int main() {
    int a = 20;
    int b = 6;

    std::cout << "a = " << a << ", b = " << b << std::endl;
    std::cout << "Addition (a + b)        : " << (a + b) << std::endl;
    std::cout << "Subtraction (a - b)     : " << (a - b) << std::endl;
    std::cout << "Multiplication (a * b)  : " << (a * b) << std::endl;
    std::cout << "Integer Division (a / b): " << (a / b) << std::endl;
    std::cout << "Float Division (double) : " << (static_cast<double>(a) / b) << std::endl;
    std::cout << "Modulo (a % b)          : " << (a % b) << std::endl;

    return 0;
}
```

### Explanation
`static_cast<double>(a) / b` converts `a` to double to perform floating-point division; `%` gives the remainder.

### Run Basic Operations
```bash
g++ -std=c++17 basic_operations.cpp -o basic_operations && ./basic_operations
```
**Expected Output**:
```text
a = 20, b = 6
Addition (a + b)        : 26
Subtraction (a - b)     : 14
Multiplication (a * b)  : 120
Integer Division (a / b): 3
Float Division (double) : 3.33333
Modulo (a % b)          : 2
```

---

## 3. Prerequisites & Installation

- **Guide**: G++ / Clang++

---

## 3. Program 3: Control Flow & Logic (`control_flow.cpp`)
*Demonstrates conditional branching (`if/else`), pattern matching / multi-way `switch`, `for` iteration loops, and `while` loop.*

```cpp
// ==========================================
// Program: Control Flow in C++
// ==========================================

#include <iostream>

int main() {
    // 1. Conditionals
    std::cout << "Conditionals:\n";
    int num = 15;
    if (num > 0) {
        if (num % 2 == 0) {
            std::cout << num << " is Positive and Even\n";
        } else {
            std::cout << num << " is Positive and Odd\n";
        }
    } else if (num < 0) {
        std::cout << num << " is Negative\n";
    } else {
        std::cout << "Number is Zero\n";
    }

    std::cout << "\nPattern Matching / Switch:\n";
    // 2. Switch statement
    char grade = 'B';
    switch (grade) {
        case 'A':
            std::cout << "Grade A: Excellent!\n";
            break;
        case 'B':
            std::cout << "Grade B: Good Job!\n";
            break;
        case 'C':
            std::cout << "Grade C: Fair\n";
            break;
        default:
            std::cout << "Keep Trying!\n";
            break;
    }

    // 3. For Loop
    std::cout << "\nFor Loop (1 to 5):\n";
    for (int i = 1; i <= 5; ++i) {
        std::cout << i << (i == 5 ? "\n" : " ");
    }

    // 4. While Loop
    std::cout << "\nWhile Loop (Countdown):\n";
    int count = 3;
    while (count > 0) {
        std::cout << count << " ";
        --count;
    }
    std::cout << "Blastoff!\n";

    return 0;
}
```

### Explanation
Demonstrates C++ `if/else` logic, `switch` branching, range-based and index-based `for` loops, and `while` loop.

### Run Control Flow
```bash
g++ -std=c++17 control_flow.cpp -o control_flow && ./control_flow
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
