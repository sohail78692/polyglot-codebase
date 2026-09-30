# Go Reference Guide

> **Category**: Mainstream & Systems  
> **Paradigm**: Multi-paradigm (Concurrent, imperative, procedural)  
> **Initial Release**: 2009  
> **Created By**: Robert Griesemer, Rob Pike, Ken Thompson (Google)  

---

## 1. Program 1: Hello World (`hello_world.go`)

```go
// ==========================================
// Program: Hello World in Go (Golang)
// ==========================================
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

### Explanation
Go uses `fmt.Println` for console output.

### Run Hello World
```bash
go run hello_world.go
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.go`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```go
// ==========================================
// Program: Basic Operations in Go (+, -, *, /, %)
// ==========================================
package main

import "fmt"

func main() {
    a := 20
    b := 6

    fmt.Printf("a = %d, b = %d\n", a, b)
    fmt.Printf("Addition (a + b)        : %d\n", a + b)
    fmt.Printf("Subtraction (a - b)     : %d\n", a - b)
    fmt.Printf("Multiplication (a * b)  : %d\n", a * b)
    fmt.Printf("Integer Division (a / b): %d\n", a / b)
    fmt.Printf("Float Division (float64): %f\n", float64(a) / float64(b))
    fmt.Printf("Modulo (a % b)          : %d\n", a % b)
}
```

### Explanation
Go enforces strict typing: float conversion must be explicit via `float64(a) / float64(b)`.

### Run Basic Operations
```bash
go run basic_operations.go
```
**Expected Output**:
```text
a = 20, b = 6
Addition (a + b)        : 26
Subtraction (a - b)     : 14
Multiplication (a * b)  : 120
Integer Division (a / b): 3
Float Division (float64): 3.3333333333333335
Modulo (a % b)          : 2
```

---

## 3. Prerequisites & Installation

- **Guide**: go.dev

---

## 3. Program 3: Control Flow & Logic (`control_flow.go`)
*Demonstrates conditional branching (`if/else`), pattern matching / multi-way `switch`, `for` iteration loops, and `while` loop.*

```go
// ==========================================
// Program: Control Flow in Go
// ==========================================

package main

import "fmt"

func main() {
    // 1. Conditionals
    fmt.Println("Conditionals:")
    num := 15
    if num > 0 {
        if num%2 == 0 {
            fmt.Printf("%d is Positive and Even\n", num)
        } else {
            fmt.Printf("%d is Positive and Odd\n", num)
        }
    } else if num < 0 {
        fmt.Printf("%d is Negative\n", num)
    } else {
        fmt.Println("Number is Zero")
    }

    fmt.Println("\nPattern Matching / Switch:")
    // 2. Switch statement
    grade := "B"
    switch grade {
    case "A":
        fmt.Println("Grade A: Excellent!")
    case "B":
        fmt.Println("Grade B: Good Job!")
    case "C":
        fmt.Println("Grade C: Fair")
    default:
        fmt.Println("Keep Trying!")
    }

    // 3. For Loop
    fmt.Println("\nFor Loop (1 to 5):")
    for i := 1; i <= 5; i++ {
        if i == 5 {
            fmt.Println(i)
        } else {
            fmt.Printf("%d ", i)
        }
    }

    // 4. While-style Loop
    fmt.Println("\nWhile Loop (Countdown):")
    count := 3
    for count > 0 {
        fmt.Printf("%d ", count)
        count--
    }
    fmt.Println("Blastoff!")
}
```

### Explanation
Demonstrates Go's parentheses-free `if/else`, clean non-fallthrough `switch`, standard `for` loop, and `while`-equivalent single-condition `for`.

### Run Control Flow
```bash
go run control_flow.go
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
