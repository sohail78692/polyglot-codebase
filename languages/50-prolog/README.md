# Prolog Reference Guide

> **Category**: Classic & Foundational  
> **Paradigm**: Declarative, Logic programming  
> **Initial Release**: 1972  
> **Created By**: Alain Colmerauer and Philippe Roussel  

---

## 1. Program 1: Hello World (`hello_world.pl`)

```pl
% ==========================================
% Program: Hello World in Prolog (SWI-Prolog)
% ==========================================
:- initialization(main).

main :-
    write('Hello, World!'), nl,
    halt.
```

### Explanation
`write('...')`, `nl`, and `halt`.

### Run Hello World
```bash
swipl -q -t main -f hello_world.pl
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.pl`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```pl
% ==========================================
% Program: Basic Operations in Prolog (+, -, *, //, mod)
% ==========================================
:- initialization(main).

main :-
    A = 20,
    B = 6,
    Add is A + B,
    Sub is A - B,
    Mul is A * B,
    Div is A // B,   % // is integer division in ISO Prolog
    Mod is A mod B,  % mod is modulo remainder
    format('a = ~w, b = ~w~n', [A, B]),
    format('Addition: ~w, Subtraction: ~w, Multiplication: ~w, Division: ~w, Modulo: ~w~n',
           [Add, Sub, Mul, Div, Mod]),
    halt.
```

### Explanation
In Prolog, arithmetic is evaluated using the `is` operator: `Add is A + B`. `//` is integer division and `mod` calculates remainder.

### Run Basic Operations
```bash
swipl -q -t main -f basic_operations.pl
```
**Expected Output**:
```text
a = 20, b = 6
Addition: 26, Subtraction: 14, Multiplication: 120, Division: 3, Modulo: 2
```

---

## 3. Prerequisites & Installation

- **Guide**: SWI-Prolog
