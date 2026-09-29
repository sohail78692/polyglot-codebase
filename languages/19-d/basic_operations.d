// ==========================================
// Program: Basic Operations in D (+, -, *, /, %)
// ==========================================
import std.stdio;

void main() {
    int a = 20;
    int b = 6;

    writefln("a = %d, b = %d", a, b);
    writefln("Addition (a + b)        : %d", a + b);
    writefln("Subtraction (a - b)     : %d", a - b);
    writefln("Multiplication (a * b)  : %d", a * b);
    writefln("Integer Division (a / b): %d", a / b);
    writefln("Float Division (double) : %f", cast(double)a / b);
    writefln("Modulo (a % b)          : %d", a % b);
}
