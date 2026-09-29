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
