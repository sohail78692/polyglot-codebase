# C Reference Guide

> **Category**: Mainstream & Systems  
> **Paradigm**: Imperative, Procedural  
> **Initial Release**: 1972  
> **Created By**: Dennis Ritchie (Bell Labs)  

---

## 1. Program 1: Hello World (`hello_world.c`)

```c
/*
 * ==========================================
 * Program: Hello World in C
 * ==========================================
 */
#include <stdio.h>

int main(void) {
    printf("Hello, World!\n");
    return 0;
}
```

### Explanation
`printf` outputs formatted text to stdout.

### Run Hello World
```bash
gcc hello_world.c -o hello_world && ./hello_world
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.c`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```c
/*
 * ==========================================
 * Program: Basic Operations in C (+, -, *, /, %)
 * ==========================================
 */
#include <stdio.h>

int main(void) {
    int a = 20;
    int b = 6;

    printf("a = %d, b = %d\n", a, b);
    printf("Addition (a + b)        : %d\n", a + b);
    printf("Subtraction (a - b)     : %d\n", a - b);
    printf("Multiplication (a * b)  : %d\n", a * b);
    printf("Integer Division (a / b): %d\n", a / b);             // Integer division truncates
    printf("Float Division (float)  : %f\n", (float)a / (float)b); // Type casting for float
    printf("Modulo (a % b)          : %d\n", a % b);             // Remainder operator

    return 0;
}
```

### Explanation
In C, dividing two integers (`a / b`) produces an integer quotient. Type-casting to `(float)` yields decimal results. `%` yields the remainder.

### Run Basic Operations
```bash
gcc basic_operations.c -o basic_operations && ./basic_operations
```
**Expected Output**:
```text
a = 20, b = 6
Addition (a + b)        : 26
Subtraction (a - b)     : 14
Multiplication (a * b)  : 120
Integer Division (a / b): 3
Float Division (float)  : 3.333333
Modulo (a % b)          : 2
```

---

## 3. Prerequisites & Installation

- **Guide**: GCC / Clang / MSVC
