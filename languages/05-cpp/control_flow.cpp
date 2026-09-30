// ==========================================
// Program: Control Flow in C++
// ==========================================

#include <iostream>

int main() {
    // 1. Conditionals
    std::cout << "Conditionals:\n";
    int num = 15;
    if (num > 0) {
        if (num % 2 == 0) {
            std::cout << num << " is Positive and Even\n";
        } else {
            std::cout << num << " is Positive and Odd\n";
        }
    } else if (num < 0) {
        std::cout << num << " is Negative\n";
    } else {
        std::cout << "Number is Zero\n";
    }

    std::cout << "\nPattern Matching / Switch:\n";
    // 2. Switch statement
    char grade = 'B';
    switch (grade) {
        case 'A':
            std::cout << "Grade A: Excellent!\n";
            break;
        case 'B':
            std::cout << "Grade B: Good Job!\n";
            break;
        case 'C':
            std::cout << "Grade C: Fair\n";
            break;
        default:
            std::cout << "Keep Trying!\n";
            break;
    }

    // 3. For Loop
    std::cout << "\nFor Loop (1 to 5):\n";
    for (int i = 1; i <= 5; ++i) {
        std::cout << i << (i == 5 ? "\n" : " ");
    }

    // 4. While Loop
    std::cout << "\nWhile Loop (Countdown):\n";
    int count = 3;
    while (count > 0) {
        std::cout << count << " ";
        --count;
    }
    std::cout << "Blastoff!\n";

    return 0;
}
