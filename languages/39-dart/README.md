# Dart Reference Guide

> **Category**: Web3, Mobile & Modern  
> **Paradigm**: Multi-paradigm (Object-oriented, class-based)  
> **Initial Release**: 2011  
> **Created By**: Lars Bak and Kasper Lund (Google)  

---

## 1. Program 1: Hello World (`hello_world.dart`)

```dart
// ==========================================
// Program: Hello World in Dart
// ==========================================
void main() {
  print('Hello, World!');
}
```

### Explanation
`void main()` is the entry point.

### Run Hello World
```bash
dart run hello_world.dart
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.dart`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```dart
// ==========================================
// Program: Basic Operations in Dart (+, -, *, /, ~/, %)
// ==========================================
void main() {
  int a = 20;
  int b = 6;

  print('a = $a, b = $b');
  print('Addition (a + b)        : ${a + b}');
  print('Subtraction (a - b)     : ${a - b}');
  print('Multiplication (a * b)  : ${a * b}');
  print('Division (a / b)        : ${a / b}');
  print('Integer Division (~/)   : ${a ~/ b}'); // ~/ is truncating integer division in Dart
  print('Modulo (a % b)          : ${a % b}');
}
```

### Explanation
Dart features the special `~/` operator for truncating integer division.

### Run Basic Operations
```bash
dart run basic_operations.dart
```
**Expected Output**:
```text
a = 20, b = 6
Addition (a + b)        : 26
Subtraction (a - b)     : 14
Multiplication (a * b)  : 120
Division (a / b)        : 3.3333333333333335
Integer Division (~/)   : 3
Modulo (a % b)          : 2
```

---

## 3. Prerequisites & Installation

- **Guide**: dart.dev
