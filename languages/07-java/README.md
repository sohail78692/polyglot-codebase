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
