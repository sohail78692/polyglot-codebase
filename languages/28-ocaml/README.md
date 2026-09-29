# OCaml Reference Guide

> **Category**: Functional & Declarative  
> **Paradigm**: Multi-paradigm (Functional, imperative, OOP)  
> **Initial Release**: 1996  
> **Created By**: INRIA  

---

## 1. Program 1: Hello World (`hello_world.ml`)

```ml
(* ==========================================
   Program: Hello World in OCaml
   ========================================== *)
let () = print_endline "Hello, World!"
```

### Explanation
`print_endline` prints text with a newline.

### Run Hello World
```bash
ocaml hello_world.ml
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.ml`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```ml
(* ==========================================
   Program: Basic Operations in OCaml (+, -, *, /, mod)
   ========================================== *)
let () =
  let a = 20 in
  let b = 6 in
  Printf.printf "a = %d, b = %d\n" a b;
  Printf.printf "Addition (a + b)        : %d\n" (a + b);
  Printf.printf "Subtraction (a - b)     : %d\n" (a - b);
  Printf.printf "Multiplication (a * b)  : %d\n" (a * b);
  Printf.printf "Integer Division (a / b): %d\n" (a / b);
  Printf.printf "Float Division (float)  : %f\n" (float_of_int a /. float_of_int b);
  Printf.printf "Modulo (a mod b)        : %d\n" (a mod b)
```

### Explanation
OCaml separates integer operators (`+`, `-`, `*`, `/`) from float operators (`+.`, `-.`, `*.`, `/.`). `mod` is modulo.

### Run Basic Operations
```bash
ocaml basic_operations.ml
```
**Expected Output**:
```text
a = 20, b = 6
Addition (a + b)        : 26
Subtraction (a - b)     : 14
Multiplication (a * b)  : 120
Integer Division (a / b): 3
Float Division (float)  : 3.333333
Modulo (a mod b)        : 2
```

---

## 3. Prerequisites & Installation

- **Guide**: ocaml.org / opam
