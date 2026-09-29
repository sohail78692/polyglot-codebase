# Perl Reference Guide

> **Category**: Shell & Scripting  
> **Paradigm**: Multi-paradigm (Procedural, functional, OOP)  
> **Initial Release**: 1987  
> **Created By**: Larry Wall  

---

## 1. Program 1: Hello World (`hello_world.pl`)

```pl
#!/usr/bin/env perl
# ==========================================
# Program: Hello World in Perl
# ==========================================
use strict;
use warnings;

print "Hello, World!
";
```

### Explanation
`use strict;` and `print`.

### Run Hello World
```bash
perl hello_world.pl
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.pl`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```pl
#!/usr/bin/env perl
# ==========================================
# Program: Basic Operations in Perl (+, -, *, /, %)
# ==========================================
use strict;
use warnings;

my $a = 20;
my $b = 6;

print "a = $a, b = $b
";
print "Addition (a + b)        : " . ($a + $b) . "
";
print "Subtraction (a - b)     : " . ($a - $b) . "
";
print "Multiplication (a * b)  : " . ($a * $b) . "
";
print "Division (a / b)        : " . ($a / $b) . "
";
print "Integer Division (int)  : " . int($a / $b) . "
";
print "Modulo (a % b)          : " . ($a % $b) . "
";
```

### Explanation
Perl scalar variables use `$`. `int($a / $b)` truncates floating point division.

### Run Basic Operations
```bash
perl basic_operations.pl
```
**Expected Output**:
```text
a = 20, b = 6
Addition (a + b)        : 26
Subtraction (a - b)     : 14
Multiplication (a * b)  : 120
Division (a / b)        : 3.33333333333333
Integer Division (int)  : 3
Modulo (a % b)          : 2
```

---

## 3. Prerequisites & Installation

- **Guide**: perl.org
