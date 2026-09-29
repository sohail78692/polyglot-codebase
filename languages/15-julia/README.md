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
