# Kotlin Reference Guide

> **Category**: Mainstream & Systems  
> **Paradigm**: Multi-paradigm (Functional, object-oriented)  
> **Initial Release**: 2011  
> **Created By**: JetBrains  

---

## 1. Program 1: Hello World (`hello_world.kt`)

```kt
// ==========================================
// Program: Hello World in Kotlin
// ==========================================
fun main() {
    println("Hello, World!")
}
```

### Explanation
Kotlin provides clean top-level functions without class wrapping.

### Run Hello World
```bash
kotlinc hello_world.kt -include-runtime -d hello_world.jar && java -jar hello_world.jar
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.kt`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```kt
// ==========================================
// Program: Basic Operations in Kotlin (+, -, *, /, %)
// ==========================================
fun main() {
    val a = 20
    val b = 6

    println("a = $a, b = $b")
    println("Addition (a + b)        : ${a + b}")
    println("Subtraction (a - b)     : ${a - b}")
    println("Multiplication (a * b)  : ${a * b}")
    println("Integer Division (a / b): ${a / b}")
    println("Float Division (toDouble): ${a.toDouble() / b}")
    println("Modulo (a % b)          : ${a % b}")
}
```

### Explanation
String template `${a + b}` evaluates expressions inline. `a.toDouble()` casts to double.

### Run Basic Operations
```bash
kotlinc basic_operations.kt -include-runtime -d basic_operations.jar && java -jar basic_operations.jar
```
**Expected Output**:
```text
a = 20, b = 6
Addition (a + b)        : 26
Subtraction (a - b)     : 14
Multiplication (a * b)  : 120
Integer Division (a / b): 3
Float Division (toDouble): 3.3333333333333335
Modulo (a % b)          : 2
```

---

## 3. Prerequisites & Installation

- **Guide**: JetBrains Kotlin

---

## 3. Program 3: Control Flow & Logic (`control_flow.kt`)
*Demonstrates conditional branching (`if/else`), pattern matching / multi-way `switch`, `for` iteration loops, and `while` loop.*

```kt
// ==========================================
// Program: Control Flow in Kotlin
// ==========================================

fun main() {
    // 1. Conditionals
    println("Conditionals:")
    val num = 15
    if (num > 0) {
        if (num % 2 == 0) {
            println("$num is Positive and Even")
        } else {
            println("$num is Positive and Odd")
        }
    } else if (num < 0) {
        println("$num is Negative")
    } else {
        println("Number is Zero")
    }

    println("\nPattern Matching / Switch:")
    // 2. When Expression
    val grade = "B"
    val result = when (grade) {
        "A" -> "Grade A: Excellent!"
        "B" -> "Grade B: Good Job!"
        "C" -> "Grade C: Fair"
        else -> "Keep Trying!"
    }
    println(result)

    // 3. For Loop with range 1..5
    println("\nFor Loop (1 to 5):")
    for (i in 1..5) {
        print(if (i == 5) "$i\n" else "$i ")
    }

    // 4. While Loop
    println("\nWhile Loop (Countdown):")
    var count = 3
    while (count > 0) {
        print("$count ")
        count--
    }
    println("Blastoff!")
}
```

### Explanation
Demonstrates Kotlin `if/else` expressions, powerful `when` branching, range-based `for (i in 1..5)`, and `while` loop.

### Run Control Flow
```bash
kotlinc control_flow.kt -include-runtime -d control_flow.jar && java -jar control_flow.jar
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
