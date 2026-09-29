# Common Lisp Reference Guide

> **Category**: Functional & Declarative  
> **Paradigm**: Multi-paradigm (Symbolic, functional, procedural, OOP)  
> **Initial Release**: 1984  
> **Created By**: Guy L. Steele Jr. et al.  

---

## 1. Program 1: Hello World (`hello_world.lisp`)

```lisp
;;; ==========================================
;;; Program: Hello World in Common Lisp
;;; ==========================================
(format t "Hello, World!~%")
```

### Explanation
`format t` writes to stdout.

### Run Hello World
```bash
sbcl --script hello_world.lisp
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.lisp`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```lisp
;;; ==========================================
;;; Program: Basic Operations in Common Lisp (+, -, *, /, mod)
;;; ==========================================
(let ((a 20)
      (b 6))
  (format t "a = ~A, b = ~A~%" a b)
  (format t "Addition (+ a b)        : ~A~%" (+ a b))
  (format t "Subtraction (- a b)     : ~A~%" (- a b))
  (format t "Multiplication (* a b)  : ~A~%" (* a b))
  (format t "Floor Quotient          : ~A~%" (floor a b))
  (format t "Exact Division (/ a b)  : ~A~%" (/ a b))
  (format t "Modulo (mod a b)        : ~A~%" (mod a b)))
```

### Explanation
Common Lisp provides built-in exact rational division `(/ 20 6) -> 10/3` and `(mod a b)` for remainder.

### Run Basic Operations
```bash
sbcl --script basic_operations.lisp
```
**Expected Output**:
```text
a = 20, b = 6
Addition (+ a b)        : 26
Subtraction (- a b)     : 14
Multiplication (* a b)  : 120
Floor Quotient          : 3
Exact Division (/ a b)  : 10/3
Modulo (mod a b)        : 2
```

---

## 3. Prerequisites & Installation

- **Guide**: SBCL
