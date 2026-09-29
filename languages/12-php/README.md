# PHP Reference Guide

> **Category**: Mainstream & Systems  
> **Paradigm**: Multi-paradigm (Imperative, OOP, procedural)  
> **Initial Release**: 1995  
> **Created By**: Rasmus Lerdorf  

---

## 1. Program 1: Hello World (`hello_world.php`)

```php
<?php
// ==========================================
// Program: Hello World in PHP
// ==========================================
echo "Hello, World!
";
?>
```

### Explanation
`echo` outputs strings to stdout.

### Run Hello World
```bash
php hello_world.php
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.php`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```php
<?php
// ==========================================
// Program: Basic Operations in PHP (+, -, *, /, %)
// ==========================================
$a = 20;
$b = 6;

echo "a = $a, b = $b
";
echo "Addition (a + b)        : " . ($a + $b) . "
";
echo "Subtraction (a - b)     : " . ($a - $b) . "
";
echo "Multiplication (a * b)  : " . ($a * $b) . "
";
echo "Division (a / b)        : " . ($a / $b) . "
";
echo "Integer Division (intdiv): " . intdiv($a, $b) . "
";
echo "Modulo (a % b)          : " . ($a % $b) . "
";
?>
```

### Explanation
In PHP, variables start with `$`. String concatenation uses `.` and `intdiv()` provides explicit integer division.

### Run Basic Operations
```bash
php basic_operations.php
```
**Expected Output**:
```text
a = 20, b = 6
Addition (a + b)        : 26
Subtraction (a - b)     : 14
Multiplication (a * b)  : 120
Division (a / b)        : 3.3333333333333
Integer Division (intdiv): 3
Modulo (a % b)          : 2
```

---

## 3. Prerequisites & Installation

- **Guide**: php.net
