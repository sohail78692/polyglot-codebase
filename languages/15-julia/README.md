# Julia Reference Guide

> **Category**: Scientific & Data  
> **Paradigm**: Multi-paradigm (Multiple dispatch, functional, procedural)  
> **Initial Release**: 2012  
> **Created By**: Jeff Bezanson et al.  

---

## 1. Program 1: Hello World (`hello_world.jl`)

```jl
# ==========================================
# Program: Hello World in Julia
# ==========================================
println("Hello, World!")
```

### Explanation
`println()` outputs text to stdout.

### Run Hello World
```bash
julia hello_world.jl
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.jl`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```jl
# ==========================================
# Program: Basic Operations in Julia (+, -, *, /, %, div)
# ==========================================
a = 20
b = 6

println("a = $a, b = $b")
println("Addition (a + b)        : $(a + b)")
println("Subtraction (a - b)     : $(a - b)")
println("Multiplication (a * b)  : $(a * b)")
println("Division (a / b)        : $(a / b)")
println("Integer Division (div)  : $(div(a, b))")
println("Modulo (a % b)          : $(a % b)")
```

### Explanation
Julia's `/` operator always performs floating-point division; `div(a, b)` performs integer division.

### Run Basic Operations
```bash
julia basic_operations.jl
```
**Expected Output**:
```text
a = 20, b = 6
Addition (a + b)        : 26
Subtraction (a - b)     : 14
Multiplication (a * b)  : 120
Division (a / b)        : 3.3333333333333335
Integer Division (div)  : 3
Modulo (a % b)          : 2
```

---

## 3. Prerequisites & Installation

- **Guide**: julialang.org

---

## 3. Program 3: Control Flow & Logic (`control_flow.jl`)
*Demonstrates conditional branching (`if/else`), pattern matching / multi-way `switch`, `for` iteration loops, and `while` loop.*

```jl
# ==========================================
# Program: Control Flow in Julia
# ==========================================

function main()
    # 1. Conditionals
    println("Conditionals:")
    num = 15
    if num > 0
        if num % 2 == 0
            println("$num is Positive and Even")
        else
            println("$num is Positive and Odd")
        end
    elseif num < 0
        println("$num is Negative")
    else
        println("Number is Zero")
    end

    println("\nPattern Matching / Switch:")
    # 2. Branch matching
    grade = "B"
    msg = if grade == "A"
        "Grade A: Excellent!"
    elseif grade == "B"
        "Grade B: Good Job!"
    elseif grade == "C"
        "Grade C: Fair"
    else
        "Keep Trying!"
    end
    println(msg)

    # 3. For Loop
    println("\nFor Loop (1 to 5):")
    for i in 1:5
        print(i, i == 5 ? "\n" : " ")
    end

    # 4. While Loop
    println("\nWhile Loop (Countdown):")
    count = 3
    while count > 0
        print(count, " ")
        count -= 1
    end
    println("Blastoff!")
end

main()
```

### Explanation
Demonstrates Julia `if/elseif/else` branching, multiple dispatch / conditional matching, range `for` loops, and `while` loop.

### Run Control Flow
```bash
julia control_flow.jl
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
