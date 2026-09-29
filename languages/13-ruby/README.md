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
