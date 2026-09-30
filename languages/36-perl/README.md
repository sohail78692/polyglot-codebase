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

---

## 3. Program 3: Control Flow & Logic (`control_flow.pl`)
*Demonstrates conditional branching (`if/else`), pattern matching / multi-way `switch`, `for` iteration loops, and `while` loop.*

```pl
#!/usr/bin/env perl
use strict;
use warnings;

# ==========================================
# Program: Control Flow in Perl
# ==========================================

sub main {
    # 1. Conditionals
    print "Conditionals:\n";
    my $num = 15;
    if ($num > 0) {
        if ($num % 2 == 0) {
            print "$num is Positive and Even\n";
        } else {
            print "$num is Positive and Odd\n";
        }
    } elsif ($num < 0) {
        print "$num is Negative\n";
    } else {
        print "Number is Zero\n";
    }

    print "\nPattern Matching / Switch:\n";
    # 2. Dispatch / pattern switch
    my $grade = "B";
    my %grade_table = (
        "A" => "Grade A: Excellent!",
        "B" => "Grade B: Good Job!",
        "C" => "Grade C: Fair"
    );
    my $msg = $grade_table{$grade} // "Keep Trying!";
    print "$msg\n";

    # 3. For Loop over range
    print "\nFor Loop (1 to 5):\n";
    print join(" ", (1..5)) . "\n";

    # 4. While Loop
    print "\nWhile Loop (Countdown):\n";
    my $count = 3;
    while ($count > 0) {
        print "$count ";
        $count--;
    }
    print "Blastoff!\n";
}

main();
```

### Explanation
Demonstrates Perl `if/elsif/else`, modern `given/when` or hash dispatch, range-based `for my $i (1..5)`, and `while` loop.

### Run Control Flow
```bash
perl control_flow.pl
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
