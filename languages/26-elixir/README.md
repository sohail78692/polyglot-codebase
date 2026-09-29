# Elixir Reference Guide

> **Category**: Functional & Declarative  
> **Paradigm**: Functional, Concurrent (Actor model)  
> **Initial Release**: 2012  
> **Created By**: José Valim  

---

## 1. Program 1: Hello World (`hello_world.exs`)

```exs
# ==========================================
# Program: Hello World in Elixir
# ==========================================
IO.puts("Hello, World!")
```

### Explanation
`IO.puts` prints a string to stdout.

### Run Hello World
```bash
elixir hello_world.exs
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.exs`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```exs
# ==========================================
# Program: Basic Operations in Elixir (+, -, *, /, div, rem)
# ==========================================
a = 20
b = 6

IO.puts("a = #{a}, b = #{b}")
IO.puts("Addition (a + b)        : #{a + b}")
IO.puts("Subtraction (a - b)     : #{a - b}")
IO.puts("Multiplication (a * b)  : #{a * b}")
IO.puts("Float Division (a / b)  : #{a / b}")
IO.puts("Integer Division (div)  : #{div(a, b)}")
IO.puts("Remainder (rem)         : #{rem(a, b)}")
```

### Explanation
In Elixir, `/` always yields a float, `div(a, b)` does integer division, and `rem(a, b)` computes remainder.

### Run Basic Operations
```bash
elixir basic_operations.exs
```
**Expected Output**:
```text
a = 20, b = 6
Addition (a + b)        : 26
Subtraction (a - b)     : 14
Multiplication (a * b)  : 120
Float Division (a / b)  : 3.3333333333333335
Integer Division (div)  : 3
Remainder (rem)         : 2
```

---

## 3. Prerequisites & Installation

- **Guide**: elixir-lang.org
