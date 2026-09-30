# Java Reference Guide

> **Category**: Mainstream & Systems  
> **Paradigm**: Multi-paradigm (Object-oriented, generic, concurrent)  
> **Initial Release**: 1995  
> **Created By**: James Gosling (Sun Microsystems)  

---

## 1. Program 1: Hello World (`HelloWorld.java`)

```java
// ==========================================
// Program: Hello World in Java
// ==========================================
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

### Explanation
Public class name must match filename `HelloWorld.java`.

### Run Hello World
```bash
javac HelloWorld.java && java HelloWorld
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`BasicOperations.java`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```java
// ==========================================
// Program: Basic Operations in Java (+, -, *, /, %)
// ==========================================
public class BasicOperations {
    public static void main(String[] args) {
        int a = 20;
        int b = 6;

        System.out.println("a = " + a + ", b = " + b);
        System.out.println("Addition (a + b)        : " + (a + b));
        System.out.println("Subtraction (a - b)     : " + (a - b));
        System.out.println("Multiplication (a * b)  : " + (a * b));
        System.out.println("Integer Division (a / b): " + (a / b));
        System.out.println("Float Division (double) : " + ((double) a / b));
        System.out.println("Modulo (a % b)          : " + (a % b));
    }
}
```

### Explanation
Java evaluates arithmetic expressions with precedence: `(a + b)` prevents string concatenation precedence errors.

### Run Basic Operations
```bash
javac BasicOperations.java && java BasicOperations
```
**Expected Output**:
```text
a = 20, b = 6
Addition (a + b)        : 26
Subtraction (a - b)     : 14
Multiplication (a * b)  : 120
Integer Division (a / b): 3
Float Division (double) : 3.3333333333333335
Modulo (a % b)          : 2
```

---

## 3. Prerequisites & Installation

- **Guide**: OpenJDK / Oracle JDK

---

## 3. Program 3: Control Flow & Logic (`ControlFlow.java`)
*Demonstrates conditional branching (`if/else`), pattern matching / multi-way `switch`, `for` iteration loops, and `while` loop.*

```java
// ==========================================
// Program: Control Flow in Java
// ==========================================

public class ControlFlow {
    public static void main(String[] args) {
        // 1. Conditionals
        System.out.println("Conditionals:");
        int num = 15;
        if (num > 0) {
            if (num % 2 == 0) {
                System.out.println(num + " is Positive and Even");
            } else {
                System.out.println(num + " is Positive and Odd");
            }
        } else if (num < 0) {
            System.out.println(num + " is Negative");
        } else {
            System.out.println("Number is Zero");
        }

        System.out.println("\nPattern Matching / Switch:");
        // 2. Enhanced Switch Rule
        String grade = "B";
        String message = switch (grade) {
            case "A" -> "Grade A: Excellent!";
            case "B" -> "Grade B: Good Job!";
            case "C" -> "Grade C: Fair";
            default  -> "Keep Trying!";
        };
        System.out.println(message);

        // 3. For Loop
        System.out.println("\nFor Loop (1 to 5):");
        for (int i = 1; i <= 5; i++) {
            System.out.print(i + (i == 5 ? "\n" : " "));
        }

        // 4. While Loop
        System.out.println("\nWhile Loop (Countdown):");
        int count = 3;
        while (count > 0) {
            System.out.print(count + " ");
            count--;
        }
        System.out.println("Blastoff!");
    }
}
```

### Explanation
Demonstrates Java `if/else` blocks, modern arrow-syntax `switch` expressions (Java 14+), `for` loop, and `while` loop.

### Run Control Flow
```bash
javac ControlFlow.java && java ControlFlow
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
