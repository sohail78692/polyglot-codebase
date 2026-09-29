# F# Reference Guide

> **Category**: Functional & Declarative  
> **Paradigm**: Functional-first, object-oriented, imperative  
> **Initial Release**: 2005  
> **Created By**: Don Syme (Microsoft Research)  

---

## 1. Program 1: Hello World (`hello_world.fs`)

```fs
// ==========================================
// Program: Hello World in F#
// ==========================================
printfn "Hello, World!"
```

### Explanation
`printfn` is a strongly typed output function.

### Run Hello World
```bash
dotnet fsi hello_world.fs
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.fs`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```fs
// ==========================================
// Program: Basic Operations in F# (+, -, *, /, %)
// ==========================================
let a = 20
let b = 6

printfn "a = %d, b = %d" a b
printfn "Addition (a + b)        : %d" (a + b)
printfn "Subtraction (a - b)     : %d" (a - b)
printfn "Multiplication (a * b)  : %d" (a * b)
printfn "Integer Division (a / b): %d" (a / b)
printfn "Float Division (float)  : %f" (float a / float b)
printfn "Modulo (a % b)          : %d" (a % b)
```

### Explanation
F# supports standard arithmetic with type safety: `float a / float b` casts to float for real division.

### Run Basic Operations
```bash
dotnet fsi basic_operations.fs
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

- **Guide**: .NET SDK
