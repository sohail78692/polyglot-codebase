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
