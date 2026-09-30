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

---

## 3. Program 3: Control Flow & Logic (`control_flow.php`)
*Demonstrates conditional branching (`if/else`), pattern matching / multi-way `switch`, `for` iteration loops, and `while` loop.*

```php
<?php
// ==========================================
// Program: Control Flow in PHP
// ==========================================

function main() {
    // 1. Conditionals
    echo "Conditionals:\n";
    $num = 15;
    if ($num > 0) {
        if ($num % 2 === 0) {
            echo "{$num} is Positive and Even\n";
        } else {
            echo "{$num} is Positive and Odd\n";
        }
    } elseif ($num < 0) {
        echo "{$num} is Negative\n";
    } else {
        echo "Number is Zero\n";
    }

    echo "\nPattern Matching / Switch:\n";
    // 2. PHP 8.0+ Match Expression
    $grade = "B";
    $message = match ($grade) {
        "A" => "Grade A: Excellent!",
        "B" => "Grade B: Good Job!",
        "C" => "Grade C: Fair",
        default => "Keep Trying!"
    };
    echo $message . "\n";

    // 3. For Loop
    echo "\nFor Loop (1 to 5):\n";
    for ($i = 1; $i <= 5; $i++) {
        echo $i . ($i === 5 ? "\n" : " ");
    }

    // 4. While Loop
    echo "\nWhile Loop (Countdown):\n";
    $count = 3;
    while ($count > 0) {
        echo $count . " ";
        $count--;
    }
    echo "Blastoff!\n";
}

main();
?>
```

### Explanation
Demonstrates PHP `if/elseif/else` logic, modern `match` expression (PHP 8.0+), indexed `for` loop, and `while` loop.

### Run Control Flow
```bash
php control_flow.php
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
