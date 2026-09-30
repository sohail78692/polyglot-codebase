// ==========================================
// Program: Control Flow in D
// ==========================================

import std.stdio;

void main() {
    // 1. Conditionals
    writeln("Conditionals:");
    int num = 15;
    if (num > 0) {
        if (num % 2 == 0) {
            writefln("%d is Positive and Even", num);
        } else {
            writefln("%d is Positive and Odd", num);
        }
    } else if (num < 0) {
        writefln("%d is Negative", num);
    } else {
        writeln("Number is Zero");
    }

    writeln("\nPattern Matching / Switch:");
    // 2. Switch Statement
    char grade = 'B';
    switch (grade) {
        case 'A':
            writeln("Grade A: Excellent!");
            break;
        case 'B':
            writeln("Grade B: Good Job!");
            break;
        case 'C':
            writeln("Grade C: Fair");
            break;
        default:
            writeln("Keep Trying!");
            break;
    }

    // 3. For Loop
    writeln("\nFor Loop (1 to 5):");
    foreach (i; 1 .. 6) {
        write(i, i == 5 ? "\n" : " ");
    }

    // 4. While Loop
    writeln("\nWhile Loop (Countdown):");
    int count = 3;
    while (count > 0) {
        write(count, " ");
        count--;
    }
    writeln("Blastoff!");
}
