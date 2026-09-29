/*
 * ==========================================
 * Program: Basic Operations in C (+, -, *, /, %)
 * ==========================================
 */
#include <stdio.h>

int main(void) {
    int a = 20;
    int b = 6;

    printf("a = %d, b = %d\n", a, b);
    printf("Addition (a + b)        : %d\n", a + b);
    printf("Subtraction (a - b)     : %d\n", a - b);
    printf("Multiplication (a * b)  : %d\n", a * b);
    printf("Integer Division (a / b): %d\n", a / b);             // Integer division truncates
    printf("Float Division (float)  : %f\n", (float)a / (float)b); // Type casting for float
    printf("Modulo (a % b)          : %d\n", a % b);             // Remainder operator

    return 0;
}
