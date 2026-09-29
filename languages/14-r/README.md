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
