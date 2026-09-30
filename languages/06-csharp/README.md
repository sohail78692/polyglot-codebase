# C# Reference Guide

> **Category**: Mainstream & Systems  
> **Paradigm**: Multi-paradigm (Object-oriented, component-oriented, functional)  
> **Initial Release**: 2000  
> **Created By**: Anders Hejlsberg (Microsoft)  

---

## 1. Program 1: Hello World (`hello_world.cs`)

```cs
// ==========================================
// Program: Hello World in C# (.NET)
// ==========================================
using System;

namespace HelloWorldApp
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");
        }
    }
}
```

### Explanation
`Console.WriteLine` writes to stdout in C#.

### Run Hello World
```bash
dotnet run (or csc hello_world.cs && ./hello_world.exe)
```
**Expected Output**:
```text
Hello, World!
```

---

## 2. Program 2: Basic Operations (`basic_operations.cs`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```cs
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
```

### Explanation
C# supports string interpolation `$"{...}"` with standard operators `+`, `-`, `*`, `/`, `%`.

### Run Basic Operations
```bash
csc basic_operations.cs && ./basic_operations.exe
```
**Expected Output**:
```text
a = 20, b = 6
Addition (a + b)        : 26
Subtraction (a - b)     : 14
Multiplication (a * b)  : 120
Integer Division (a / b): 3
Float Division (double) : 3.3333333333333335
Modulo (a % b)          : 2
```

---

## 3. Prerequisites & Installation

- **Guide**: .NET SDK

---

## 3. Program 3: Control Flow & Logic (`control_flow.cs`)
*Demonstrates conditional branching (`if/else`), pattern matching / multi-way `switch`, `for` iteration loops, and `while` loop.*

```cs
// ==========================================
// Program: Control Flow in C#
// ==========================================

using System;

class Program
{
    static void Main()
    {
        // 1. Conditionals
        Console.WriteLine("Conditionals:");
        int num = 15;
        if (num > 0)
        {
            if (num % 2 == 0)
                Console.WriteLine($"{num} is Positive and Even");
            else
                Console.WriteLine($"{num} is Positive and Odd");
        }
        else if (num < 0)
        {
            Console.WriteLine($"{num} is Negative");
        }
        else
        {
            Console.WriteLine("Number is Zero");
        }

        Console.WriteLine("\nPattern Matching / Switch:");
        // 2. Switch Expression
        string grade = "B";
        string feedback = grade switch
        {
            "A" => "Grade A: Excellent!",
            "B" => "Grade B: Good Job!",
            "C" => "Grade C: Fair",
            _   => "Keep Trying!"
        };
        Console.WriteLine(feedback);

        // 3. For Loop
        Console.WriteLine("\nFor Loop (1 to 5):");
        for (int i = 1; i <= 5; i++)
        {
            Console.Write(i + (i == 5 ? "\n" : " "));
        }

        // 4. While Loop
        Console.WriteLine("\nWhile Loop (Countdown):");
        int count = 3;
        while (count > 0)
        {
            Console.Write(count + " ");
            count--;
        }
        Console.WriteLine("Blastoff!");
    }
}
```

### Explanation
Demonstrates C# `if/else`, modern switch expression (`grade switch { ... }`), `for` loop, and `while` loop.

### Run Control Flow
```bash
dotnet run
```
**Expected Output**:
```text
Conditionals:
15 is Positive and Odd

Pattern Matching / Switch:
Grade B: Good Job!

For Loop (1 to 5):
1 2 3 4 5

While Loop (Countdown):
3 2 1 Blastoff!
```
