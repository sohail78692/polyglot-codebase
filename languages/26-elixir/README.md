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

---

## 3. Program 3: Control Flow & Logic (`control_flow.exs`)
*Demonstrates conditional branching (`if/else`), pattern matching / multi-way `switch`, `for` iteration loops, and `while` loop.*

```exs
# ==========================================
# Program: Control Flow in Elixir
# ==========================================

defmodule ControlFlow do
  def countdown(0), do: IO.puts("Blastoff!")
  def countdown(n) do
    IO.write("#{n} ")
    countdown(n - 1)
  end

  def main do
    # 1. Conditionals (cond)
    IO.puts("Conditionals:")
    num = 15
    cond do
      num > 0 ->
        if rem(num, 2) == 0 do
          IO.puts("#{num} is Positive and Even")
        else
          IO.puts("#{num} is Positive and Odd")
        end
      num < 0 -> IO.puts("#{num} is Negative")
      true    -> IO.puts("Number is Zero")
    end

    IO.puts("\nPattern Matching / Switch:")
    # 2. Case Pattern Matching
    grade = "B"
    msg = case grade do
      "A" -> "Grade A: Excellent!"
      "B" -> "Grade B: Good Job!"
      "C" -> "Grade C: Fair"
      _   -> "Keep Trying!"
    end
    IO.puts(msg)

    # 3. For Comprehension
    IO.puts("\nFor Loop (1 to 5):")
    Enum.each(1..5, fn i ->
      IO.write("#{i}#{if i == 5, do: "\n", else: " "}")
    end)

    # 4. While Loop via recursion
    IO.puts("\nWhile Loop (Countdown):")
    countdown(3)
  end
end

ControlFlow.main()
```

### Explanation
Demonstrates Elixir's `if/else`, `cond`, `case` pattern matching, `for` comprehensions, and recursion for loops.

### Run Control Flow
```bash
elixir control_flow.exs
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
