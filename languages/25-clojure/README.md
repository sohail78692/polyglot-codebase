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

---

## 3. Program 3: Control Flow & Logic (`control_flow.clj`)
*Demonstrates conditional branching (`if/else`), pattern matching / multi-way `switch`, `for` iteration loops, and `while` loop.*

```clj
;; ==========================================
;; Program: Control Flow in Clojure
;; ==========================================

(ns control-flow)

(defn -main []
  ;; 1. Conditionals (cond)
  (println "Conditionals:")
  (let [num 15]
    (cond
      (> num 0) (if (zero? (mod num 2))
                  (println (str num " is Positive and Even"))
                  (println (str num " is Positive and Odd")))
      (< num 0) (println (str num " is Negative"))
      :else     (println "Number is Zero")))

  (println "\nPattern Matching / Switch:")
  ;; 2. Case macro
  (let [grade "B"]
    (println (case grade
               "A" "Grade A: Excellent!"
               "B" "Grade B: Good Job!"
               "C" "Grade C: Fair"
               "Keep Trying!")))

  ;; 3. For Loop via doseq
  (println "\nFor Loop (1 to 5):")
  (doseq [i (range 1 6)]
    (print (str i (if (= i 5) "\n" " "))))

  ;; 4. While Loop via loop/recur
  (println "\nWhile Loop (Countdown):")
  (loop [count 3]
    (if (> count 0)
      (do
        (print (str count " "))
        (recur (dec count)))
      (println "Blastoff!"))))

(-main)
```

### Explanation
Demonstrates Lisp S-expression conditionals (`if`, `cond`), `case` pattern matching, `doseq` iteration, and `loop/recur` tail recursion.

### Run Control Flow
```bash
clojure control_flow.clj
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
