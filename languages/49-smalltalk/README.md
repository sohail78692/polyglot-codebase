# Smalltalk Reference Guide

> **Category**: Classic & Foundational  
> **Paradigm**: Pure object-oriented, message passing  
> **Initial Release**: 1972  
> **Created By**: Alan Kay et al. (Xerox PARC)  

---

## 1. Program 1: Hello World (`hello_world.st`)

```st
"==========================================
 Program: Hello World in Smalltalk
 =========================================="
Transcript show: 'Hello, World!'; cr.
```

### Explanation
`Transcript show: '...'; cr.` message sending.

### Run Hello World
```bash
gst hello_world.st
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.st`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```st
"==========================================
 Program: Basic Operations in Smalltalk (+, -, *, //, \\)
 =========================================="
| a b |
a := 20.
b := 6.

Transcript show: 'a = 20, b = 6'; cr.
Transcript show: 'Addition (a + b)        : ', (a + b) printString; cr.
Transcript show: 'Subtraction (a - b)     : ', (a - b) printString; cr.
Transcript show: 'Multiplication (a * b)  : ', (a * b) printString; cr.
Transcript show: 'Integer Division (//)   : ', (a // b) printString; cr.
Transcript show: 'Exact Fraction (/)      : ', (a / b) printString; cr.
Transcript show: 'Modulo (\\)             : ', (a \\ b) printString; cr.
```

### Explanation
In Smalltalk, `+`, `-`, `*` are binary messages sent to number objects. `//` is integer division, `/` yields a Fraction, and `\\` calculates modulo.

### Run Basic Operations
```bash
gst basic_operations.st
```
**Expected Output**:
```text
a = 20, b = 6
Addition (a + b)        : 26
Subtraction (a - b)     : 14
Multiplication (a * b)  : 120
Integer Division (//)   : 3
Exact Fraction (/)      : (10/3)
Modulo (\\)             : 2
```

---

## 3. Prerequisites & Installation

- **Guide**: GNU Smalltalk (gst)

---

## 3. Program 3: Control Flow & Logic (`control_flow.st`)
*Demonstrates conditional branching (`if/else`), pattern matching / multi-way `switch`, `for` iteration loops, and `while` loop.*

```st
"==========================================
 Program: Control Flow in Smalltalk (GNU Smalltalk)
 =========================================="

| num grade count forItems whileItems |

Transcript show: 'Conditionals:'; cr.
num := 15.
(num > 0)
    ifTrue: [
        ((num \ 2) = 0)
            ifTrue: [ Transcript show: num printString, ' is Positive and Even'; cr ]
            ifFalse: [ Transcript show: num printString, ' is Positive and Odd'; cr ] ]
    ifFalse: [ Transcript show: 'Not positive'; cr ].

Transcript cr.
Transcript show: 'Pattern Matching / Switch:'; cr.
grade := 'B'.
(grade = 'A') ifTrue: [ Transcript show: 'Grade A: Excellent!'; cr ].
(grade = 'B') ifTrue: [ Transcript show: 'Grade B: Good Job!'; cr ].
(grade = 'C') ifTrue: [ Transcript show: 'Grade C: Fair'; cr ].

Transcript cr.
Transcript show: 'For Loop (1 to 5):'; cr.
forItems := OrderedCollection new.
1 to: 5 do: [ :i | forItems add: i printString ].
Transcript show: (forItems fold: [ :a :b | a, ' ', b ]); cr.

Transcript cr.
Transcript show: 'While Loop (Countdown):'; cr.
count := 3.
whileItems := OrderedCollection new.
[ count > 0 ] whileTrue: [
    whileItems add: count printString.
    count := count - 1.
].
whileItems add: 'Blastoff!'.
Transcript show: (whileItems fold: [ :a :b | a, ' ', b ]); cr.
```

### Explanation
Demonstrates Smalltalk pure object message passing for control flow: `ifTrue:ifFalse:`, dictionary/block dispatch, `to:do:`, and `whileTrue:`.

### Run Control Flow
```bash
gst control_flow.st
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
