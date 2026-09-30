# F# Reference Guide

> **Category**: Functional & Declarative  
> **Paradigm**: Functional-first, object-oriented, imperative  
> **Initial Release**: 2005  
> **Created By**: Don Syme (Microsoft Research)  

---

## 1. Program 1: Hello World (`hello_world.fs`)

```fs
// ==========================================
// Program: Hello World in F#
// ==========================================
printfn "Hello, World!"
```

### Explanation
`printfn` is a strongly typed output function.

### Run Hello World
```bash
dotnet fsi hello_world.fs
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.fs`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```fs
// ==========================================
// Program: Basic Operations in F# (+, -, *, /, %)
// ==========================================
let a = 20
let b = 6

printfn "a = %d, b = %d" a b
printfn "Addition (a + b)        : %d" (a + b)
printfn "Subtraction (a - b)     : %d" (a - b)
printfn "Multiplication (a * b)  : %d" (a * b)
printfn "Integer Division (a / b): %d" (a / b)
printfn "Float Division (float)  : %f" (float a / float b)
printfn "Modulo (a % b)          : %d" (a % b)
```

### Explanation
F# supports standard arithmetic with type safety: `float a / float b` casts to float for real division.

### Run Basic Operations
```bash
dotnet fsi basic_operations.fs
```
**Expected Output**:
```text
a = 20, b = 6
Addition (a + b)        : 26
Subtraction (a - b)     : 14
Multiplication (a * b)  : 120
Integer Division (a / b): 3
Float Division (float)  : 3.333333
Modulo (a % b)          : 2
```

---

## 3. Prerequisites & Installation

- **Guide**: .NET SDK

---

## 3. Program 3: Control Flow & Logic (`control_flow.fs`)
*Demonstrates conditional branching (`if/else`), pattern matching / multi-way `switch`, `for` iteration loops, and `while` loop.*

```fs
// ==========================================
// Program: Control Flow in F#
// ==========================================

let main () =
    // 1. Conditionals
    printfn "Conditionals:"
    let num = 15
    if num > 0 then
        if num % 2 = 0 then
            printfn "%d is Positive and Even" num
        else
            printfn "%d is Positive and Odd" num
    elif num < 0 then
        printfn "%d is Negative" num
    else
        printfn "Number is Zero"

    printfn "\nPattern Matching / Switch:"
    // 2. Match expression
    let grade = "B"
    let msg = 
        match grade with
        | "A" -> "Grade A: Excellent!"
        | "B" -> "Grade B: Good Job!"
        | "C" -> "Grade C: Fair"
        | _   -> "Keep Trying!"
    printfn "%s" msg

    // 3. For loop
    printfn "\nFor Loop (1 to 5):"
    for i in 1..5 do
        printf "%d%s" i (if i = 5 then "\n" else " ")

    // 4. While loop
    printfn "\nWhile Loop (Countdown):"
    let mutable count = 3
    while count > 0 do
        printf "%d " count
        count <- count - 1
    printfn "Blastoff!"

main ()
```

### Explanation
Demonstrates F# lightweight syntax `if/then/elif/else`, `match ... with` pattern matching, `for i in 1..5 do`, and `while` loop.

### Run Control Flow
```bash
dotnet fsi control_flow.fs
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
