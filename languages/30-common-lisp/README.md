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

---

## 3. Program 3: Control Flow & Logic (`control_flow.lisp`)
*Demonstrates conditional branching (`if/else`), pattern matching / multi-way `switch`, `for` iteration loops, and `while` loop.*

```lisp
;; ==========================================
;; Program: Control Flow in Common Lisp
;; ==========================================

(defun main ()
  ;; 1. Conditionals (cond)
  (format t "Conditionals:~%")
  (let ((num 15))
    (cond
      ((> num 0)
       (if (= (mod num 2) 0)
           (format t "~A is Positive and Even~%" num)
           (format t "~A is Positive and Odd~%" num)))
      ((< num 0) (format t "~A is Negative~%" num))
      (t (format t "Number is Zero~%"))))

  (format t "~%Pattern Matching / Switch:~%")
  ;; 2. Case macro
  (let ((grade 'B))
    (case grade
      (A (format t "Grade A: Excellent!~%"))
      (B (format t "Grade B: Good Job!~%"))
      (C (format t "Grade C: Fair~%"))
      (otherwise (format t "Keep Trying!~%"))))

  ;; 3. For loop (loop for i from 1 to 5)
  (format t "~%For Loop (1 to 5):~%")
  (loop for i from 1 to 5 do
    (format t "~A~A" i (if (= i 5) "~%" " ")))

  ;; 4. While loop (countdown)
  (format t "~%While Loop (Countdown):~%")
  (let ((count 3))
    (loop while (> count 0) do
      (format t "~A " count)
      (decf count)))
  (format t "Blastoff!~%"))

(main)
```

### Explanation
Demonstrates Common Lisp `if`, `cond`, `case` macros, `dotimes` / `loop for i from 1 to 5`, and `loop while` constructs.

### Run Control Flow
```bash
sbcl --script control_flow.lisp
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
