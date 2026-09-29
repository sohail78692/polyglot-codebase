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
