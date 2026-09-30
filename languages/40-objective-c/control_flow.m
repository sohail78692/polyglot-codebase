// ==========================================
// Program: Control Flow in Objective-C
// ==========================================

#import <Foundation/Foundation.h>
#include <stdio.h>

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        // 1. Conditionals
        printf("Conditionals:\n");
        int num = 15;
        if (num > 0) {
            if (num % 2 == 0) {
                printf("%d is Positive and Even\n", num);
            } else {
                printf("%d is Positive and Odd\n", num);
            }
        } else if (num < 0) {
            printf("%d is Negative\n", num);
        } else {
            printf("Number is Zero\n");
        }

        printf("\nPattern Matching / Switch:\n");
        // 2. Switch Statement
        char grade = 'B';
        switch (grade) {
            case 'A':
                printf("Grade A: Excellent!\n");
                break;
            case 'B':
                printf("Grade B: Good Job!\n");
                break;
            case 'C':
                printf("Grade C: Fair\n");
                break;
            default:
                printf("Keep Trying!\n");
                break;
        }

        // 3. For Loop
        printf("\nFor Loop (1 to 5):\n");
        for (int i = 1; i <= 5; i++) {
            printf("%d%s", i, (i == 5 ? "\n" : " "));
        }

        // 4. While Loop
        printf("\nWhile Loop (Countdown):\n");
        int count = 3;
        while (count > 0) {
            printf("%d ", count);
            count--;
        }
        printf("Blastoff!\n");
    }
    return 0;
}
