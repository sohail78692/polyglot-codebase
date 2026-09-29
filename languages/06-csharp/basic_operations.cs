// ==========================================
// Program: Basic Operations in C# (+, -, *, /, %)
// ==========================================
using System;

namespace BasicOperationsApp
{
    class Program
    {
        static void Main(string[] args)
        {
            int a = 20;
            int b = 6;

            Console.WriteLine($"a = {a}, b = {b}");
            Console.WriteLine($"Addition (a + b)        : {a + b}");
            Console.WriteLine($"Subtraction (a - b)     : {a - b}");
            Console.WriteLine($"Multiplication (a * b)  : {a * b}");
            Console.WriteLine($"Integer Division (a / b): {a / b}");
            Console.WriteLine($"Float Division (double) : {(double)a / b}");
            Console.WriteLine($"Modulo (a % b)          : {a % b}");
        }
    }
}
