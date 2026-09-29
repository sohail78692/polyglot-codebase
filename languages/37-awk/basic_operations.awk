# ==========================================
# Program: Basic Operations in AWK (+, -, *, /, %)
# ==========================================
BEGIN {
    a = 20
    b = 6

    printf "a = %d, b = %d\n", a, b
    printf "Addition (a + b)        : %d\n", a + b
    printf "Subtraction (a - b)     : %d\n", a - b
    printf "Multiplication (a * b)  : %d\n", a * b
    printf "Division (a / b)        : %f\n", a / b
    printf "Integer Division (int)  : %d\n", int(a / b)
    printf "Modulo (a %%%% b)          : %d\n", a % b
}
