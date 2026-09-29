// ==========================================
// Program: Basic Operations in Objective-C (+, -, *, /, %)
// ==========================================
#import <Foundation/Foundation.h>

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        int a = 20;
        int b = 6;

        NSLog(@"a = %d, b = %d", a, b);
        NSLog(@"Addition (a + b)        : %d", a + b);
        NSLog(@"Subtraction (a - b)     : %d", a - b);
        NSLog(@"Multiplication (a * b)  : %d", a * b);
        NSLog(@"Integer Division (a / b): %d", a / b);
        NSLog(@"Float Division (double) : %f", (double)a / b);
        NSLog(@"Modulo (a %% b)          : %d", a % b);
    }
    return 0;
}
