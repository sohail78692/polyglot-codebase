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

---

## 3. Program 3: Control Flow & Logic (`control_flow.ml`)
*Demonstrates conditional branching (`if/else`), pattern matching / multi-way `switch`, `for` iteration loops, and `while` loop.*

```ml
(* ==========================================
   Program: Control Flow in OCaml
   ========================================== *)

let () =
  (* 1. Conditionals *)
  print_endline "Conditionals:";
  let num = 15 in
  if num > 0 then
    if num mod 2 = 0 then
      Printf.printf "%d is Positive and Even\n" num
    else
      Printf.printf "%d is Positive and Odd\n" num
  else if num < 0 then
    Printf.printf "%d is Negative\n" num
  else
    print_endline "Number is Zero";

  print_endline "\nPattern Matching / Switch:";
  (* 2. Pattern Matching *)
  let grade = "B" in
  let msg = match grade with
    | "A" -> "Grade A: Excellent!"
    | "B" -> "Grade B: Good Job!"
    | "C" -> "Grade C: Fair"
    | _   -> "Keep Trying!"
  in
  print_endline msg;

  (* 3. For Loop *)
  print_endline "\nFor Loop (1 to 5):";
  for i = 1 to 5 do
    Printf.printf "%d%s" i (if i = 5 then "\n" else " ")
  done;

  (* 4. While Loop *)
  print_endline "\nWhile Loop (Countdown):";
  let count = ref 3 in
  while !count > 0 do
    Printf.printf "%d " !count;
    decr count
  done;
  print_endline "Blastoff!"
```

### Explanation
Demonstrates OCaml `if/then/else` expressions, `match ... with` pattern matching, and `for i = 1 to 5 do` and `while` loops.

### Run Control Flow
```bash
ocaml control_flow.ml
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
