# Crystal Reference Guide

> **Category**: Web3, Mobile & Modern  
> **Paradigm**: Object-oriented, compiled, statically type-checked  
> **Initial Release**: 2014  
> **Created By**: Ary Borenszweig et al.  

---

## 1. Program 1: Hello World (`hello_world.cr`)

```cr
# ==========================================
# Program: Hello World in Crystal
# ==========================================
puts "Hello, World!"
```

### Explanation
`puts` sends text to stdout.

### Run Hello World
```bash
crystal run hello_world.cr
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.cr`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```cr
# ==========================================
# Program: Basic Operations in Crystal (+, -, *, /, //, %)
# ==========================================
a = 20
b = 6

puts "a = #{a}, b = #{b}"
puts "Addition (a + b)        : #{a + b}"
puts "Subtraction (a - b)     : #{a - b}"
puts "Multiplication (a * b)  : #{a * b}"
puts "Float Division (a / b)  : #{a / b}"
puts "Integer Division (//)   : #{a // b}" # // is integer division in Crystal
puts "Modulo (a % b)          : #{a % b}"
```

### Explanation
Crystal uses `//` for explicit integer division and `/` for float division.

### Run Basic Operations
```bash
crystal run basic_operations.cr
```
**Expected Output**:
```text
a = 20, b = 6
Addition (a + b)        : 26
Subtraction (a - b)     : 14
Multiplication (a * b)  : 120
Float Division (a / b)  : 3.3333333333333335
Integer Division (//)   : 3
Modulo (a % b)          : 2
```

---

## 3. Prerequisites & Installation

- **Guide**: crystal-lang.org

---

## 3. Program 3: Control Flow & Logic (`control_flow.cr`)
*Demonstrates conditional branching (`if/else`), pattern matching / multi-way `switch`, `for` iteration loops, and `while` loop.*

```cr
# ==========================================
# Program: Control Flow in Crystal
# ==========================================

def main
  # 1. Conditionals
  puts "Conditionals:"
  num = 15
  if num > 0
    if num % 2 == 0
      puts "#{num} is Positive and Even"
    else
      puts "#{num} is Positive and Odd"
    end
  elsif num < 0
    puts "#{num} is Negative"
  else
    puts "Number is Zero"
  end

  puts "\nPattern Matching / Switch:"
  # 2. Case Expression
  grade = "B"
  msg = case grade
  when "A" then "Grade A: Excellent!"
  when "B" then "Grade B: Good Job!"
  when "C" then "Grade C: Fair"
  else "Keep Trying!"
  end
  puts msg

  # 3. For Loop over range
  puts "\nFor Loop (1 to 5):"
  puts (1..5).to_a.join(" ")

  # 4. While Loop
  puts "\nWhile Loop (Countdown):"
  count = 3
  while count > 0
    print "#{count} "
    count -= 1
  end
  puts "Blastoff!"
end

main
```

### Explanation
Demonstrates Crystal statically-typed Ruby-like syntax with `if/elsif/else`, `case/when` expressions, range loops, and `while` loop.

### Run Control Flow
```bash
crystal run control_flow.cr
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
