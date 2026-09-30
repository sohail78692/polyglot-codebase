# Scheme / Racket Reference Guide

> **Category**: Functional & Declarative  
> **Paradigm**: Functional (Lisp dialect)  
> **Initial Release**: 1975  
> **Created By**: Guy L. Steele & Gerald Jay Sussman  

---

## 1. Program 1: Hello World (`hello_world.rkt`)

```rkt
#lang racket
;; ==========================================
;; Program: Hello World in Racket / Scheme
;; ==========================================
(displayln "Hello, World!")
```

### Explanation
`displayln` outputs string to port.

### Run Hello World
```bash
racket hello_world.rkt
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.rkt`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```rkt
#lang racket
;; ==========================================
;; Program: Basic Operations in Racket / Scheme
;; ==========================================
(define a 20)
(define b 6)

(printf "a = ~a, b = ~a\n" a b)
(printf "Addition: ~a, Subtraction: ~a, Multiplication: ~a, Quotient: ~a, Exact Division: ~a, Remainder: ~a\n"
        (+ a b)
        (- a b)
        (* a b)
        (quotient a b)
        (/ a b)
        (remainder a b))
```

### Explanation
`quotient` computes integer division, `/` computes rational fractions, and `remainder` computes modulo.

### Run Basic Operations
```bash
racket basic_operations.rkt
```
**Expected Output**:
```text
a = 20, b = 6
Addition: 26, Subtraction: 14, Multiplication: 120, Quotient: 3, Exact Division: 10/3, Remainder: 2
```

---

## 3. Prerequisites & Installation

- **Guide**: racket-lang.org

---

## 3. Program 3: Control Flow & Logic (`control_flow.rkt`)
*Demonstrates conditional branching (`if/else`), pattern matching / multi-way `switch`, `for` iteration loops, and `while` loop.*

```rkt
#lang racket
;; ==========================================
;; Program: Control Flow in Scheme / Racket
;; ==========================================

(define (main)
  ;; 1. Conditionals (cond)
  (displayln "Conditionals:")
  (define num 15)
  (cond
    [(> num 0)
     (if (= (remainder num 2) 0)
         (printf "~a is Positive and Even\n" num)
         (printf "~a is Positive and Odd\n" num))]
    [(< num 0) (printf "~a is Negative\n" num)]
    [else (displayln "Number is Zero")])

  (displayln "\nPattern Matching / Switch:")
  ;; 2. Case statement
  (define grade 'B)
  (case grade
    [(A) (displayln "Grade A: Excellent!")]
    [(B) (displayln "Grade B: Good Job!")]
    [(C) (displayln "Grade C: Fair")]
    [else (displayln "Keep Trying!")])

  ;; 3. For loop
  (displayln "\nFor Loop (1 to 5):")
  (for ([i (in-range 1 6)])
    (display i)
    (if (= i 5) (newline) (display " ")))

  ;; 4. While loop via named let recursion
  (displayln "\nWhile Loop (Countdown):")
  (let loop ([count 3])
    (when (> count 0)
      (printf "~a " count)
      (loop (- count 1))))
  (displayln "Blastoff!"))

(main)
```

### Explanation
Demonstrates Scheme S-expression `cond`, `case` branching, `for` iteration loops, and named `let` countdown recursion.

### Run Control Flow
```bash
racket control_flow.rkt
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
