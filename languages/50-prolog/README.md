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

---

## 3. Program 3: Control Flow & Logic (`control_flow.pl`)
*Demonstrates conditional branching (`if/else`), pattern matching / multi-way `switch`, `for` iteration loops, and `while` loop.*

```pl
% ==========================================
% Program: Control Flow in Prolog
% ==========================================

% 1. Conditional classification clauses
classify_num(N) :-
    N > 0,
    1 is N mod 2,
    write(N), write(' is Positive and Odd'), nl.
classify_num(N) :-
    N > 0,
    0 is N mod 2,
    write(N), write(' is Positive and Even'), nl.
classify_num(N) :-
    N < 0,
    write(N), write(' is Negative'), nl.
classify_num(_) :-
    write('Number is Zero'), nl.

% 2. Unification pattern matching (Switch equivalent)
grade_feedback('A') :- write('Grade A: Excellent!'), nl.
grade_feedback('B') :- write('Grade B: Good Job!'), nl.
grade_feedback('C') :- write('Grade C: Fair'), nl.
grade_feedback(_)   :- write('Keep Trying!'), nl.

% 3. Recursive loop (For loop equivalent)
for_loop(I, Max) :-
    I =< Max,
    write(I),
    (I =:= Max -> nl ; write(' ')),
    Next is I + 1,
    for_loop(Next, Max).
for_loop(I, Max) :- I > Max.

% 4. Recursive countdown (While loop equivalent)
countdown(0) :-
    write('Blastoff!'), nl.
countdown(N) :-
    N > 0,
    write(N), write(' '),
    Next is N - 1,
    countdown(Next).

main :-
    write('Conditionals:'), nl,
    classify_num(15),
    nl,
    write('Pattern Matching / Switch:'), nl,
    grade_feedback('B'),
    nl,
    write('For Loop (1 to 5):'), nl,
    for_loop(1, 5),
    nl,
    write('While Loop (Countdown):'), nl,
    countdown(3),
    halt.
```

### Explanation
Demonstrates Prolog logic-based branching via multiple clause predicates, unification pattern matching, and recursive predicates for loops.

### Run Control Flow
```bash
gprolog --consult-file control_flow.pl --entry-goal main
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
