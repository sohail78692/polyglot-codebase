# Clojure Reference Guide

> **Category**: Functional & Declarative  
> **Paradigm**: Functional Lisp dialect (JVM hosted)  
> **Initial Release**: 2007  
> **Created By**: Rich Hickey  

---

## 1. Program 1: Hello World (`hello_world.clj`)

```clj
;;; ==========================================
;;; Program: Hello World in Clojure
;;; ==========================================
(println "Hello, World!")
```

### Explanation
S-expression `(println "...")`.

### Run Hello World
```bash
clj -M hello_world.clj
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.clj`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```clj
;;; ==========================================
;;; Program: Basic Operations in Clojure (+, -, *, quot, mod)
;;; ==========================================
(let [a 20
      b 6]
  (println (str "a = " a ", b = " b))
  (println (str "Addition (+ a b)        : " (+ a b)))
  (println (str "Subtraction (- a b)     : " (- a b)))
  (println (str "Multiplication (* a b)  : " (* a b)))
  (println (str "Quotient (quot a b)     : " (quot a b)))
  (println (str "Exact Division (/ a b)  : " (/ a b)))
  (println (str "Modulo (mod a b)        : " (mod a b))))
```

### Explanation
In Lisp/Clojure, operators are prefix functions: `(+ a b)`. `(/ 20 6)` produces an exact Rational number `10/3`, while `(quot a b)` returns integer quotient.

### Run Basic Operations
```bash
clj -M basic_operations.clj
```
**Expected Output**:
```text
a = 20, b = 6
Addition (+ a b)        : 26
Subtraction (- a b)     : 14
Multiplication (* a b)  : 120
Quotient (quot a b)     : 3
Exact Division (/ a b)  : 10/3
Modulo (mod a b)        : 2
```

---

## 3. Prerequisites & Installation

- **Guide**: clojure.org
