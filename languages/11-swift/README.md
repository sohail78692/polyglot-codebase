# Swift Reference Guide

> **Category**: Mainstream & Systems  
> **Paradigm**: Multi-paradigm (Protocol-oriented, object-oriented, functional)  
> **Initial Release**: 2014  
> **Created By**: Chris Lattner (Apple)  

---

## 1. Program 1: Hello World (`hello_world.swift`)

```swift
// ==========================================
// Program: Hello World in Swift
// ==========================================
print("Hello, World!")
```

### Explanation
Top-level statements execute directly.

### Run Hello World
```bash
swift hello_world.swift
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.swift`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```swift
// ==========================================
// Program: Basic Operations in Swift (+, -, *, /, %)
// ==========================================
let a = 20
let b = 6

print("a = \(a), b = \(b)")
print("Addition (a + b)        : \(a + b)")
print("Subtraction (a - b)     : \(a - b)")
print("Multiplication (a * b)  : \(a * b)")
print("Integer Division (a / b): \(a / b)")
print("Float Division (Double) : \(Double(a) / Double(b))")
print("Modulo (a % b)          : \(a % b)")
```

### Explanation
Swift uses string interpolation `\(...)` and strictly rejects implicit conversions between `Int` and `Double`.

### Run Basic Operations
```bash
swift basic_operations.swift
```
**Expected Output**:
```text
a = 20, b = 6
Addition (a + b)        : 26
Subtraction (a - b)     : 14
Multiplication (a * b)  : 120
Integer Division (a / b): 3
Float Division (Double) : 3.3333333333333335
Modulo (a % b)          : 2
```

---

## 3. Prerequisites & Installation

- **Guide**: Xcode / swift.org
