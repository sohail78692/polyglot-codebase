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
