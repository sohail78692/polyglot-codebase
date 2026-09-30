# Objective-C Reference Guide

> **Category**: Web3, Mobile & Modern  
> **Paradigm**: Object-oriented, reflective  
> **Initial Release**: 1984  
> **Created By**: Brad Cox and Tom Love  

---

## 1. Program 1: Hello World (`hello_world.m`)

```m
// ==========================================
// Program: Hello World in Objective-C
// ==========================================
#import <Foundation/Foundation.h>

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        NSLog(@"Hello, World!");
    }
    return 0;
}
```

### Explanation
`NSLog` formats and logs strings.

### Run Hello World
```bash
clang -framework Foundation hello_world.m -o hello_world && ./hello_world
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.m`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```m
// ==========================================
// Program: Basic Operations in Objective-C (+, -, *, /, %)
// ==========================================
#import <Foundation/Foundation.h>

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        int a = 20;
        int b = 6;

        NSLog(@"a = %d, b = %d", a, b);
        NSLog(@"Addition (a + b)        : %d", a + b);
        NSLog(@"Subtraction (a - b)     : %d", a - b);
        NSLog(@"Multiplication (a * b)  : %d", a * b);
        NSLog(@"Integer Division (a / b): %d", a / b);
        NSLog(@"Float Division (double) : %f", (double)a / b);
        NSLog(@"Modulo (a %% b)          : %d", a % b);
    }
    return 0;
}
```

### Explanation
Objective-C inherits C's standard arithmetic operators with `%` for remainder.

### Run Basic Operations
```bash
clang -framework Foundation basic_operations.m -o basic_operations && ./basic_operations
```
**Expected Output**:
```text
a = 20, b = 6
Addition (a + b)        : 26
Subtraction (a - b)     : 14
Multiplication (a * b)  : 120
Integer Division (a / b): 3
Float Division (double) : 3.333333
Modulo (a % b)          : 2
```

---

## 3. Prerequisites & Installation

- **Guide**: Clang / GNUstep / Xcode

---

## 3. Program 3: Control Flow & Logic (`control_flow.m`)
*Demonstrates conditional branching (`if/else`), pattern matching / multi-way `switch`, `for` iteration loops, and `while` loop.*

```m
// ==========================================
// Program: Control Flow in Objective-C
// ==========================================

#import <Foundation/Foundation.h>
#include <stdio.h>

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        // 1. Conditionals
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
        // 2. Switch Statement
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

        // 3. For Loop
        printf("\nFor Loop (1 to 5):\n");
        for (int i = 1; i <= 5; i++) {
            printf("%d%s", i, (i == 5 ? "\n" : " "));
        }

        // 4. While Loop
        printf("\nWhile Loop (Countdown):\n");
        int count = 3;
        while (count > 0) {
            printf("%d ", count);
            count--;
        }
        printf("Blastoff!\n");
    }
    return 0;
}
```

### Explanation
Demonstrates Objective-C Foundation framework conditionals, `switch` statement on primitive char, `for` loops, and `while` loops.

### Run Control Flow
```bash
clang -framework Foundation control_flow.m -o control_flow && ./control_flow
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
