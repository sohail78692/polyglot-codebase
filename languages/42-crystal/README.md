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
