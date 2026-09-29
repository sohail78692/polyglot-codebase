# Tcl Reference Guide

> **Category**: Shell & Scripting  
> **Paradigm**: Command-driven, functional, imperative  
> **Initial Release**: 1988  
> **Created By**: John Ousterhout  

---

## 1. Program 1: Hello World (`hello_world.tcl`)

```tcl
# ==========================================
# Program: Hello World in Tcl
# ==========================================
puts "Hello, World!"
```

### Explanation
`puts` outputs to default channel.

### Run Hello World
```bash
tclsh hello_world.tcl
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.tcl`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```tcl
# ==========================================
# Program: Basic Operations in Tcl (+, -, *, /, %)
# ==========================================
set a 20
set b 6

puts "a = $a, b = $b"
puts "Addition (a + b)        : [expr {$a + $b}]"
puts "Subtraction (a - b)     : [expr {$a - $b}]"
puts "Multiplication (a * b)  : [expr {$a * $b}]"
puts "Integer Division (a / b): [expr {$a / $b}]"
puts "Float Division          : [expr {double($a) / $b}]"
puts "Modulo (a % b)          : [expr {$a % $b}]"
```

### Explanation
In Tcl, all math is evaluated through the `expr` command within `[...]`.

### Run Basic Operations
```bash
tclsh basic_operations.tcl
```
**Expected Output**:
```text
a = 20, b = 6
Addition (a + b)        : 26
Subtraction (a - b)     : 14
Multiplication (a * b)  : 120
Integer Division (a / b): 3
Float Division          : 3.3333333333333335
Modulo (a % b)          : 2
```

---

## 3. Prerequisites & Installation

- **Guide**: tcl.tk
