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

---

## 3. Program 3: Control Flow & Logic (`control_flow.c`)
*Demonstrates conditional branching (`if/else`), pattern matching / multi-way `switch`, `for` iteration loops, and `while` loop.*

```c
/* ==========================================
   Program: Control Flow in C
   ========================================== */

#include <stdio.h>

int main(void) {
    /* 1. Conditionals (if / else if / else) */
    printf("Conditionals:\n");
    int num = 15;
    if (num > 0) {
        if (num % 2 == 0) {
            printf("%d is Positive and Even\n", num);
        } else {
            printf("%d is Positive and Odd\n", num);
        }
    } else if (num < 0) {
        printf("%d is Negative\n", num);
    } else {
        printf("Number is Zero\n");
    }

    printf("\nPattern Matching / Switch:\n");
    /* 2. Switch statement */
    char grade = 'B';
    switch (grade) {
        case 'A':
            printf("Grade A: Excellent!\n");
            break;
        case 'B':
            printf("Grade B: Good Job!\n");
            break;
        case 'C':
            printf("Grade C: Fair\n");
            break;
        default:
            printf("Keep Trying!\n");
            break;
    }

    /* 3. For Loop */
    printf("\nFor Loop (1 to 5):\n");
    for (int i = 1; i <= 5; i++) {
        printf("%d%s", i, (i == 5) ? "\n" : " ");
    }

    /* 4. While Loop */
    printf("\nWhile Loop (Countdown):\n");
    int count = 3;
    while (count > 0) {
        printf("%d ", count);
        count--;
    }
    printf("Blastoff!\n");

    return 0;
}
```

### Explanation
Demonstrates ANSI C `if/else` control flow, `switch/case` jump tables, indexed `for` loops, and `while` loop countdowns.

### Run Control Flow
```bash
gcc control_flow.c -o control_flow && ./control_flow
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
