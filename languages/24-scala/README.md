# Scala Reference Guide

> **Category**: Functional & Declarative  
> **Paradigm**: Functional, Object-oriented  
> **Initial Release**: 2004  
> **Created By**: Martin Odersky  

---

## 1. Program 1: Hello World (`hello_world.scala`)

```scala
// ==========================================
// Program: Hello World in Scala (Scala 3)
// ==========================================
@main def run(): Unit =
  println("Hello, World!")
```

### Explanation
Scala 3 uses `@main` for top-level entry functions.

### Run Hello World
```bash
scala hello_world.scala
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.scala`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```scala
// ==========================================
// Program: Basic Operations in Scala (Scala 3)
// ==========================================
@main def runOps(): Unit =
  val a = 20
  val b = 6

  println(s"a = $a, b = $b")
  println(s"Addition (a + b)        : ${a + b}")
  println(s"Subtraction (a - b)     : ${a - b}")
  println(s"Multiplication (a * b)  : ${a * b}")
  println(s"Integer Division (a / b): ${a / b}")
  println(s"Float Division (toDouble): ${a.toDouble / b}")
  println(s"Modulo (a % b)          : ${a % b}")
```

### Explanation
String interpolator `s"..."` evaluates `${a + b}` directly.

### Run Basic Operations
```bash
scala basic_operations.scala
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

- **Guide**: scala-lang.org

---

## 3. Program 3: Control Flow & Logic (`control_flow.scala`)
*Demonstrates conditional branching (`if/else`), pattern matching / multi-way `switch`, `for` iteration loops, and `while` loop.*

```scala
// ==========================================
// Program: Control Flow in Scala
// ==========================================

object ControlFlow {
  def main(args: Array[String]): Unit = {
    // 1. Conditionals
    println("Conditionals:")
    val num = 15
    if (num > 0) {
      if (num % 2 == 0) println(s"$num is Positive and Even")
      else println(s"$num is Positive and Odd")
    } else if (num < 0) {
      println(s"$num is Negative")
    } else {
      println("Number is Zero")
    }

    println("\nPattern Matching / Switch:")
    // 2. Pattern Matching
    val grade = "B"
    val msg = grade match {
      case "A" => "Grade A: Excellent!"
      case "B" => "Grade B: Good Job!"
      case "C" => "Grade C: Fair"
      case _   => "Keep Trying!"
    }
    println(msg)

    // 3. For Loop (1 to 5 inclusive)
    println("\nFor Loop (1 to 5):")
    for (i <- 1 to 5) {
      print(if (i == 5) s"$i\n" else s"$i ")
    }

    // 4. While Loop
    println("\nWhile Loop (Countdown):")
    var count = 3
    while (count > 0) {
      print(s"$count ")
      count -= 1
    }
    println("Blastoff!")
  }
}
```

### Explanation
Demonstrates Scala expression-based `if/else`, powerful `match` pattern matching, `for (i <- 1 to 5)` loop, and `while` loop.

### Run Control Flow
```bash
scala control_flow.scala
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
