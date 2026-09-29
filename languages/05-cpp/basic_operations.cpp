/*
 * ==========================================
 * Program: Basic Operations in C++ (+, -, *, /, %)
 * ==========================================
 */
#include <iostream>

int main() {
    int a = 20;
    int b = 6;

    std::cout << "a = " << a << ", b = " << b << std::endl;
    std::cout << "Addition (a + b)        : " << (a + b) << std::endl;
    std::cout << "Subtraction (a - b)     : " << (a - b) << std::endl;
    std::cout << "Multiplication (a * b)  : " << (a * b) << std::endl;
    std::cout << "Integer Division (a / b): " << (a / b) << std::endl;
    std::cout << "Float Division (double) : " << (static_cast<double>(a) / b) << std::endl;
    std::cout << "Modulo (a % b)          : " << (a % b) << std::endl;

    return 0;
}
