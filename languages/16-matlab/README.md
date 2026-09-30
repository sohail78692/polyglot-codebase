# MATLAB / GNU Octave Reference Guide

> **Category**: Scientific & Data  
> **Paradigm**: Array programming, procedural  
> **Initial Release**: 1984  
> **Created By**: Cleve Moler (MathWorks)  

---

## 1. Program 1: Hello World (`hello_world.m`)

```m
% ==========================================
% Program: Hello World in MATLAB / GNU Octave
% ==========================================
disp('Hello, World!');
```

### Explanation
`disp` prints values without variable names.

### Run Hello World
```bash
octave --silent hello_world.m
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.m`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```m
% ==========================================
% Program: Basic Operations in MATLAB / GNU Octave
% ==========================================
a = 20;
b = 6;

fprintf('a = %d, b = %d\n', a, b);
fprintf('Addition (a + b)        : %d\n', a + b);
fprintf('Subtraction (a - b)     : %d\n', a - b);
fprintf('Multiplication (a * b)  : %d\n', a * b);
fprintf('Division (a / b)        : %f\n', a / b);
fprintf('Integer Division (idiv) : %d\n', fix(a / b));
fprintf('Modulo (mod(a, b))      : %d\n', mod(a, b));
```

### Explanation
`fprintf` formats output; `fix(a / b)` truncates to integer; `mod(a, b)` calculates modulo.

### Run Basic Operations
```bash
octave --silent basic_operations.m
```
**Expected Output**:
```text
a = 20, b = 6
Addition (a + b)        : 26
Subtraction (a - b)     : 14
Multiplication (a * b)  : 120
Division (a / b)        : 3.333333
Integer Division (idiv) : 3
Modulo (mod(a, b))      : 2
```

---

## 3. Prerequisites & Installation

- **Guide**: MATLAB or GNU Octave

---

## 3. Program 3: Control Flow & Logic (`control_flow.m`)
*Demonstrates conditional branching (`if/else`), pattern matching / multi-way `switch`, `for` iteration loops, and `while` loop.*

```m
% ==========================================
% Program: Control Flow in MATLAB / Octave
% ==========================================

function main()
    % 1. Conditionals
    disp("Conditionals:");
    num = 15;
    if num > 0
        if rem(num, 2) == 0
            fprintf("%d is Positive and Even\n", num);
        else
            fprintf("%d is Positive and Odd\n", num);
        end
    elseif num < 0
        fprintf("%d is Negative\n", num);
    else
        fprintf("Number is Zero\n");
    end

    fprintf("\nPattern Matching / Switch:\n");
    % 2. Switch Statement
    grade = 'B';
    switch grade
        case 'A'
            disp("Grade A: Excellent!");
        case 'B'
            disp("Grade B: Good Job!");
        case 'C'
            disp("Grade C: Fair");
        otherwise
            disp("Keep Trying!");
    end

    % 3. For Loop
    fprintf("\nFor Loop (1 to 5):\n");
    for i = 1:5
        if i == 5
            fprintf("%d\n", i);
        else
            fprintf("%d ", i);
        end
    end

    % 4. While Loop
    fprintf("\nWhile Loop (Countdown):\n");
    count = 3;
    while count > 0
        fprintf("%d ", count);
        count = count - 1;
    end
    fprintf("Blastoff!\n");
end

main();
```

### Explanation
Demonstrates MATLAB/GNU Octave matrix language `if/elseif/else`, `switch/case/otherwise`, index `for` loops, and `while` loop.

### Run Control Flow
```bash
octave -q control_flow.m
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
