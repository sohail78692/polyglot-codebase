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

---

## 3. Program 3: Control Flow & Logic (`control_flow.dart`)
*Demonstrates conditional branching (`if/else`), pattern matching / multi-way `switch`, `for` iteration loops, and `while` loop.*

```dart
// ==========================================
// Program: Control Flow in Dart
// ==========================================

void main() {
  // 1. Conditionals
  print("Conditionals:");
  int num = 15;
  if (num > 0) {
    if (num % 2 == 0) {
      print("$num is Positive and Even");
    } else {
      print("$num is Positive and Odd");
    }
  } else if (num < 0) {
    print("$num is Negative");
  } else {
    print("Number is Zero");
  }

  print("\nPattern Matching / Switch:");
  // 2. Dart 3.0 Switch Expression
  String grade = "B";
  String message = switch (grade) {
    "A" => "Grade A: Excellent!",
    "B" => "Grade B: Good Job!",
    "C" => "Grade C: Fair",
    _   => "Keep Trying!"
  };
  print(message);

  // 3. For Loop
  print("\nFor Loop (1 to 5):");
  List<int> forItems = [];
  for (int i = 1; i <= 5; i++) {
    forItems.add(i);
  }
  print(forItems.join(" "));

  // 4. While Loop
  print("\nWhile Loop (Countdown):");
  int count = 3;
  List<String> whileItems = [];
  while (count > 0) {
    whileItems.add(count.toString());
    count--;
  }
  whileItems.add("Blastoff!");
  print(whileItems.join(" "));
}
```

### Explanation
Demonstrates Dart 3.0+ pattern matching switch expressions, `if/else`, indexed `for` loops, and `while` loop.

### Run Control Flow
```bash
dart run control_flow.dart
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
