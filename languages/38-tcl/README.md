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

---

## 3. Program 3: Control Flow & Logic (`control_flow.tcl`)
*Demonstrates conditional branching (`if/else`), pattern matching / multi-way `switch`, `for` iteration loops, and `while` loop.*

```tcl
# ==========================================
# Program: Control Flow in Tcl
# ==========================================

proc main {} {
    # 1. Conditionals
    puts "Conditionals:"
    set num 15
    if {$num > 0} {
        if {$num % 2 == 0} {
            puts "$num is Positive and Even"
        } else {
            puts "$num is Positive and Odd"
        }
    } elseif {$num < 0} {
        puts "$num is Negative"
    } else {
        puts "Number is Zero"
    }

    puts "\nPattern Matching / Switch:"
    # 2. Switch command
    set grade "B"
    switch $grade {
        "A" { puts "Grade A: Excellent!" }
        "B" { puts "Grade B: Good Job!" }
        "C" { puts "Grade C: Fair" }
        default { puts "Keep Trying!" }
    }

    # 3. For loop
    puts "\nFor Loop (1 to 5):"
    set forList {}
    for {set i 1} {$i <= 5} {incr i} {
        lappend forList $i
    }
    puts [join $forList " "]

    # 4. While loop
    puts "\nWhile Loop (Countdown):"
    set count 3
    set whileList {}
    while {$count > 0} {
        lappend whileList $count
        incr count -1
    }
    lappend whileList "Blastoff!"
    puts [join $whileList " "]
}

main
```

### Explanation
Demonstrates Tcl command-based syntax `if/elseif/else`, `switch` command, `for` loop command, and `while` countdown loop.

### Run Control Flow
```bash
tclsh control_flow.tcl
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
