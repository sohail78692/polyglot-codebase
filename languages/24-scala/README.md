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
