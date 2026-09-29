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
