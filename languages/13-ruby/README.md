# Ruby Reference Guide

> **Category**: Mainstream & Systems  
> **Paradigm**: Multi-paradigm (Pure object-oriented, imperative, functional)  
> **Initial Release**: 1995  
> **Created By**: Yukihiro Matsumoto (Matz)  

---

## 1. Program 1: Hello World (`hello_world.rb`)

```rb
# ==========================================
# Program: Hello World in Ruby
# ==========================================
puts "Hello, World!"
```

### Explanation
`puts` outputs an object followed by a newline.

### Run Hello World
```bash
ruby hello_world.rb
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.rb`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```rb
# ==========================================
# Program: Basic Operations in Ruby (+, -, *, /, %)
# ==========================================
a = 20
b = 6

puts "a = #{a}, b = #{b}"
puts "Addition (a + b)        : #{a + b}"
puts "Subtraction (a - b)     : #{a - b}"
puts "Multiplication (a * b)  : #{a * b}"
puts "Integer Division (a / b): #{a / b}"
puts "Float Division (to_f)   : #{a.to_f / b}"
puts "Modulo (a % b)          : #{a % b}"
```

### Explanation
Ruby divides integers using integer division. `a.to_f` converts to a float for fractional division.

### Run Basic Operations
```bash
ruby basic_operations.rb
```
**Expected Output**:
```text
a = 20, b = 6
Addition (a + b)        : 26
Subtraction (a - b)     : 14
Multiplication (a * b)  : 120
Integer Division (a / b): 3
Float Division (to_f)   : 3.3333333333333335
Modulo (a % b)          : 2
```

---

## 3. Prerequisites & Installation

- **Guide**: ruby-lang.org

---

## 3. Program 3: Control Flow & Logic (`control_flow.rb`)
*Demonstrates conditional branching (`if/else`), pattern matching / multi-way `switch`, `for` iteration loops, and `while` loop.*

```rb
# ==========================================
# Program: Control Flow in Ruby
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
  # 2. Case statement
  grade = "B"
  case grade
  when "A"
    puts "Grade A: Excellent!"
  when "B"
    puts "Grade B: Good Job!"
  when "C"
    puts "Grade C: Fair"
  else
    puts "Keep Trying!"
  end

  # 3. For loop / Range iteration
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
Demonstrates Ruby's expressive `if/elsif/else`, flexible `case/when` pattern matching, range-based `each`, and `while` loop.

### Run Control Flow
```bash
ruby control_flow.rb
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
