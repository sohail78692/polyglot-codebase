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
