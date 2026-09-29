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
