# R Reference Guide

> **Category**: Scientific & Data  
> **Paradigm**: Multi-paradigm (Functional, array, procedural)  
> **Initial Release**: 1993  
> **Created By**: Ross Ihaka and Robert Gentleman  

---

## 1. Program 1: Hello World (`hello_world.r`)

```r
# ==========================================
# Program: Hello World in R
# ==========================================
cat("Hello, World!
")
```

### Explanation
`cat()` prints text without vector indices.

### Run Hello World
```bash
Rscript hello_world.r
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.r`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```r
# ==========================================
# Program: Basic Operations in R (+, -, *, /, %/%, %%)
# ==========================================
a <- 20
b <- 6

cat(sprintf("a = %d, b = %d
", a, b))
cat(sprintf("Addition (a + b)        : %d
", a + b))
cat(sprintf("Subtraction (a - b)     : %d
", a - b))
cat(sprintf("Multiplication (a * b)  : %d
", a * b))
cat(sprintf("Division (a / b)        : %f
", a / b))
cat(sprintf("Integer Division (a %%/%% b): %d
", a %/% b)) # %/% is integer division in R
cat(sprintf("Modulo (a %%%% b)         : %d
", a %% b))   # %% is modulo in R
```

### Explanation
In R, integer division is `%/%` and modulo is `%%`.

### Run Basic Operations
```bash
Rscript basic_operations.r
```
**Expected Output**:
```text
a = 20, b = 6
Addition (a + b)        : 26
Subtraction (a - b)     : 14
Multiplication (a * b)  : 120
Division (a / b)        : 3.333333
Integer Division (a %/% b): 3
Modulo (a %% b)         : 2
```

---

## 3. Prerequisites & Installation

- **Guide**: r-project.org

---

## 3. Program 3: Control Flow & Logic (`control_flow.r`)
*Demonstrates conditional branching (`if/else`), pattern matching / multi-way `switch`, `for` iteration loops, and `while` loop.*

```r
# ==========================================
# Program: Control Flow in R
# ==========================================

main <- function() {
  # 1. Conditionals
  cat("Conditionals:\n")
  num <- 15
  if (num > 0) {
    if (num %% 2 == 0) {
      cat(num, "is Positive and Even\n")
    } else {
      cat(num, "is Positive and Odd\n")
    }
  } else if (num < 0) {
    cat(num, "is Negative\n")
  } else {
    cat("Number is Zero\n")
  }

  cat("\nPattern Matching / Switch:\n")
  # 2. Switch function
  grade <- "B"
  msg <- switch(grade,
    "A" = "Grade A: Excellent!",
    "B" = "Grade B: Good Job!",
    "C" = "Grade C: Fair",
    "Keep Trying!"
  )
  cat(msg, "\n")

  # 3. For Loop
  cat("\nFor Loop (1 to 5):\n")
  cat(paste(1:5, collapse = " "), "\n")

  # 4. While Loop
  cat("\nWhile Loop (Countdown):\n")
  count <- 3
  while (count > 0) {
    cat(count, "")
    count <- count - 1
  }
  cat("Blastoff!\n")
}

main()
```

### Explanation
Demonstrates R vector conditionals, `switch()` evaluation, vector `for` loops, and `while` countdowns.

### Run Control Flow
```bash
Rscript control_flow.r
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
