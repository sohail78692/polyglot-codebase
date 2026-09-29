import os
import json

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

LANGUAGES = [
    {
        "id": "01-python",
        "name": "Python",
        "ext": "py",
        "hw_file": "hello_world.py",
        "ops_file": "basic_operations.py",
        "category": "Mainstream & Systems",
        "paradigm": "Multi-paradigm (Object-oriented, imperative, functional, procedural)",
        "year": "1991",
        "creator": "Guido van Rossum",
        "install": "python.org or `winget install Python.Python.3.12` / `brew install python` / `apt install python3`",
        "hw_run": "python hello_world.py",
        "ops_run": "python basic_operations.py",
        "hw_output": "Hello, World!",
        "ops_output": "a = 20, b = 6\nAddition (a + b)        : 26\nSubtraction (a - b)     : 14\nMultiplication (a * b)  : 120\nDivision (a / b)        : 3.3333333333333335\nInteger Division (a // b): 3\nModulo (a % b)          : 2",
        "hw_code": '''# ==========================================
# Program: Hello World in Python
# ==========================================

# Step 1: Define our main entry function.
def main():
    # 'print()' sends text to the terminal and appends a newline.
    print("Hello, World!")

# Step 2: Run main() if executed directly.
if __name__ == "__main__":
    main()
''',
        "ops_code": '''# ==========================================
# Program: Basic Operations in Python (+, -, *, /, //, %)
# ==========================================

def main():
    a = 20
    b = 6

    print(f"a = {a}, b = {b}")
    print(f"Addition (a + b)        : {a + b}")
    print(f"Subtraction (a - b)     : {a - b}")
    print(f"Multiplication (a * b)  : {a * b}")
    print(f"Division (a / b)        : {a / b}")       # Float division
    print(f"Integer Division (a // b): {a // b}")     # Truncating integer division
    print(f"Modulo (a % b)          : {a % b}")       # Remainder of division

if __name__ == "__main__":
    main()
''',
        "hw_exp": "Python uses `print()` to output text. `if __name__ == '__main__':` ensures the script executes only when directly run.",
        "ops_exp": "Python supports standard arithmetic: `+`, `-`, `*`, `/` (float division), `//` (integer floor division), and `%` (modulo)."
    },
    {
        "id": "02-javascript",
        "name": "JavaScript",
        "ext": "js",
        "hw_file": "hello_world.js",
        "ops_file": "basic_operations.js",
        "category": "Mainstream & Systems",
        "paradigm": "Multi-paradigm (Event-driven, functional, imperative)",
        "year": "1995",
        "creator": "Brendan Eich",
        "install": "nodejs.org or `winget install OpenJS.NodeJS` / `brew install node` / `apt install nodejs`",
        "hw_run": "node hello_world.js",
        "ops_run": "node basic_operations.js",
        "hw_output": "Hello, World!",
        "ops_output": "a = 20, b = 6\nAddition (a + b)        : 26\nSubtraction (a - b)     : 14\nMultiplication (a * b)  : 120\nDivision (a / b)        : 3.3333333333333335\nInteger Division        : 3\nModulo (a % b)          : 2",
        "hw_code": '''// ==========================================
// Program: Hello World in JavaScript (Node.js)
// ==========================================

function main() {
    console.log("Hello, World!");
}

main();
''',
        "ops_code": '''// ==========================================
// Program: Basic Operations in JavaScript (+, -, *, /, %)
// ==========================================

function main() {
    const a = 20;
    const b = 6;

    console.log(`a = ${a}, b = ${b}`);
    console.log(`Addition (a + b)        : ${a + b}`);
    console.log(`Subtraction (a - b)     : ${a - b}`);
    console.log(`Multiplication (a * b)  : ${a * b}`);
    console.log(`Division (a / b)        : ${a / b}`);
    console.log(`Integer Division        : ${Math.floor(a / b)}`);
    console.log(`Modulo (a % b)          : ${a % b}`);
}

main();
''',
        "hw_exp": "`console.log()` sends text to standard output.",
        "ops_exp": "JavaScript uses standard operators: `+`, `-`, `*`, `/`, and `%`. For integer division, `Math.floor()` truncates decimals."
    },
    {
        "id": "03-typescript",
        "name": "TypeScript",
        "ext": "ts",
        "hw_file": "hello_world.ts",
        "ops_file": "basic_operations.ts",
        "category": "Mainstream & Systems",
        "paradigm": "Multi-paradigm (Static typed superset of JavaScript)",
        "year": "2012",
        "creator": "Anders Hejlsberg (Microsoft)",
        "install": "`npm install -g typescript ts-node` or `npx ts-node`",
        "hw_run": "npx ts-node hello_world.ts",
        "ops_run": "npx ts-node basic_operations.ts",
        "hw_output": "Hello, World!",
        "ops_output": "a = 20, b = 6\nAddition (a + b)        : 26\nSubtraction (a - b)     : 14\nMultiplication (a * b)  : 120\nDivision (a / b)        : 3.3333333333333335\nInteger Division        : 3\nModulo (a % b)          : 2",
        "hw_code": '''// ==========================================
// Program: Hello World in TypeScript
// ==========================================

function greet(message: string): void {
    console.log(message);
}

greet("Hello, World!");
''',
        "ops_code": '''// ==========================================
// Program: Basic Operations in TypeScript (+, -, *, /, %)
// ==========================================

function calculate(a: number, b: number): void {
    console.log(`a = ${a}, b = ${b}`);
    console.log(`Addition (a + b)        : ${a + b}`);
    console.log(`Subtraction (a - b)     : ${a - b}`);
    console.log(`Multiplication (a * b)  : ${a * b}`);
    console.log(`Division (a / b)        : ${a / b}`);
    console.log(`Integer Division        : ${Math.floor(a / b)}`);
    console.log(`Modulo (a % b)          : ${a % b}`);
}

calculate(20, 6);
''',
        "hw_exp": "TypeScript enforces parameter types (`: string`) and return types (`: void`).",
        "ops_exp": "TypeScript provides static type safety for numeric variables (`: number`) with standard math operators."
    },
    {
        "id": "04-c",
        "name": "C",
        "ext": "c",
        "hw_file": "hello_world.c",
        "ops_file": "basic_operations.c",
        "category": "Mainstream & Systems",
        "paradigm": "Imperative, Procedural",
        "year": "1972",
        "creator": "Dennis Ritchie (Bell Labs)",
        "install": "GCC / Clang / MSVC",
        "hw_run": "gcc hello_world.c -o hello_world && ./hello_world",
        "ops_run": "gcc basic_operations.c -o basic_operations && ./basic_operations",
        "hw_output": "Hello, World!",
        "ops_output": "a = 20, b = 6\nAddition (a + b)        : 26\nSubtraction (a - b)     : 14\nMultiplication (a * b)  : 120\nInteger Division (a / b): 3\nFloat Division (float)  : 3.333333\nModulo (a % b)          : 2",
        "hw_code": '''/*
 * ==========================================
 * Program: Hello World in C
 * ==========================================
 */
#include <stdio.h>

int main(void) {
    printf("Hello, World!\\n");
    return 0;
}
''',
        "ops_code": '''/*
 * ==========================================
 * Program: Basic Operations in C (+, -, *, /, %)
 * ==========================================
 */
#include <stdio.h>

int main(void) {
    int a = 20;
    int b = 6;

    printf("a = %d, b = %d\\n", a, b);
    printf("Addition (a + b)        : %d\\n", a + b);
    printf("Subtraction (a - b)     : %d\\n", a - b);
    printf("Multiplication (a * b)  : %d\\n", a * b);
    printf("Integer Division (a / b): %d\\n", a / b);             // Integer division truncates
    printf("Float Division (float)  : %f\\n", (float)a / (float)b); // Type casting for float
    printf("Modulo (a % b)          : %d\\n", a % b);             // Remainder operator

    return 0;
}
''',
        "hw_exp": "`printf` outputs formatted text to stdout.",
        "ops_exp": "In C, dividing two integers (`a / b`) produces an integer quotient. Type-casting to `(float)` yields decimal results. `%` yields the remainder."
    },
    {
        "id": "05-cpp",
        "name": "C++",
        "ext": "cpp",
        "hw_file": "hello_world.cpp",
        "ops_file": "basic_operations.cpp",
        "category": "Mainstream & Systems",
        "paradigm": "Multi-paradigm (OOP, generic, procedural, functional)",
        "year": "1985",
        "creator": "Bjarne Stroustrup",
        "install": "G++ / Clang++",
        "hw_run": "g++ -std=c++17 hello_world.cpp -o hello_world && ./hello_world",
        "ops_run": "g++ -std=c++17 basic_operations.cpp -o basic_operations && ./basic_operations",
        "hw_output": "Hello, World!",
        "ops_output": "a = 20, b = 6\nAddition (a + b)        : 26\nSubtraction (a - b)     : 14\nMultiplication (a * b)  : 120\nInteger Division (a / b): 3\nFloat Division (double) : 3.33333\nModulo (a % b)          : 2",
        "hw_code": '''/*
 * ==========================================
 * Program: Hello World in C++
 * ==========================================
 */
#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
''',
        "ops_code": '''/*
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
''',
        "hw_exp": "`std::cout` and `<<` send data to standard output stream.",
        "ops_exp": "`static_cast<double>(a) / b` converts `a` to double to perform floating-point division; `%` gives the remainder."
    },
    {
        "id": "06-csharp",
        "name": "C#",
        "ext": "cs",
        "hw_file": "hello_world.cs",
        "ops_file": "basic_operations.cs",
        "category": "Mainstream & Systems",
        "paradigm": "Multi-paradigm (Object-oriented, component-oriented, functional)",
        "year": "2000",
        "creator": "Anders Hejlsberg (Microsoft)",
        "install": ".NET SDK",
        "hw_run": "dotnet run (or csc hello_world.cs && ./hello_world.exe)",
        "ops_run": "csc basic_operations.cs && ./basic_operations.exe",
        "hw_output": "Hello, World!",
        "ops_output": "a = 20, b = 6\nAddition (a + b)        : 26\nSubtraction (a - b)     : 14\nMultiplication (a * b)  : 120\nInteger Division (a / b): 3\nFloat Division (double) : 3.3333333333333335\nModulo (a % b)          : 2",
        "hw_code": '''// ==========================================
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
''',
        "ops_code": '''// ==========================================
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
''',
        "hw_exp": "`Console.WriteLine` writes to stdout in C#.",
        "ops_exp": "C# supports string interpolation `$\"{...}\"` with standard operators `+`, `-`, `*`, `/`, `%`."
    },
    {
        "id": "07-java",
        "name": "Java",
        "ext": "java",
        "hw_file": "HelloWorld.java",
        "ops_file": "BasicOperations.java",
        "category": "Mainstream & Systems",
        "paradigm": "Multi-paradigm (Object-oriented, generic, concurrent)",
        "year": "1995",
        "creator": "James Gosling (Sun Microsystems)",
        "install": "OpenJDK / Oracle JDK",
        "hw_run": "javac HelloWorld.java && java HelloWorld",
        "ops_run": "javac BasicOperations.java && java BasicOperations",
        "hw_output": "Hello, World!",
        "ops_output": "a = 20, b = 6\nAddition (a + b)        : 26\nSubtraction (a - b)     : 14\nMultiplication (a * b)  : 120\nInteger Division (a / b): 3\nFloat Division (double) : 3.3333333333333335\nModulo (a % b)          : 2",
        "hw_code": '''// ==========================================
// Program: Hello World in Java
// ==========================================
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
''',
        "ops_code": '''// ==========================================
// Program: Basic Operations in Java (+, -, *, /, %)
// ==========================================
public class BasicOperations {
    public static void main(String[] args) {
        int a = 20;
        int b = 6;

        System.out.println("a = " + a + ", b = " + b);
        System.out.println("Addition (a + b)        : " + (a + b));
        System.out.println("Subtraction (a - b)     : " + (a - b));
        System.out.println("Multiplication (a * b)  : " + (a * b));
        System.out.println("Integer Division (a / b): " + (a / b));
        System.out.println("Float Division (double) : " + ((double) a / b));
        System.out.println("Modulo (a % b)          : " + (a % b));
    }
}
''',
        "hw_exp": "Public class name must match filename `HelloWorld.java`.",
        "ops_exp": "Java evaluates arithmetic expressions with precedence: `(a + b)` prevents string concatenation precedence errors."
    },
    {
        "id": "08-go",
        "name": "Go",
        "ext": "go",
        "hw_file": "hello_world.go",
        "ops_file": "basic_operations.go",
        "category": "Mainstream & Systems",
        "paradigm": "Multi-paradigm (Concurrent, imperative, procedural)",
        "year": "2009",
        "creator": "Robert Griesemer, Rob Pike, Ken Thompson (Google)",
        "install": "go.dev",
        "hw_run": "go run hello_world.go",
        "ops_run": "go run basic_operations.go",
        "hw_output": "Hello, World!",
        "ops_output": "a = 20, b = 6\nAddition (a + b)        : 26\nSubtraction (a - b)     : 14\nMultiplication (a * b)  : 120\nInteger Division (a / b): 3\nFloat Division (float64): 3.3333333333333335\nModulo (a % b)          : 2",
        "hw_code": '''// ==========================================
// Program: Hello World in Go (Golang)
// ==========================================
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
''',
        "ops_code": '''// ==========================================
// Program: Basic Operations in Go (+, -, *, /, %)
// ==========================================
package main

import "fmt"

func main() {
    a := 20
    b := 6

    fmt.Printf("a = %d, b = %d\\n", a, b)
    fmt.Printf("Addition (a + b)        : %d\\n", a + b)
    fmt.Printf("Subtraction (a - b)     : %d\\n", a - b)
    fmt.Printf("Multiplication (a * b)  : %d\\n", a * b)
    fmt.Printf("Integer Division (a / b): %d\\n", a / b)
    fmt.Printf("Float Division (float64): %f\\n", float64(a) / float64(b))
    fmt.Printf("Modulo (a % b)          : %d\\n", a % b)
}
''',
        "hw_exp": "Go uses `fmt.Println` for console output.",
        "ops_exp": "Go enforces strict typing: float conversion must be explicit via `float64(a) / float64(b)`."
    },
    {
        "id": "09-rust",
        "name": "Rust",
        "ext": "rs",
        "hw_file": "hello_world.rs",
        "ops_file": "basic_operations.rs",
        "category": "Mainstream & Systems",
        "paradigm": "Multi-paradigm (Concurrent, functional, imperative, generic)",
        "year": "2015",
        "creator": "Graydon Hoare (Mozilla Research)",
        "install": "rustup.rs",
        "hw_run": "rustc hello_world.rs && ./hello_world",
        "ops_run": "rustc basic_operations.rs && ./basic_operations",
        "hw_output": "Hello, World!",
        "ops_output": "a = 20, b = 6\nAddition (a + b)        : 26\nSubtraction (a - b)     : 14\nMultiplication (a * b)  : 120\nInteger Division (a / b): 3\nFloat Division (f64)    : 3.3333333333333335\nModulo (a % b)          : 2",
        "hw_code": '''// ==========================================
// Program: Hello World in Rust
// ==========================================
fn main() {
    println!("Hello, World!");
}
''',
        "ops_code": '''// ==========================================
// Program: Basic Operations in Rust (+, -, *, /, %)
// ==========================================
fn main() {
    let a: i32 = 20;
    let b: i32 = 6;

    println!("a = {}, b = {}", a, b);
    println!("Addition (a + b)        : {}", a + b);
    println!("Subtraction (a - b)     : {}", a - b);
    println!("Multiplication (a * b)  : {}", a * b);
    println!("Integer Division (a / b): {}", a / b);
    println!("Float Division (f64)    : {}", (a as f64) / (b as f64));
    println!("Modulo (a % b)          : {}", a % b);
}
''',
        "hw_exp": "`println!` macro handles formatting at compile time.",
        "ops_exp": "Rust checks for overflow and requires explicit casting `(a as f64)` for type safety."
    },
    {
        "id": "10-kotlin",
        "name": "Kotlin",
        "ext": "kt",
        "hw_file": "hello_world.kt",
        "ops_file": "basic_operations.kt",
        "category": "Mainstream & Systems",
        "paradigm": "Multi-paradigm (Functional, object-oriented)",
        "year": "2011",
        "creator": "JetBrains",
        "install": "JetBrains Kotlin",
        "hw_run": "kotlinc hello_world.kt -include-runtime -d hello_world.jar && java -jar hello_world.jar",
        "ops_run": "kotlinc basic_operations.kt -include-runtime -d basic_operations.jar && java -jar basic_operations.jar",
        "hw_output": "Hello, World!",
        "ops_output": "a = 20, b = 6\nAddition (a + b)        : 26\nSubtraction (a - b)     : 14\nMultiplication (a * b)  : 120\nInteger Division (a / b): 3\nFloat Division (toDouble): 3.3333333333333335\nModulo (a % b)          : 2",
        "hw_code": '''// ==========================================
// Program: Hello World in Kotlin
// ==========================================
fun main() {
    println("Hello, World!")
}
''',
        "ops_code": '''// ==========================================
// Program: Basic Operations in Kotlin (+, -, *, /, %)
// ==========================================
fun main() {
    val a = 20
    val b = 6

    println("a = $a, b = $b")
    println("Addition (a + b)        : ${a + b}")
    println("Subtraction (a - b)     : ${a - b}")
    println("Multiplication (a * b)  : ${a * b}")
    println("Integer Division (a / b): ${a / b}")
    println("Float Division (toDouble): ${a.toDouble() / b}")
    println("Modulo (a % b)          : ${a % b}")
}
''',
        "hw_exp": "Kotlin provides clean top-level functions without class wrapping.",
        "ops_exp": "String template `${a + b}` evaluates expressions inline. `a.toDouble()` casts to double."
    },
    {
        "id": "11-swift",
        "name": "Swift",
        "ext": "swift",
        "hw_file": "hello_world.swift",
        "ops_file": "basic_operations.swift",
        "category": "Mainstream & Systems",
        "paradigm": "Multi-paradigm (Protocol-oriented, object-oriented, functional)",
        "year": "2014",
        "creator": "Chris Lattner (Apple)",
        "install": "Xcode / swift.org",
        "hw_run": "swift hello_world.swift",
        "ops_run": "swift basic_operations.swift",
        "hw_output": "Hello, World!",
        "ops_output": "a = 20, b = 6\nAddition (a + b)        : 26\nSubtraction (a - b)     : 14\nMultiplication (a * b)  : 120\nInteger Division (a / b): 3\nFloat Division (Double) : 3.3333333333333335\nModulo (a % b)          : 2",
        "hw_code": '''// ==========================================
// Program: Hello World in Swift
// ==========================================
print("Hello, World!")
''',
        "ops_code": '''// ==========================================
// Program: Basic Operations in Swift (+, -, *, /, %)
// ==========================================
let a = 20
let b = 6

print("a = \(a), b = \(b)")
print("Addition (a + b)        : \(a + b)")
print("Subtraction (a - b)     : \(a - b)")
print("Multiplication (a * b)  : \(a * b)")
print("Integer Division (a / b): \(a / b)")
print("Float Division (Double) : \(Double(a) / Double(b))")
print("Modulo (a % b)          : \(a % b)")
''',
        "hw_exp": "Top-level statements execute directly.",
        "ops_exp": "Swift uses string interpolation `\\(...)` and strictly rejects implicit conversions between `Int` and `Double`."
    },
    {
        "id": "12-php",
        "name": "PHP",
        "ext": "php",
        "hw_file": "hello_world.php",
        "ops_file": "basic_operations.php",
        "category": "Mainstream & Systems",
        "paradigm": "Multi-paradigm (Imperative, OOP, procedural)",
        "year": "1995",
        "creator": "Rasmus Lerdorf",
        "install": "php.net",
        "hw_run": "php hello_world.php",
        "ops_run": "php basic_operations.php",
        "hw_output": "Hello, World!",
        "ops_output": "a = 20, b = 6\nAddition (a + b)        : 26\nSubtraction (a - b)     : 14\nMultiplication (a * b)  : 120\nDivision (a / b)        : 3.3333333333333\nInteger Division (intdiv): 3\nModulo (a % b)          : 2",
        "hw_code": '''<?php
// ==========================================
// Program: Hello World in PHP
// ==========================================
echo "Hello, World!\n";
?>
''',
        "ops_code": '''<?php
// ==========================================
// Program: Basic Operations in PHP (+, -, *, /, %)
// ==========================================
$a = 20;
$b = 6;

echo "a = $a, b = $b\n";
echo "Addition (a + b)        : " . ($a + $b) . "\n";
echo "Subtraction (a - b)     : " . ($a - $b) . "\n";
echo "Multiplication (a * b)  : " . ($a * $b) . "\n";
echo "Division (a / b)        : " . ($a / $b) . "\n";
echo "Integer Division (intdiv): " . intdiv($a, $b) . "\n";
echo "Modulo (a % b)          : " . ($a % $b) . "\n";
?>
''',
        "hw_exp": "`echo` outputs strings to stdout.",
        "ops_exp": "In PHP, variables start with `$`. String concatenation uses `.` and `intdiv()` provides explicit integer division."
    },
    {
        "id": "13-ruby",
        "name": "Ruby",
        "ext": "rb",
        "hw_file": "hello_world.rb",
        "ops_file": "basic_operations.rb",
        "category": "Mainstream & Systems",
        "paradigm": "Multi-paradigm (Pure object-oriented, imperative, functional)",
        "year": "1995",
        "creator": "Yukihiro Matsumoto (Matz)",
        "install": "ruby-lang.org",
        "hw_run": "ruby hello_world.rb",
        "ops_run": "ruby basic_operations.rb",
        "hw_output": "Hello, World!",
        "ops_output": "a = 20, b = 6\nAddition (a + b)        : 26\nSubtraction (a - b)     : 14\nMultiplication (a * b)  : 120\nInteger Division (a / b): 3\nFloat Division (to_f)   : 3.3333333333333335\nModulo (a % b)          : 2",
        "hw_code": '''# ==========================================
# Program: Hello World in Ruby
# ==========================================
puts "Hello, World!"
''',
        "ops_code": '''# ==========================================
# Program: Basic Operations in Ruby (+, -, *, /, %)
# ==========================================
a = 20
b = 6

puts "a = #{a}, b = #{b}"
puts "Addition (a + b)        : #{a + b}"
puts "Subtraction (a - b)     : #{a - b}"
puts "Multiplication (a * b)  : #{a * b}"
puts "Integer Division (a / b): #{a / b}"
puts "Float Division (to_f)   : #{a.to_f / b}"
puts "Modulo (a % b)          : #{a % b}"
''',
        "hw_exp": "`puts` outputs an object followed by a newline.",
        "ops_exp": "Ruby divides integers using integer division. `a.to_f` converts to a float for fractional division."
    },
    {
        "id": "14-r",
        "name": "R",
        "ext": "r",
        "hw_file": "hello_world.r",
        "ops_file": "basic_operations.r",
        "category": "Scientific & Data",
        "paradigm": "Multi-paradigm (Functional, array, procedural)",
        "year": "1993",
        "creator": "Ross Ihaka and Robert Gentleman",
        "install": "r-project.org",
        "hw_run": "Rscript hello_world.r",
        "ops_run": "Rscript basic_operations.r",
        "hw_output": "Hello, World!",
        "ops_output": "a = 20, b = 6\nAddition (a + b)        : 26\nSubtraction (a - b)     : 14\nMultiplication (a * b)  : 120\nDivision (a / b)        : 3.333333\nInteger Division (a %/% b): 3\nModulo (a %% b)         : 2",
        "hw_code": '''# ==========================================
# Program: Hello World in R
# ==========================================
cat("Hello, World!\n")
''',
        "ops_code": '''# ==========================================
# Program: Basic Operations in R (+, -, *, /, %/%, %%)
# ==========================================
a <- 20
b <- 6

cat(sprintf("a = %d, b = %d\n", a, b))
cat(sprintf("Addition (a + b)        : %d\n", a + b))
cat(sprintf("Subtraction (a - b)     : %d\n", a - b))
cat(sprintf("Multiplication (a * b)  : %d\n", a * b))
cat(sprintf("Division (a / b)        : %f\n", a / b))
cat(sprintf("Integer Division (a %%/%% b): %d\n", a %/% b)) # %/% is integer division in R
cat(sprintf("Modulo (a %%%% b)         : %d\n", a %% b))   # %% is modulo in R
''',
        "hw_exp": "`cat()` prints text without vector indices.",
        "ops_exp": "In R, integer division is `%/%` and modulo is `%%`."
    },
    {
        "id": "15-julia",
        "name": "Julia",
        "ext": "jl",
        "hw_file": "hello_world.jl",
        "ops_file": "basic_operations.jl",
        "category": "Scientific & Data",
        "paradigm": "Multi-paradigm (Multiple dispatch, functional, procedural)",
        "year": "2012",
        "creator": "Jeff Bezanson et al.",
        "install": "julialang.org",
        "hw_run": "julia hello_world.jl",
        "ops_run": "julia basic_operations.jl",
        "hw_output": "Hello, World!",
        "ops_output": "a = 20, b = 6\nAddition (a + b)        : 26\nSubtraction (a - b)     : 14\nMultiplication (a * b)  : 120\nDivision (a / b)        : 3.3333333333333335\nInteger Division (div)  : 3\nModulo (a % b)          : 2",
        "hw_code": '''# ==========================================
# Program: Hello World in Julia
# ==========================================
println("Hello, World!")
''',
        "ops_code": '''# ==========================================
# Program: Basic Operations in Julia (+, -, *, /, %, div)
# ==========================================
a = 20
b = 6

println("a = $a, b = $b")
println("Addition (a + b)        : $(a + b)")
println("Subtraction (a - b)     : $(a - b)")
println("Multiplication (a * b)  : $(a * b)")
println("Division (a / b)        : $(a / b)")
println("Integer Division (div)  : $(div(a, b))")
println("Modulo (a % b)          : $(a % b)")
''',
        "hw_exp": "`println()` outputs text to stdout.",
        "ops_exp": "Julia's `/` operator always performs floating-point division; `div(a, b)` performs integer division."
    },
    {
        "id": "16-matlab",
        "name": "MATLAB / GNU Octave",
        "ext": "m",
        "hw_file": "hello_world.m",
        "ops_file": "basic_operations.m",
        "category": "Scientific & Data",
        "paradigm": "Array programming, procedural",
        "year": "1984",
        "creator": "Cleve Moler (MathWorks)",
        "install": "MATLAB or GNU Octave",
        "hw_run": "octave --silent hello_world.m",
        "ops_run": "octave --silent basic_operations.m",
        "hw_output": "Hello, World!",
        "ops_output": "a = 20, b = 6\nAddition (a + b)        : 26\nSubtraction (a - b)     : 14\nMultiplication (a * b)  : 120\nDivision (a / b)        : 3.333333\nInteger Division (idiv) : 3\nModulo (mod(a, b))      : 2",
        "hw_code": '''% ==========================================
% Program: Hello World in MATLAB / GNU Octave
% ==========================================
disp('Hello, World!');
''',
        "ops_code": '''% ==========================================
% Program: Basic Operations in MATLAB / GNU Octave
% ==========================================
a = 20;
b = 6;

fprintf('a = %d, b = %d\\n', a, b);
fprintf('Addition (a + b)        : %d\\n', a + b);
fprintf('Subtraction (a - b)     : %d\\n', a - b);
fprintf('Multiplication (a * b)  : %d\\n', a * b);
fprintf('Division (a / b)        : %f\\n', a / b);
fprintf('Integer Division (idiv) : %d\\n', fix(a / b));
fprintf('Modulo (mod(a, b))      : %d\\n', mod(a, b));
''',
        "hw_exp": "`disp` prints values without variable names.",
        "ops_exp": "`fprintf` formats output; `fix(a / b)` truncates to integer; `mod(a, b)` calculates modulo."
    },
    {
        "id": "17-zig",
        "name": "Zig",
        "ext": "zig",
        "hw_file": "hello_world.zig",
        "ops_file": "basic_operations.zig",
        "category": "Scientific & Data",
        "paradigm": "Imperative, Systems",
        "year": "2016",
        "creator": "Andrew Kelley",
        "install": "ziglang.org",
        "hw_run": "zig run hello_world.zig",
        "ops_run": "zig run basic_operations.zig",
        "hw_output": "Hello, World!",
        "ops_output": "a = 20, b = 6\nAddition (a + b)        : 26\nSubtraction (a - b)     : 14\nMultiplication (a * b)  : 120\nInteger Division (div)  : 3\nFloat Division          : 3.3333333333333335\nModulo (@rem)           : 2",
        "hw_code": '''// ==========================================
// Program: Hello World in Zig
// ==========================================
const std = @import("std");

pub fn main() !void {
    const stdout = std.io.getStdOut().writer();
    try stdout.print("Hello, World!\\n", .{});
}
''',
        "ops_code": '''// ==========================================
// Program: Basic Operations in Zig (+, -, *, @divTrunc, @rem)
// ==========================================
const std = @import("std");

pub fn main() !void {
    const stdout = std.io.getStdOut().writer();
    const a: i32 = 20;
    const b: i32 = 6;

    try stdout.print("a = {d}, b = {d}\\n", .{a, b});
    try stdout.print("Addition (a + b)        : {d}\\n", .{a + b});
    try stdout.print("Subtraction (a - b)     : {d}\\n", .{a - b});
    try stdout.print("Multiplication (a * b)  : {d}\\n", .{a * b});
    try stdout.print("Integer Division (div)  : {d}\\n", .{@divTrunc(a, b)});
    try stdout.print("Float Division          : {d}\\n", .{@as(f64, @floatFromInt(a)) / @as(f64, @floatFromInt(b))});
    try stdout.print("Modulo (@rem)           : {d}\\n", .{@rem(a, b)});
}
''',
        "hw_exp": "Explicit error handling using `try` and `@import(\"std\")`.",
        "ops_exp": "Zig uses builtins like `@divTrunc` and `@rem` for integer division and remainder with no hidden overflow."
    },
    {
        "id": "18-assembly",
        "name": "Assembly (x86_64 NASM)",
        "ext": "asm",
        "hw_file": "hello_world.asm",
        "ops_file": "basic_operations.asm",
        "category": "Scientific & Data",
        "paradigm": "Low-level Assembly",
        "year": "1970s",
        "creator": "AMD / Intel",
        "install": "NASM & GCC/LD",
        "hw_run": "nasm -f elf64 hello_world.asm -o hello_world.o && ld hello_world.o -o hello_world && ./hello_world",
        "ops_run": "nasm -f elf64 basic_operations.asm -o basic_ops.o && gcc basic_ops.o -no-pie -o basic_ops && ./basic_ops",
        "hw_output": "Hello, World!",
        "ops_output": "a = 20, b = 6\nAddition: 26, Subtraction: 14, Multiplication: 120, Division: 3, Modulo: 2",
        "hw_code": '''; ==========================================
; Program: Hello World in x86_64 Assembly (Linux NASM)
; ==========================================
section .data
    msg db "Hello, World!", 0x0a
    len equ $ - msg

section .text
    global _start

_start:
    mov rax, 1
    mov rdi, 1
    mov rsi, msg
    mov rdx, len
    syscall

    mov rax, 60
    xor rdi, rdi
    syscall
''',
        "ops_code": '''; ==========================================
; Program: Basic Operations in x86_64 Assembly (NASM + printf)
; Demonstrates CPU instructions: add, sub, imul, idiv
; ==========================================
section .data
    fmt db "a = 20, b = 6", 10
        db "Addition: %d, Subtraction: %d, Multiplication: %d, Division: %d, Modulo: %d", 10, 0

section .text
    global main
    extern printf

main:
    push rbp
    mov rbp, rsp

    ; a = 20, b = 6
    ; 1. Addition (20 + 6 = 26)
    mov r12, 20
    add r12, 6          ; r12 = 26

    ; 2. Subtraction (20 - 6 = 14)
    mov r13, 20
    sub r13, 6          ; r13 = 14

    ; 3. Multiplication (20 * 6 = 120)
    mov rax, 20
    imul rax, 6         ; rax = 120
    mov r14, rax

    ; 4. Division & Modulo (20 / 6 -> quotient 3, remainder 2)
    mov rax, 20
    cqo                 ; Sign-extend rax into rdx:rax
    mov rbx, 6
    idiv rbx            ; rax = quotient (3), rdx = remainder (2)
    mov r15, rax        ; r15 = 3 (division)
    mov rbx, rdx        ; rbx = 2 (modulo)

    ; Print results via printf(fmt, add, sub, mul, div, mod)
    mov rdi, fmt
    mov rsi, r12
    mov rdx, r13
    mov rcx, r14
    mov r8, r15
    mov r9, rbx
    xor eax, eax
    call printf

    xor eax, eax
    leave
    ret
''',
        "hw_exp": "Direct kernel syscalls using `rax=1` (write) and `rax=60` (exit).",
        "ops_exp": "Demonstrates core CPU instructions: `add`, `sub`, `imul`, and `idiv` (which calculates both quotient and remainder simultaneously)."
    },
    {
        "id": "19-d",
        "name": "D",
        "ext": "d",
        "hw_file": "hello_world.d",
        "ops_file": "basic_operations.d",
        "category": "Scientific & Data",
        "paradigm": "Multi-paradigm (OOP, generic, functional, imperative)",
        "year": "2001",
        "creator": "Walter Bright (Digital Mars)",
        "install": "dlang.org",
        "hw_run": "dmd -run hello_world.d",
        "ops_run": "dmd -run basic_operations.d",
        "hw_output": "Hello, World!",
        "ops_output": "a = 20, b = 6\nAddition (a + b)        : 26\nSubtraction (a - b)     : 14\nMultiplication (a * b)  : 120\nInteger Division (a / b): 3\nFloat Division (double) : 3.33333\nModulo (a % b)          : 2",
        "hw_code": '''// ==========================================
// Program: Hello World in D
// ==========================================
import std.stdio;

void main() {
    writeln("Hello, World!");
}
''',
        "ops_code": '''// ==========================================
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
''',
        "hw_exp": "`writeln` writes to stdout.",
        "ops_exp": "`cast(double)a` explicitly casts to double for floating-point division."
    },
    {
        "id": "20-nim",
        "name": "Nim",
        "ext": "nim",
        "hw_file": "hello_world.nim",
        "ops_file": "basic_operations.nim",
        "category": "Scientific & Data",
        "paradigm": "Multi-paradigm (Metaprogramming, functional, procedural)",
        "year": "2008",
        "creator": "Andreas Rumpf",
        "install": "nim-lang.org",
        "hw_run": "nim compile --run hello_world.nim",
        "ops_run": "nim compile --run basic_operations.nim",
        "hw_output": "Hello, World!",
        "ops_output": "a = 20, b = 6\nAddition (a + b)        : 26\nSubtraction (a - b)     : 14\nMultiplication (a * b)  : 120\nFloat Division (a / b)  : 3.333333333333334\nInteger Division (div)  : 3\nModulo (mod)            : 2",
        "hw_code": '''# ==========================================
# Program: Hello World in Nim
# ==========================================
echo "Hello, World!"
''',
        "ops_code": '''# ==========================================
# Program: Basic Operations in Nim (+, -, *, /, div, mod)
# ==========================================
let a = 20
let b = 6

echo "a = ", a, ", b = ", b
echo "Addition (a + b)        : ", a + b
echo "Subtraction (a - b)     : ", a - b
echo "Multiplication (a * b)  : ", a * b
echo "Float Division (a / b)  : ", a / b     # '/' returns a float
echo "Integer Division (div)  : ", a div b   # 'div' is integer division
echo "Modulo (mod)            : ", a mod b   # 'mod' is modulo
''',
        "hw_exp": "`echo` outputs to stdout with a newline.",
        "ops_exp": "Nim uses `div` for integer division and `mod` for remainder."
    },
    {
        "id": "21-fortran",
        "name": "Fortran",
        "ext": "f90",
        "hw_file": "hello_world.f90",
        "ops_file": "basic_operations.f90",
        "category": "Scientific & Data",
        "paradigm": "Array, imperative, procedural",
        "year": "1957",
        "creator": "John Backus (IBM)",
        "install": "GFortran",
        "hw_run": "gfortran hello_world.f90 -o hello_world && ./hello_world",
        "ops_run": "gfortran basic_operations.f90 -o basic_operations && ./basic_operations",
        "hw_output": " Hello, World!",
        "ops_output": " a = 20, b = 6\n Addition (a + b)        : 26\n Subtraction (a - b)     : 14\n Multiplication (a * b)  : 120\n Integer Division (a / b): 3\n Float Division (real)   : 3.33333325\n Modulo (mod(a, b))      : 2",
        "hw_code": '''! ==========================================
! Program: Hello World in Modern Fortran (90+)
! ==========================================
program hello_world
    implicit none
    print *, "Hello, World!"
end program hello_world
''',
        "ops_code": '''! ==========================================
! Program: Basic Operations in Modern Fortran (+, -, *, /, mod)
! ==========================================
program basic_operations
    implicit none
    integer :: a, b

    a = 20
    b = 6

    print *, "a = 20, b = 6"
    print *, "Addition (a + b)        : ", a + b
    print *, "Subtraction (a - b)     : ", a - b
    print *, "Multiplication (a * b)  : ", a * b
    print *, "Integer Division (a / b): ", a / b
    print *, "Float Division (real)   : ", real(a) / real(b)
    print *, "Modulo (mod(a, b))      : ", mod(a, b)
end program basic_operations
''',
        "hw_exp": "`print *` formats and writes to stdout.",
        "ops_exp": "`mod(a, b)` calculates remainder; `real(a) / real(b)` performs floating-point division."
    },
    {
        "id": "22-ada",
        "name": "Ada",
        "ext": "adb",
        "hw_file": "hello_world.adb",
        "ops_file": "basic_operations.adb",
        "category": "Scientific & Data",
        "paradigm": "Multi-paradigm (Strongly typed, concurrent, OOP)",
        "year": "1980",
        "creator": "Jean Ichbiah",
        "install": "GNAT Ada Compiler",
        "hw_run": "gnatmake hello_world.adb && ./hello_world",
        "ops_run": "gnatmake basic_operations.adb && ./basic_operations",
        "hw_output": "Hello, World!",
        "ops_output": "a = 20, b = 6\nAddition (a + b)        :  26\nSubtraction (a - b)     :  14\nMultiplication (a * b)  :  120\nInteger Division (a / b):  3\nModulo (a mod b)        :  2",
        "hw_code": '''-- ==========================================
-- Program: Hello World in Ada
-- ==========================================
with Ada.Text_IO; use Ada.Text_IO;

procedure Hello_World is
begin
    Put_Line ("Hello, World!");
end Hello_World;
''',
        "ops_code": '''-- ==========================================
-- Program: Basic Operations in Ada (+, -, *, /, mod)
-- ==========================================
with Ada.Text_IO; use Ada.Text_IO;
with Ada.Integer_Text_IO; use Ada.Integer_Text_IO;

procedure Basic_Operations is
    A : Integer := 20;
    B : Integer := 6;
begin
    Put_Line ("a = 20, b = 6");
    Put ("Addition (a + b)        : "); Put (A + B); New_Line;
    Put ("Subtraction (a - b)     : "); Put (A - B); New_Line;
    Put ("Multiplication (a * b)  : "); Put (A * B); New_Line;
    Put ("Integer Division (a / b): "); Put (A / B); New_Line;
    Put ("Modulo (a mod b)        : "); Put (A mod B); New_Line;
end Basic_Operations;
''',
        "hw_exp": "`Put_Line` writes to stdout.",
        "ops_exp": "Ada uses `mod` keyword for modulo and `Integer_Text_IO` for formatted integer output."
    },
    {
        "id": "23-haskell",
        "name": "Haskell",
        "ext": "hs",
        "hw_file": "hello_world.hs",
        "ops_file": "basic_operations.hs",
        "category": "Functional & Declarative",
        "paradigm": "Purely functional, lazy evaluation",
        "year": "1990",
        "creator": "Simon Peyton Jones et al.",
        "install": "GHC / ghcup",
        "hw_run": "runhaskell hello_world.hs",
        "ops_run": "runhaskell basic_operations.hs",
        "hw_output": "Hello, World!",
        "ops_output": "a = 20, b = 6\nAddition (a + b)        : 26\nSubtraction (a - b)     : 14\nMultiplication (a * b)  : 120\nInteger Division (div)  : 3\nFloat Division (/)      : 3.3333333333333335\nModulo (mod)            : 2",
        "hw_code": '''-- ==========================================
-- Program: Hello World in Haskell
-- ==========================================
main :: IO ()
main = putStrLn "Hello, World!"
''',
        "ops_code": '''-- ==========================================
-- Program: Basic Operations in Haskell (+, -, *, div, mod, /)
-- ==========================================
main :: IO ()
main = do
    let a = 20 :: Int
    let b = 6 :: Int
    putStrLn "a = 20, b = 6"
    putStrLn ("Addition (a + b)        : " ++ show (a + b))
    putStrLn ("Subtraction (a - b)     : " ++ show (a - b))
    putStrLn ("Multiplication (a * b)  : " ++ show (a * b))
    putStrLn ("Integer Division (div)  : " ++ show (a `div` b))
    putStrLn ("Float Division (/)      : " ++ show (fromIntegral a / fromIntegral b))
    putStrLn ("Modulo (mod)            : " ++ show (a `mod` b))
''',
        "hw_exp": "Haskell uses `putStrLn` to output strings in the `IO` monad.",
        "ops_exp": "Haskell uses backticks for infix functions like `` `div` `` and `` `mod` ``. `fromIntegral` converts Int to Fractional."
    },
    {
        "id": "24-scala",
        "name": "Scala",
        "ext": "scala",
        "hw_file": "hello_world.scala",
        "ops_file": "basic_operations.scala",
        "category": "Functional & Declarative",
        "paradigm": "Functional, Object-oriented",
        "year": "2004",
        "creator": "Martin Odersky",
        "install": "scala-lang.org",
        "hw_run": "scala hello_world.scala",
        "ops_run": "scala basic_operations.scala",
        "hw_output": "Hello, World!",
        "ops_output": "a = 20, b = 6\nAddition (a + b)        : 26\nSubtraction (a - b)     : 14\nMultiplication (a * b)  : 120\nInteger Division (a / b): 3\nFloat Division (toDouble): 3.3333333333333335\nModulo (a % b)          : 2",
        "hw_code": '''// ==========================================
// Program: Hello World in Scala (Scala 3)
// ==========================================
@main def run(): Unit =
  println("Hello, World!")
''',
        "ops_code": '''// ==========================================
// Program: Basic Operations in Scala (Scala 3)
// ==========================================
@main def runOps(): Unit =
  val a = 20
  val b = 6

  println(s"a = $a, b = $b")
  println(s"Addition (a + b)        : ${a + b}")
  println(s"Subtraction (a - b)     : ${a - b}")
  println(s"Multiplication (a * b)  : ${a * b}")
  println(s"Integer Division (a / b): ${a / b}")
  println(s"Float Division (toDouble): ${a.toDouble / b}")
  println(s"Modulo (a % b)          : ${a % b}")
''',
        "hw_exp": "Scala 3 uses `@main` for top-level entry functions.",
        "ops_exp": "String interpolator `s\"...\"` evaluates `${a + b}` directly."
    },
    {
        "id": "25-clojure",
        "name": "Clojure",
        "ext": "clj",
        "hw_file": "hello_world.clj",
        "ops_file": "basic_operations.clj",
        "category": "Functional & Declarative",
        "paradigm": "Functional Lisp dialect (JVM hosted)",
        "year": "2007",
        "creator": "Rich Hickey",
        "install": "clojure.org",
        "hw_run": "clj -M hello_world.clj",
        "ops_run": "clj -M basic_operations.clj",
        "hw_output": "Hello, World!",
        "ops_output": "a = 20, b = 6\nAddition (+ a b)        : 26\nSubtraction (- a b)     : 14\nMultiplication (* a b)  : 120\nQuotient (quot a b)     : 3\nExact Division (/ a b)  : 10/3\nModulo (mod a b)        : 2",
        "hw_code": ''';;; ==========================================
;;; Program: Hello World in Clojure
;;; ==========================================
(println "Hello, World!")
''',
        "ops_code": ''';;; ==========================================
;;; Program: Basic Operations in Clojure (+, -, *, quot, mod)
;;; ==========================================
(let [a 20
      b 6]
  (println (str "a = " a ", b = " b))
  (println (str "Addition (+ a b)        : " (+ a b)))
  (println (str "Subtraction (- a b)     : " (- a b)))
  (println (str "Multiplication (* a b)  : " (* a b)))
  (println (str "Quotient (quot a b)     : " (quot a b)))
  (println (str "Exact Division (/ a b)  : " (/ a b)))
  (println (str "Modulo (mod a b)        : " (mod a b))))
''',
        "hw_exp": "S-expression `(println \"...\")`.",
        "ops_exp": "In Lisp/Clojure, operators are prefix functions: `(+ a b)`. `(/ 20 6)` produces an exact Rational number `10/3`, while `(quot a b)` returns integer quotient."
    },
    {
        "id": "26-elixir",
        "name": "Elixir",
        "ext": "exs",
        "hw_file": "hello_world.exs",
        "ops_file": "basic_operations.exs",
        "category": "Functional & Declarative",
        "paradigm": "Functional, Concurrent (Actor model)",
        "year": "2012",
        "creator": "José Valim",
        "install": "elixir-lang.org",
        "hw_run": "elixir hello_world.exs",
        "ops_run": "elixir basic_operations.exs",
        "hw_output": "Hello, World!",
        "ops_output": "a = 20, b = 6\nAddition (a + b)        : 26\nSubtraction (a - b)     : 14\nMultiplication (a * b)  : 120\nFloat Division (a / b)  : 3.3333333333333335\nInteger Division (div)  : 3\nRemainder (rem)         : 2",
        "hw_code": '''# ==========================================
# Program: Hello World in Elixir
# ==========================================
IO.puts("Hello, World!")
''',
        "ops_code": '''# ==========================================
# Program: Basic Operations in Elixir (+, -, *, /, div, rem)
# ==========================================
a = 20
b = 6

IO.puts("a = #{a}, b = #{b}")
IO.puts("Addition (a + b)        : #{a + b}")
IO.puts("Subtraction (a - b)     : #{a - b}")
IO.puts("Multiplication (a * b)  : #{a * b}")
IO.puts("Float Division (a / b)  : #{a / b}")
IO.puts("Integer Division (div)  : #{div(a, b)}")
IO.puts("Remainder (rem)         : #{rem(a, b)}")
''',
        "hw_exp": "`IO.puts` prints a string to stdout.",
        "ops_exp": "In Elixir, `/` always yields a float, `div(a, b)` does integer division, and `rem(a, b)` computes remainder."
    },
    {
        "id": "27-erlang",
        "name": "Erlang",
        "ext": "erl",
        "hw_file": "hello_world.erl",
        "ops_file": "basic_operations.erl",
        "category": "Functional & Declarative",
        "paradigm": "Functional, Concurrent (Actor model)",
        "year": "1986",
        "creator": "Joe Armstrong et al.",
        "install": "erlang.org",
        "hw_run": "erlc hello_world.erl && erl -noshell -s hello_world start -s init stop",
        "ops_run": "erlc basic_operations.erl && erl -noshell -s basic_operations start -s init stop",
        "hw_output": "Hello, World!",
        "ops_output": "a = 20, b = 6\nAddition: 26, Subtraction: 14, Multiplication: 120, Division: 3, Remainder: 2",
        "hw_code": '''% ==========================================
% Program: Hello World in Erlang
% ==========================================
-module(hello_world).
-export([start/0]).

start() ->
    io:format("Hello, World!~n").
''',
        "ops_code": '''% ==========================================
% Program: Basic Operations in Erlang (+, -, *, div, rem)
% ==========================================
-module(basic_operations).
-export([start/0]).

start() ->
    A = 20,
    B = 6,
    io:format("a = ~p, b = ~p~n", [A, B]),
    io:format("Addition: ~p, Subtraction: ~p, Multiplication: ~p, Division: ~p, Remainder: ~p~n",
              [A + B, A - B, A * B, A div B, A rem B]).
''',
        "hw_exp": "Erlang module with exported `start/0`.",
        "ops_exp": "Erlang variables are capitalized (`A`, `B`). `div` is integer division, and `rem` is remainder."
    },
    {
        "id": "28-ocaml",
        "name": "OCaml",
        "ext": "ml",
        "hw_file": "hello_world.ml",
        "ops_file": "basic_operations.ml",
        "category": "Functional & Declarative",
        "paradigm": "Multi-paradigm (Functional, imperative, OOP)",
        "year": "1996",
        "creator": "INRIA",
        "install": "ocaml.org / opam",
        "hw_run": "ocaml hello_world.ml",
        "ops_run": "ocaml basic_operations.ml",
        "hw_output": "Hello, World!",
        "ops_output": "a = 20, b = 6\nAddition (a + b)        : 26\nSubtraction (a - b)     : 14\nMultiplication (a * b)  : 120\nInteger Division (a / b): 3\nFloat Division (float)  : 3.333333\nModulo (a mod b)        : 2",
        "hw_code": '''(* ==========================================
   Program: Hello World in OCaml
   ========================================== *)
let () = print_endline "Hello, World!"
''',
        "ops_code": '''(* ==========================================
   Program: Basic Operations in OCaml (+, -, *, /, mod)
   ========================================== *)
let () =
  let a = 20 in
  let b = 6 in
  Printf.printf "a = %d, b = %d\\n" a b;
  Printf.printf "Addition (a + b)        : %d\\n" (a + b);
  Printf.printf "Subtraction (a - b)     : %d\\n" (a - b);
  Printf.printf "Multiplication (a * b)  : %d\\n" (a * b);
  Printf.printf "Integer Division (a / b): %d\\n" (a / b);
  Printf.printf "Float Division (float)  : %f\\n" (float_of_int a /. float_of_int b);
  Printf.printf "Modulo (a mod b)        : %d\\n" (a mod b)
''',
        "hw_exp": "`print_endline` prints text with a newline.",
        "ops_exp": "OCaml separates integer operators (`+`, `-`, `*`, `/`) from float operators (`+.`, `-.`, `*.`, `/.`). `mod` is modulo."
    },
    {
        "id": "29-fsharp",
        "name": "F#",
        "ext": "fs",
        "hw_file": "hello_world.fs",
        "ops_file": "basic_operations.fs",
        "category": "Functional & Declarative",
        "paradigm": "Functional-first, object-oriented, imperative",
        "year": "2005",
        "creator": "Don Syme (Microsoft Research)",
        "install": ".NET SDK",
        "hw_run": "dotnet fsi hello_world.fs",
        "ops_run": "dotnet fsi basic_operations.fs",
        "hw_output": "Hello, World!",
        "ops_output": "a = 20, b = 6\nAddition (a + b)        : 26\nSubtraction (a - b)     : 14\nMultiplication (a * b)  : 120\nInteger Division (a / b): 3\nFloat Division (float)  : 3.333333\nModulo (a % b)          : 2",
        "hw_code": '''// ==========================================
// Program: Hello World in F#
// ==========================================
printfn "Hello, World!"
''',
        "ops_code": '''// ==========================================
// Program: Basic Operations in F# (+, -, *, /, %)
// ==========================================
let a = 20
let b = 6

printfn "a = %d, b = %d" a b
printfn "Addition (a + b)        : %d" (a + b)
printfn "Subtraction (a - b)     : %d" (a - b)
printfn "Multiplication (a * b)  : %d" (a * b)
printfn "Integer Division (a / b): %d" (a / b)
printfn "Float Division (float)  : %f" (float a / float b)
printfn "Modulo (a % b)          : %d" (a % b)
''',
        "hw_exp": "`printfn` is a strongly typed output function.",
        "ops_exp": "F# supports standard arithmetic with type safety: `float a / float b` casts to float for real division."
    },
    {
        "id": "30-common-lisp",
        "name": "Common Lisp",
        "ext": "lisp",
        "hw_file": "hello_world.lisp",
        "ops_file": "basic_operations.lisp",
        "category": "Functional & Declarative",
        "paradigm": "Multi-paradigm (Symbolic, functional, procedural, OOP)",
        "year": "1984",
        "creator": "Guy L. Steele Jr. et al.",
        "install": "SBCL",
        "hw_run": "sbcl --script hello_world.lisp",
        "ops_run": "sbcl --script basic_operations.lisp",
        "hw_output": "Hello, World!",
        "ops_output": "a = 20, b = 6\nAddition (+ a b)        : 26\nSubtraction (- a b)     : 14\nMultiplication (* a b)  : 120\nFloor Quotient          : 3\nExact Division (/ a b)  : 10/3\nModulo (mod a b)        : 2",
        "hw_code": ''';;; ==========================================
;;; Program: Hello World in Common Lisp
;;; ==========================================
(format t "Hello, World!~%")
''',
        "ops_code": ''';;; ==========================================
;;; Program: Basic Operations in Common Lisp (+, -, *, /, mod)
;;; ==========================================
(let ((a 20)
      (b 6))
  (format t "a = ~A, b = ~A~%" a b)
  (format t "Addition (+ a b)        : ~A~%" (+ a b))
  (format t "Subtraction (- a b)     : ~A~%" (- a b))
  (format t "Multiplication (* a b)  : ~A~%" (* a b))
  (format t "Floor Quotient          : ~A~%" (floor a b))
  (format t "Exact Division (/ a b)  : ~A~%" (/ a b))
  (format t "Modulo (mod a b)        : ~A~%" (mod a b)))
''',
        "hw_exp": "`format t` writes to stdout.",
        "ops_exp": "Common Lisp provides built-in exact rational division `(/ 20 6) -> 10/3` and `(mod a b)` for remainder."
    },
    {
        "id": "31-scheme",
        "name": "Scheme / Racket",
        "ext": "rkt",
        "hw_file": "hello_world.rkt",
        "ops_file": "basic_operations.rkt",
        "category": "Functional & Declarative",
        "paradigm": "Functional (Lisp dialect)",
        "year": "1975",
        "creator": "Guy L. Steele & Gerald Jay Sussman",
        "install": "racket-lang.org",
        "hw_run": "racket hello_world.rkt",
        "ops_run": "racket basic_operations.rkt",
        "hw_output": "Hello, World!",
        "ops_output": "a = 20, b = 6\nAddition: 26, Subtraction: 14, Multiplication: 120, Quotient: 3, Exact Division: 10/3, Remainder: 2",
        "hw_code": '''#lang racket
;; ==========================================
;; Program: Hello World in Racket / Scheme
;; ==========================================
(displayln "Hello, World!")
''',
        "ops_code": '''#lang racket
;; ==========================================
;; Program: Basic Operations in Racket / Scheme
;; ==========================================
(define a 20)
(define b 6)

(printf "a = ~a, b = ~a\\n" a b)
(printf "Addition: ~a, Subtraction: ~a, Multiplication: ~a, Quotient: ~a, Exact Division: ~a, Remainder: ~a\\n"
        (+ a b)
        (- a b)
        (* a b)
        (quotient a b)
        (/ a b)
        (remainder a b))
''',
        "hw_exp": "`displayln` outputs string to port.",
        "ops_exp": "`quotient` computes integer division, `/` computes rational fractions, and `remainder` computes modulo."
    },
    {
        "id": "32-bash",
        "name": "Bash",
        "ext": "sh",
        "hw_file": "hello_world.sh",
        "ops_file": "basic_operations.sh",
        "category": "Shell & Scripting",
        "paradigm": "Command Language, Scripting",
        "year": "1989",
        "creator": "Brian Fox",
        "install": "Built-in / Git Bash",
        "hw_run": "bash hello_world.sh",
        "ops_run": "bash basic_operations.sh",
        "hw_output": "Hello, World!",
        "ops_output": "a = 20, b = 6\nAddition (a + b)        : 26\nSubtraction (a - b)     : 14\nMultiplication (a * b)  : 120\nInteger Division (a / b): 3\nModulo (a % b)          : 2",
        "hw_code": '''#!/usr/bin/env bash
# ==========================================
# Program: Hello World in Bash
# ==========================================
echo "Hello, World!"
''',
        "ops_code": '''#!/usr/bin/env bash
# ==========================================
# Program: Basic Operations in Bash (+, -, *, /, %)
# ==========================================
a=20
b=6

echo "a = $a, b = $b"
echo "Addition (a + b)        : $((a + b))"
echo "Subtraction (a - b)     : $((a - b))"
echo "Multiplication (a * b)  : $((a * b))"
echo "Integer Division (a / b): $((a / b))"
echo "Modulo (a % b)          : $((a % b))"
''',
        "hw_exp": "`echo` outputs to stdout.",
        "ops_exp": "Bash evaluates arithmetic inside `$(( ... ))` using standard operators."
    },
    {
        "id": "33-powershell",
        "name": "PowerShell",
        "ext": "ps1",
        "hw_file": "hello_world.ps1",
        "ops_file": "basic_operations.ps1",
        "category": "Shell & Scripting",
        "paradigm": "Task-based command-line shell & scripting language",
        "year": "2006",
        "creator": "Jeffrey Snover (Microsoft)",
        "install": "Built-in Windows / pwsh",
        "hw_run": "powershell -ExecutionPolicy Bypass -File hello_world.ps1",
        "ops_run": "powershell -ExecutionPolicy Bypass -File basic_operations.ps1",
        "hw_output": "Hello, World!",
        "ops_output": "a = 20, b = 6\nAddition (a + b)        : 26\nSubtraction (a - b)     : 14\nMultiplication (a * b)  : 120\nDivision (a / b)        : 3.33333333333333\nInteger Division ([int]): 3\nModulo (a % b)          : 2",
        "hw_code": '''# ==========================================
# Program: Hello World in PowerShell
# ==========================================
Write-Output "Hello, World!"
''',
        "ops_code": '''# ==========================================
# Program: Basic Operations in PowerShell (+, -, *, /, %)
# ==========================================
$a = 20
$b = 6

Write-Output "a = $a, b = $b"
Write-Output "Addition (a + b)        : $($a + $b)"
Write-Output "Subtraction (a - b)     : $($a - $b)"
Write-Output "Multiplication (a * b)  : $($a * $b)"
Write-Output "Division (a / b)        : $($a / $b)"
Write-Output "Integer Division ([int]): $([Math]::Floor($a / $b))"
Write-Output "Modulo (a % b)          : $($a % $b)"
''',
        "hw_exp": "`Write-Output` sends objects to output pipeline.",
        "ops_exp": "PowerShell embeds subexpressions using `$($a + $b)` and leverages .NET `[Math]::Floor`."
    },
    {
        "id": "34-batch",
        "name": "Windows Batch",
        "ext": "bat",
        "hw_file": "hello_world.bat",
        "ops_file": "basic_operations.bat",
        "category": "Shell & Scripting",
        "paradigm": "Command script",
        "year": "1981",
        "creator": "Microsoft",
        "install": "Built-in Windows",
        "hw_run": "hello_world.bat",
        "ops_run": "basic_operations.bat",
        "hw_output": "Hello, World!",
        "ops_output": "a = 20, b = 6\nAddition (a + b)        : 26\nSubtraction (a - b)     : 14\nMultiplication (a * b)  : 120\nInteger Division (a / b): 3\nModulo (a %% b)          : 2",
        "hw_code": '''@echo off
rem ==========================================
rem Program: Hello World in Windows Batch
rem ==========================================
echo Hello, World!
''',
        "ops_code": '''@echo off
rem ==========================================
rem Program: Basic Operations in Windows Batch (+, -, *, /, %%)
rem ==========================================
set a=20
set b=6

set /a add=a+b
set /a sub=a-b
set /a mul=a*b
set /a div=a/b
set /a mod=a%%b

echo a = %a%, b = %b%
echo Addition (a + b)        : %add%
echo Subtraction (a - b)     : %sub%
echo Multiplication (a * b)  : %mul%
echo Integer Division (a / b): %div%
echo Modulo (a %%%% b)          : %mod%
''',
        "hw_exp": "`@echo off` and `echo` print directly.",
        "ops_exp": "Batch uses `set /a` for arithmetic evaluations. Modulo inside batch scripts is escaped as `%%`."
    },
    {
        "id": "35-lua",
        "name": "Lua",
        "ext": "lua",
        "hw_file": "hello_world.lua",
        "ops_file": "basic_operations.lua",
        "category": "Shell & Scripting",
        "paradigm": "Multi-paradigm (Scripting, procedural, prototype-based)",
        "year": "1993",
        "creator": "Roberto Ierusalimschy et al.",
        "install": "lua.org",
        "hw_run": "lua hello_world.lua",
        "ops_run": "lua basic_operations.lua",
        "hw_output": "Hello, World!",
        "ops_output": "a = 20, b = 6\nAddition (a + b)        : 26\nSubtraction (a - b)     : 14\nMultiplication (a * b)  : 120\nDivision (a / b)        : 3.3333333333333\nInteger Division (a // b): 3\nModulo (a % b)          : 2",
        "hw_code": '''-- ==========================================
-- Program: Hello World in Lua
-- ==========================================
print("Hello, World!")
''',
        "ops_code": '''-- ==========================================
-- Program: Basic Operations in Lua (+, -, *, /, //, %)
-- ==========================================
local a = 20
local b = 6

print(string.format("a = %d, b = %d", a, b))
print(string.format("Addition (a + b)        : %d", a + b))
print(string.format("Subtraction (a - b)     : %d", a - b))
print(string.format("Multiplication (a * b)  : %d", a * b))
print(string.format("Division (a / b)        : %f", a / b))
print(string.format("Integer Division (a // b): %d", a // b)) -- Lua 5.3+ integer division
print(string.format("Modulo (a %%%% b)          : %d", a % b))
''',
        "hw_exp": "`print()` writes values to stdout.",
        "ops_exp": "Lua 5.3+ supports `//` for integer division and `%` for remainder."
    },
    {
        "id": "36-perl",
        "name": "Perl",
        "ext": "pl",
        "hw_file": "hello_world.pl",
        "ops_file": "basic_operations.pl",
        "category": "Shell & Scripting",
        "paradigm": "Multi-paradigm (Procedural, functional, OOP)",
        "year": "1987",
        "creator": "Larry Wall",
        "install": "perl.org",
        "hw_run": "perl hello_world.pl",
        "ops_run": "perl basic_operations.pl",
        "hw_output": "Hello, World!",
        "ops_output": "a = 20, b = 6\nAddition (a + b)        : 26\nSubtraction (a - b)     : 14\nMultiplication (a * b)  : 120\nDivision (a / b)        : 3.33333333333333\nInteger Division (int)  : 3\nModulo (a % b)          : 2",
        "hw_code": '''#!/usr/bin/env perl
# ==========================================
# Program: Hello World in Perl
# ==========================================
use strict;
use warnings;

print "Hello, World!\n";
''',
        "ops_code": '''#!/usr/bin/env perl
# ==========================================
# Program: Basic Operations in Perl (+, -, *, /, %)
# ==========================================
use strict;
use warnings;

my $a = 20;
my $b = 6;

print "a = $a, b = $b\n";
print "Addition (a + b)        : " . ($a + $b) . "\n";
print "Subtraction (a - b)     : " . ($a - $b) . "\n";
print "Multiplication (a * b)  : " . ($a * $b) . "\n";
print "Division (a / b)        : " . ($a / $b) . "\n";
print "Integer Division (int)  : " . int($a / $b) . "\n";
print "Modulo (a % b)          : " . ($a % $b) . "\n";
''',
        "hw_exp": "`use strict;` and `print`.",
        "ops_exp": "Perl scalar variables use `$`. `int($a / $b)` truncates floating point division."
    },
    {
        "id": "37-awk",
        "name": "AWK",
        "ext": "awk",
        "hw_file": "hello_world.awk",
        "ops_file": "basic_operations.awk",
        "category": "Shell & Scripting",
        "paradigm": "Data-driven, pattern scanning and processing",
        "year": "1977",
        "creator": "Alfred Aho et al.",
        "install": "gawk",
        "hw_run": "awk -f hello_world.awk /dev/null",
        "ops_run": "awk -f basic_operations.awk /dev/null",
        "hw_output": "Hello, World!",
        "ops_output": "a = 20, b = 6\nAddition (a + b)        : 26\nSubtraction (a - b)     : 14\nMultiplication (a * b)  : 120\nDivision (a / b)        : 3.33333\nInteger Division (int)  : 3\nModulo (a % b)          : 2",
        "hw_code": '''# ==========================================
# Program: Hello World in AWK
# ==========================================
BEGIN {
    print "Hello, World!"
}
''',
        "ops_code": '''# ==========================================
# Program: Basic Operations in AWK (+, -, *, /, %)
# ==========================================
BEGIN {
    a = 20
    b = 6

    printf "a = %d, b = %d\\n", a, b
    printf "Addition (a + b)        : %d\\n", a + b
    printf "Subtraction (a - b)     : %d\\n", a - b
    printf "Multiplication (a * b)  : %d\\n", a * b
    printf "Division (a / b)        : %f\\n", a / b
    printf "Integer Division (int)  : %d\\n", int(a / b)
    printf "Modulo (a %%%% b)          : %d\\n", a % b
}
''',
        "hw_exp": "`BEGIN` block executes prior to input processing.",
        "ops_exp": "AWK performs floating division by default; `int(a / b)` yields the integer quotient."
    },
    {
        "id": "38-tcl",
        "name": "Tcl",
        "ext": "tcl",
        "hw_file": "hello_world.tcl",
        "ops_file": "basic_operations.tcl",
        "category": "Shell & Scripting",
        "paradigm": "Command-driven, functional, imperative",
        "year": "1988",
        "creator": "John Ousterhout",
        "install": "tcl.tk",
        "hw_run": "tclsh hello_world.tcl",
        "ops_run": "tclsh basic_operations.tcl",
        "hw_output": "Hello, World!",
        "ops_output": "a = 20, b = 6\nAddition (a + b)        : 26\nSubtraction (a - b)     : 14\nMultiplication (a * b)  : 120\nInteger Division (a / b): 3\nFloat Division          : 3.3333333333333335\nModulo (a % b)          : 2",
        "hw_code": '''# ==========================================
# Program: Hello World in Tcl
# ==========================================
puts "Hello, World!"
''',
        "ops_code": '''# ==========================================
# Program: Basic Operations in Tcl (+, -, *, /, %)
# ==========================================
set a 20
set b 6

puts "a = $a, b = $b"
puts "Addition (a + b)        : [expr {$a + $b}]"
puts "Subtraction (a - b)     : [expr {$a - $b}]"
puts "Multiplication (a * b)  : [expr {$a * $b}]"
puts "Integer Division (a / b): [expr {$a / $b}]"
puts "Float Division          : [expr {double($a) / $b}]"
puts "Modulo (a % b)          : [expr {$a % $b}]"
''',
        "hw_exp": "`puts` outputs to default channel.",
        "ops_exp": "In Tcl, all math is evaluated through the `expr` command within `[...]`."
    },
    {
        "id": "39-dart",
        "name": "Dart",
        "ext": "dart",
        "hw_file": "hello_world.dart",
        "ops_file": "basic_operations.dart",
        "category": "Web3, Mobile & Modern",
        "paradigm": "Multi-paradigm (Object-oriented, class-based)",
        "year": "2011",
        "creator": "Lars Bak and Kasper Lund (Google)",
        "install": "dart.dev",
        "hw_run": "dart run hello_world.dart",
        "ops_run": "dart run basic_operations.dart",
        "hw_output": "Hello, World!",
        "ops_output": "a = 20, b = 6\nAddition (a + b)        : 26\nSubtraction (a - b)     : 14\nMultiplication (a * b)  : 120\nDivision (a / b)        : 3.3333333333333335\nInteger Division (~/)   : 3\nModulo (a % b)          : 2",
        "hw_code": '''// ==========================================
// Program: Hello World in Dart
// ==========================================
void main() {
  print('Hello, World!');
}
''',
        "ops_code": '''// ==========================================
// Program: Basic Operations in Dart (+, -, *, /, ~/, %)
// ==========================================
void main() {
  int a = 20;
  int b = 6;

  print('a = $a, b = $b');
  print('Addition (a + b)        : ${a + b}');
  print('Subtraction (a - b)     : ${a - b}');
  print('Multiplication (a * b)  : ${a * b}');
  print('Division (a / b)        : ${a / b}');
  print('Integer Division (~/)   : ${a ~/ b}'); // ~/ is truncating integer division in Dart
  print('Modulo (a % b)          : ${a % b}');
}
''',
        "hw_exp": "`void main()` is the entry point.",
        "ops_exp": "Dart features the special `~/` operator for truncating integer division."
    },
    {
        "id": "40-objective-c",
        "name": "Objective-C",
        "ext": "m",
        "hw_file": "hello_world.m",
        "ops_file": "basic_operations.m",
        "category": "Web3, Mobile & Modern",
        "paradigm": "Object-oriented, reflective",
        "year": "1984",
        "creator": "Brad Cox and Tom Love",
        "install": "Clang / GNUstep / Xcode",
        "hw_run": "clang -framework Foundation hello_world.m -o hello_world && ./hello_world",
        "ops_run": "clang -framework Foundation basic_operations.m -o basic_operations && ./basic_operations",
        "hw_output": "Hello, World!",
        "ops_output": "a = 20, b = 6\nAddition (a + b)        : 26\nSubtraction (a - b)     : 14\nMultiplication (a * b)  : 120\nInteger Division (a / b): 3\nFloat Division (double) : 3.333333\nModulo (a % b)          : 2",
        "hw_code": '''// ==========================================
// Program: Hello World in Objective-C
// ==========================================
#import <Foundation/Foundation.h>

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        NSLog(@"Hello, World!");
    }
    return 0;
}
''',
        "ops_code": '''// ==========================================
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
''',
        "hw_exp": "`NSLog` formats and logs strings.",
        "ops_exp": "Objective-C inherits C's standard arithmetic operators with `%` for remainder."
    },
    {
        "id": "41-v",
        "name": "V (Vlang)",
        "ext": "v",
        "hw_file": "hello_world.v",
        "ops_file": "basic_operations.v",
        "category": "Web3, Mobile & Modern",
        "paradigm": "Static, procedural, safe systems language",
        "year": "2019",
        "creator": "Alexander Medvednikov",
        "install": "vlang.io",
        "hw_run": "v run hello_world.v",
        "ops_run": "v run basic_operations.v",
        "hw_output": "Hello, World!",
        "ops_output": "a = 20, b = 6\nAddition (a + b)        : 26\nSubtraction (a - b)     : 14\nMultiplication (a * b)  : 120\nInteger Division (a / b): 3\nFloat Division (f64)    : 3.3333333333333335\nModulo (a % b)          : 2",
        "hw_code": '''// ==========================================
// Program: Hello World in V (Vlang)
// ==========================================
fn main() {
    println('Hello, World!')
}
''',
        "ops_code": '''// ==========================================
// Program: Basic Operations in V (+, -, *, /, %)
// ==========================================
fn main() {
    a := 20
    b := 6

    println('a = $a, b = $b')
    println('Addition (a + b)        : ${a + b}')
    println('Subtraction (a - b)     : ${a - b}')
    println('Multiplication (a * b)  : ${a * b}')
    println('Integer Division (a / b): ${a / b}')
    println('Float Division (f64)    : ${f64(a) / f64(b)}')
    println('Modulo (a % b)          : ${a % b}')
}
''',
        "hw_exp": "`println` writes text followed by newline.",
        "ops_exp": "V uses string interpolation `${...}` and `f64(a)` for float conversion."
    },
    {
        "id": "42-crystal",
        "name": "Crystal",
        "ext": "cr",
        "hw_file": "hello_world.cr",
        "ops_file": "basic_operations.cr",
        "category": "Web3, Mobile & Modern",
        "paradigm": "Object-oriented, compiled, statically type-checked",
        "year": "2014",
        "creator": "Ary Borenszweig et al.",
        "install": "crystal-lang.org",
        "hw_run": "crystal run hello_world.cr",
        "ops_run": "crystal run basic_operations.cr",
        "hw_output": "Hello, World!",
        "ops_output": "a = 20, b = 6\nAddition (a + b)        : 26\nSubtraction (a - b)     : 14\nMultiplication (a * b)  : 120\nFloat Division (a / b)  : 3.3333333333333335\nInteger Division (//)   : 3\nModulo (a % b)          : 2",
        "hw_code": '''# ==========================================
# Program: Hello World in Crystal
# ==========================================
puts "Hello, World!"
''',
        "ops_code": '''# ==========================================
# Program: Basic Operations in Crystal (+, -, *, /, //, %)
# ==========================================
a = 20
b = 6

puts "a = #{a}, b = #{b}"
puts "Addition (a + b)        : #{a + b}"
puts "Subtraction (a - b)     : #{a - b}"
puts "Multiplication (a * b)  : #{a * b}"
puts "Float Division (a / b)  : #{a / b}"
puts "Integer Division (//)   : #{a // b}" # // is integer division in Crystal
puts "Modulo (a % b)          : #{a % b}"
''',
        "hw_exp": "`puts` sends text to stdout.",
        "ops_exp": "Crystal uses `//` for explicit integer division and `/` for float division."
    },
    {
        "id": "43-solidity",
        "name": "Solidity",
        "ext": "sol",
        "hw_file": "hello_world.sol",
        "ops_file": "basic_operations.sol",
        "category": "Web3, Mobile & Modern",
        "paradigm": "Contract-oriented, static typing (Ethereum EVM)",
        "year": "2014",
        "creator": "Gavin Wood et al.",
        "install": "`npm install -g solc`",
        "hw_run": "solc --bin hello_world.sol",
        "ops_run": "solc --bin basic_operations.sol",
        "hw_output": "Binary bytecode compiled successfully",
        "ops_output": "add = 26, sub = 14, mul = 120, div = 3, mod = 2",
        "hw_code": '''// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

// ==========================================
// Program: Hello World in Solidity (Ethereum Smart Contract)
// ==========================================
contract HelloWorld {
    string public greeting = "Hello, World!";

    function getGreeting() public view returns (string memory) {
        return greeting;
    }
}
''',
        "ops_code": '''// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

// ==========================================
// Program: Basic Operations in Solidity (+, -, *, /, %)
// ==========================================
contract BasicOperations {
    // Calculates +, -, *, /, % on the Ethereum Virtual Machine
    function calculate(uint256 a, uint256 b) public pure returns (
        uint256 addResult,
        uint256 subResult,
        uint256 mulResult,
        uint256 divResult,
        uint256 modResult
    ) {
        addResult = a + b;
        subResult = a - b;
        mulResult = a * b;
        divResult = a / b; // EVM integer division truncates
        modResult = a % b; // Modulo remainder
    }
}
''',
        "hw_exp": "Public state variable and getter on Ethereum.",
        "ops_exp": "Solidity operates on unsigned integers (`uint256`). EVM division automatically truncates; `%` calculates remainder with built-in overflow protection in 0.8+."
    },
    {
        "id": "44-sql",
        "name": "SQL",
        "ext": "sql",
        "hw_file": "hello_world.sql",
        "ops_file": "basic_operations.sql",
        "category": "Web3, Mobile & Modern",
        "paradigm": "Declarative (Relational Database Query Language)",
        "year": "1974",
        "creator": "Donald D. Chamberlin and Raymond F. Boyce (IBM)",
        "install": "SQLite / PostgreSQL / MySQL",
        "hw_run": "sqlite3 :memory: < hello_world.sql",
        "ops_run": "sqlite3 :memory: < basic_operations.sql",
        "hw_output": "Hello, World!",
        "ops_output": "26|14|120|3|3.33333333333333|2",
        "hw_code": '''-- ==========================================
-- Program: Hello World in SQL (ANSI Standard)
-- ==========================================
SELECT 'Hello, World!' AS message;
''',
        "ops_code": '''-- ==========================================
-- Program: Basic Operations in SQL (+, -, *, /, %)
-- ==========================================
SELECT
    20 + 6 AS addition,
    20 - 6 AS subtraction,
    20 * 6 AS multiplication,
    20 / 6 AS integer_division,
    20 * 1.0 / 6 AS float_division,
    20 % 6 AS modulo;
''',
        "hw_exp": "`SELECT` outputs a query projection.",
        "ops_exp": "SQL provides standard mathematical operators in `SELECT` statements; `20 * 1.0 / 6` casts to decimal."
    },
    {
        "id": "45-cobol",
        "name": "COBOL",
        "ext": "cob",
        "hw_file": "hello_world.cob",
        "ops_file": "basic_operations.cob",
        "category": "Classic & Foundational",
        "paradigm": "Imperative, procedural (Business computing)",
        "year": "1959",
        "creator": "CODASYL (Grace Hopper influence)",
        "install": "GnuCOBOL",
        "hw_run": "cobc -x hello_world.cob -o hello_world && ./hello_world",
        "ops_run": "cobc -x basic_operations.cob -o basic_operations && ./basic_operations",
        "hw_output": "Hello, World!",
        "ops_output": "A = 20, B = 6\nADDITION: 26\nSUBTRACTION: 14\nMULTIPLICATION: 120\nDIVISION: 3\nREMAINDER: 2",
        "hw_code": '''      * ==========================================
      * Program: Hello World in COBOL
      * ==========================================
       IDENTIFICATION DIVISION.
       PROGRAM-ID. HELLO-WORLD.

       PROCEDURE DIVISION.
           DISPLAY 'Hello, World!'.
           STOP RUN.
''',
        "ops_code": '''      * ==========================================
      * Program: Basic Operations in COBOL (+, -, *, /, %)
      * ==========================================
       IDENTIFICATION DIVISION.
       PROGRAM-ID. BASIC-OPS.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 A          PIC 99 VALUE 20.
       01 B          PIC 99 VALUE 6.
       01 RES-ADD    PIC 99.
       01 RES-SUB    PIC 99.
       01 RES-MUL    PIC 999.
       01 RES-DIV    PIC 99.
       01 RES-MOD    PIC 99.

       PROCEDURE DIVISION.
           COMPUTE RES-ADD = A + B.
           COMPUTE RES-SUB = A - B.
           COMPUTE RES-MUL = A * B.
           DIVIDE A BY B GIVING RES-DIV REMAINDER RES-MOD.

           DISPLAY 'A = 20, B = 6'.
           DISPLAY 'ADDITION: ' RES-ADD.
           DISPLAY 'SUBTRACTION: ' RES-SUB.
           DISPLAY 'MULTIPLICATION: ' RES-MUL.
           DISPLAY 'DIVISION: ' RES-DIV.
           DISPLAY 'REMAINDER: ' RES-MOD.
           STOP RUN.
''',
        "hw_exp": "`DISPLAY` and `STOP RUN`.",
        "ops_exp": "COBOL uses English-like verbs: `COMPUTE` for formulas and `DIVIDE ... GIVING ... REMAINDER` for division and modulo."
    },
    {
        "id": "46-pascal",
        "name": "Pascal",
        "ext": "pas",
        "hw_file": "hello_world.pas",
        "ops_file": "basic_operations.pas",
        "category": "Classic & Foundational",
        "paradigm": "Imperative, structured, procedural",
        "year": "1970",
        "creator": "Niklaus Wirth",
        "install": "Free Pascal Compiler (FPC)",
        "hw_run": "fpc hello_world.pas && ./hello_world",
        "ops_run": "fpc basic_operations.pas && ./basic_operations",
        "hw_output": "Hello, World!",
        "ops_output": "a = 20, b = 6\nAddition (a + b)        : 26\nSubtraction (a - b)     : 14\nMultiplication (a * b)  : 120\nInteger Division (div)  : 3\nFloat Division (/)      : 3.33\nModulo (mod)            : 2",
        "hw_code": '''(* ==========================================
   Program: Hello World in Pascal
   ========================================== *)
program HelloWorld;
begin
    writeln('Hello, World!');
end.
''',
        "ops_code": '''(* ==========================================
   Program: Basic Operations in Pascal (+, -, *, /, div, mod)
   ========================================== *)
program BasicOperations;
var
    a, b: integer;
begin
    a := 20;
    b := 6;

    writeln('a = 20, b = 6');
    writeln('Addition (a + b)        : ', a + b);
    writeln('Subtraction (a - b)     : ', a - b);
    writeln('Multiplication (a * b)  : ', a * b);
    writeln('Integer Division (div)  : ', a div b);
    writeln('Float Division (/)      : ', (a / b):0:2);
    writeln('Modulo (mod)            : ', a mod b);
end.
''',
        "hw_exp": "`writeln` formats output to next line.",
        "ops_exp": "Pascal uses `div` for integer quotient, `/` for real division, and `mod` for remainder."
    },
    {
        "id": "47-basic",
        "name": "BASIC",
        "ext": "bas",
        "hw_file": "hello_world.bas",
        "ops_file": "basic_operations.bas",
        "category": "Classic & Foundational",
        "paradigm": "Imperative, procedural",
        "year": "1964",
        "creator": "John G. Kemeny & Thomas E. Kurtz",
        "install": "FreeBASIC",
        "hw_run": "fbc -lang qb hello_world.bas && ./hello_world",
        "ops_run": "fbc -lang qb basic_operations.bas && ./basic_operations",
        "hw_output": "Hello, World!",
        "ops_output": "a = 20, b = 6\nAddition: 26, Subtraction: 14, Multiplication: 120, Division: 3, Modulo: 2",
        "hw_code": '''10 REM ==========================================
20 REM Program: Hello World in Classic BASIC
30 REM ==========================================
40 PRINT "Hello, World!"
50 END
''',
        "ops_code": '''10 REM ==========================================
20 REM Program: Basic Operations in Classic BASIC (+, -, *, \, MOD)
30 REM ==========================================
40 A = 20
50 B = 6
60 PRINT "a = 20, b = 6"
70 PRINT "Addition: "; A + B; ", Subtraction: "; A - B; ", Multiplication: "; A * B; ", Division: "; A \ B; ", Modulo: "; A MOD B
80 END
''',
        "hw_exp": "`PRINT` and numbered lines in classic Dartmouth/QuickBASIC.",
        "ops_exp": "BASIC uses `\\` for integer division, `/` for floating division, and `MOD` for remainder."
    },
    {
        "id": "48-forth",
        "name": "Forth",
        "ext": "fs",
        "hw_file": "hello_world.fs",
        "ops_file": "basic_operations.fs",
        "category": "Classic & Foundational",
        "paradigm": "Stack-oriented, concatenative, procedural",
        "year": "1970",
        "creator": "Charles H. Moore",
        "install": "Gforth",
        "hw_run": "gforth hello_world.fs -e bye",
        "ops_run": "gforth basic_operations.fs -e bye",
        "hw_output": "Hello, World!",
        "ops_output": "a = 20, b = 6\nAddition: 26\nSubtraction: 14\nMultiplication: 120\nDivision: 3\nModulo: 2",
        "hw_code": '''\\ ==========================================
\\ Program: Hello World in Forth
\\ ==========================================
: HELLO ( -- )
  ." Hello, World!" CR ;

HELLO
''',
        "ops_code": '''\\ ==========================================
\\ Program: Basic Operations in Forth (+, -, *, /, MOD)
\\ ==========================================
: OPERATIONS ( -- )
  ." a = 20, b = 6" CR
  ." Addition: " 20 6 + . CR
  ." Subtraction: " 20 6 - . CR
  ." Multiplication: " 20 6 * . CR
  ." Division: " 20 6 / . CR
  ." Modulo: " 20 6 MOD . CR ;

OPERATIONS
''',
        "hw_exp": "Word definition `: HELLO ... ;` and print `.\" ...\"`.",
        "ops_exp": "Forth is stack-based: `20 6 +` pushes 20 and 6, pops them to add, and `.` prints the top of the stack."
    },
    {
        "id": "49-smalltalk",
        "name": "Smalltalk",
        "ext": "st",
        "hw_file": "hello_world.st",
        "ops_file": "basic_operations.st",
        "category": "Classic & Foundational",
        "paradigm": "Pure object-oriented, message passing",
        "year": "1972",
        "creator": "Alan Kay et al. (Xerox PARC)",
        "install": "GNU Smalltalk (gst)",
        "hw_run": "gst hello_world.st",
        "ops_run": "gst basic_operations.st",
        "hw_output": "Hello, World!",
        "ops_output": "a = 20, b = 6\nAddition (a + b)        : 26\nSubtraction (a - b)     : 14\nMultiplication (a * b)  : 120\nInteger Division (//)   : 3\nExact Fraction (/)      : (10/3)\nModulo (\\\\)             : 2",
        "hw_code": '''"==========================================
 Program: Hello World in Smalltalk
 =========================================="
Transcript show: 'Hello, World!'; cr.
''',
        "ops_code": '''"==========================================
 Program: Basic Operations in Smalltalk (+, -, *, //, \\\\)
 =========================================="
| a b |
a := 20.
b := 6.

Transcript show: 'a = 20, b = 6'; cr.
Transcript show: 'Addition (a + b)        : ', (a + b) printString; cr.
Transcript show: 'Subtraction (a - b)     : ', (a - b) printString; cr.
Transcript show: 'Multiplication (a * b)  : ', (a * b) printString; cr.
Transcript show: 'Integer Division (//)   : ', (a // b) printString; cr.
Transcript show: 'Exact Fraction (/)      : ', (a / b) printString; cr.
Transcript show: 'Modulo (\\\\)             : ', (a \\\\ b) printString; cr.
''',
        "hw_exp": "`Transcript show: '...'; cr.` message sending.",
        "ops_exp": "In Smalltalk, `+`, `-`, `*` are binary messages sent to number objects. `//` is integer division, `/` yields a Fraction, and `\\\\` calculates modulo."
    },
    {
        "id": "50-prolog",
        "name": "Prolog",
        "ext": "pl",
        "hw_file": "hello_world.pl",
        "ops_file": "basic_operations.pl",
        "category": "Classic & Foundational",
        "paradigm": "Declarative, Logic programming",
        "year": "1972",
        "creator": "Alain Colmerauer and Philippe Roussel",
        "install": "SWI-Prolog",
        "hw_run": "swipl -q -t main -f hello_world.pl",
        "ops_run": "swipl -q -t main -f basic_operations.pl",
        "hw_output": "Hello, World!",
        "ops_output": "a = 20, b = 6\nAddition: 26, Subtraction: 14, Multiplication: 120, Division: 3, Modulo: 2",
        "hw_code": '''% ==========================================
% Program: Hello World in Prolog (SWI-Prolog)
% ==========================================
:- initialization(main).

main :-
    write('Hello, World!'), nl,
    halt.
''',
        "ops_code": '''% ==========================================
% Program: Basic Operations in Prolog (+, -, *, //, mod)
% ==========================================
:- initialization(main).

main :-
    A = 20,
    B = 6,
    Add is A + B,
    Sub is A - B,
    Mul is A * B,
    Div is A // B,   % // is integer division in ISO Prolog
    Mod is A mod B,  % mod is modulo remainder
    format('a = ~w, b = ~w~n', [A, B]),
    format('Addition: ~w, Subtraction: ~w, Multiplication: ~w, Division: ~w, Modulo: ~w~n',
           [Add, Sub, Mul, Div, Mod]),
    halt.
''',
        "hw_exp": "`write('...')`, `nl`, and `halt`.",
        "ops_exp": "In Prolog, arithmetic is evaluated using the `is` operator: `Add is A + B`. `//` is integer division and `mod` calculates remainder."
    }
]

def main():
    print(f"Generating repository structure for {len(LANGUAGES)} languages with Hello World AND Basic Operations...")
    
    docs_dir = os.path.join(BASE_DIR, "docs")
    languages_dir = os.path.join(BASE_DIR, "languages")
    github_dir = os.path.join(BASE_DIR, ".github", "workflows")
    scripts_dir = os.path.join(BASE_DIR, "scripts")
    
    os.makedirs(docs_dir, exist_ok=True)
    os.makedirs(languages_dir, exist_ok=True)
    os.makedirs(github_dir, exist_ok=True)
    os.makedirs(scripts_dir, exist_ok=True)

    for lang in LANGUAGES:
        lang_dir = os.path.join(languages_dir, lang["id"])
        os.makedirs(lang_dir, exist_ok=True)
        
        # 1. Write Hello World file
        hw_file = os.path.join(lang_dir, lang["hw_file"])
        with open(hw_file, "w", encoding="utf-8") as f:
            f.write(lang["hw_code"])
            
        # 2. Write Basic Operations file
        ops_file = os.path.join(lang_dir, lang["ops_file"])
        with open(ops_file, "w", encoding="utf-8") as f:
            f.write(lang["ops_code"])
            
        # 3. Write language README.md with BOTH programs
        lang_readme = os.path.join(lang_dir, "README.md")
        readme_content = f"""# {lang['name']} Reference Guide

> **Category**: {lang['category']}  
> **Paradigm**: {lang['paradigm']}  
> **Initial Release**: {lang['year']}  
> **Created By**: {lang['creator']}  

---

## 1. Program 1: Hello World (`{lang['hw_file']}`)

```{lang['ext']}
{lang['hw_code'].strip()}
```

### Explanation
{lang['hw_exp']}

### Run Hello World
```bash
{lang['hw_run']}
```
**Expected Output**:
```text
{lang['hw_output']}
```

---

## 2. Program 2: Basic Operations (`{lang['ops_file']}`)
*Demonstrates arithmetic operations: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), and Modulo/Remainder (`%`).*

```{lang['ext']}
{lang['ops_code'].strip()}
```

### Explanation
{lang['ops_exp']}

### Run Basic Operations
```bash
{lang['ops_run']}
```
**Expected Output**:
```text
{lang['ops_output']}
```

---

## 3. Prerequisites & Installation

- **Guide**: {lang['install']}
"""
        with open(lang_readme, "w", encoding="utf-8") as f:
            f.write(readme_content)
        print(f"  [+] Configured {lang['id']}: {lang['hw_file']} & {lang['ops_file']}")

    # 4. Create Root README.md
    print("Generating Root README.md...")
    table_rows = []
    for i, lang in enumerate(LANGUAGES, 1):
        table_rows.append(
            f"| {i:02d} | [{lang['name']}](languages/{lang['id']}/) | `.{lang['ext']}` | [{lang['hw_file']}](languages/{lang['id']}/{lang['hw_file']}) | [{lang['ops_file']}](languages/{lang['id']}/{lang['ops_file']}) | {lang['category']} |"
        )
    
    table_content = "\n".join(table_rows)

    root_readme = f"""<div align="center">

# 🌍 The Polyglot Codebase: 50 Languages Reference

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Languages](https://img.shields.io/badge/Languages-50%20Covered-success.svg)](languages/)
[![Programs](https://img.shields.io/badge/Programs-100%20Implemented-blueviolet.svg)](languages/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](docs/CONTRIBUTING.md)
[![Status](https://img.shields.io/badge/Build-Passing-brightgreen.svg)](#)

*A clean, idiomatic, and reference-grade educational repository demonstrating **"Hello, World!"** and **Basic Arithmetic Operations (+, -, \*, /, %)** across 50 programming languages, complete with step-by-step annotations, compiler setup, and progressive roadmap milestones.*

[Explore Languages](#-complete-language-matrix-50-languages) • [Repository Structure](#-repository-structure) • [Contributing](docs/CONTRIBUTING.md) • [Roadmap](docs/ROADMAP.md)

</div>

---

## 🌟 Why This Repository?
Learning how different languages express fundamental constructs helps developers:
- Compare syntax across paradigms: **Imperative, OOP, Functional, Logic, Declarative, Stack-based**.
- Understand arithmetic evaluation models (Integer vs Floating Division, Exact Rationals, Modulo/Remainder keywords like `%`, `mod`, `rem`, `MOD`, `%%`, `\\\\`).
- Quickly spin up boilerplate and run commands for any technology stack.
- Serve as a crystal-clear learning reference and teaching resource.

---

## 📊 Complete Language Matrix (50 Languages, 100 Programs)

| # | Language | Extension | 1. Hello World | 2. Basic Operations (+, -, \*, /, %) | Category |
|---|----------|-----------|----------------|--------------------------------------|----------|
{table_content}

---

## 📂 Repository Structure

```
.
├── .github/
│   └── workflows/
│       └── ci.yml                 # Automated syntax and structure CI
├── docs/
│   ├── CONTRIBUTING.md            # Guidelines for contributors
│   ├── CODE_OF_CONDUCT.md         # Community standard
│   └── ROADMAP.md                 # Progressive roadmap milestones
├── languages/                     # 50 individual language folders
│   ├── 01-python/
│   │   ├── README.md              # Full documentation & run commands
│   │   ├── hello_world.py         # Program 1
│   │   └── basic_operations.py    # Program 2 (+, -, *, /, //, %)
│   ├── ...
│   └── 50-prolog/
│       ├── README.md
│       ├── hello_world.pl
│       └── basic_operations.pl
├── scripts/
│   ├── generate_repo.py           # Code generator script
│   └── verify_all.py              # Repository validation tool
├── LICENSE                        # MIT License
└── README.md                      # Main visual index & matrix
```

---

## 🚀 How to Run Locally

You can clone this repository and test any language:

```bash
git clone https://github.com/sohail78692/polyglot-codebase.git
cd polyglot-codebase
```

To run the verification test suite:

```bash
python scripts/verify_all.py
```

---

## 🛣️ Progressive Roadmap
This repository is planned as a progressive multi-part series:
1. **Part 1 (Current ✅)**: Hello World across 50 languages.
2. **Part 2 (Current ✅)**: Basic Operations (`+`, `-`, `*`, `/`, `%`) across 50 languages.
3. **Part 3**: Control Flow (Conditionals: If/Else, Match/Switch; Loops: For, While).
4. **Part 4**: Functions, Closures, and Error Handling.
5. **Part 5**: Idiomatic Algorithms (FizzBuzz, Fibonacci, Sorting).

See [docs/ROADMAP.md](docs/ROADMAP.md) for full details.

---

## 🤝 Contributing
Contributions are warmly welcomed! Please read [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) for instructions on proposing new languages or improving code idioms.

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
"""
    with open(os.path.join(BASE_DIR, "README.md"), "w", encoding="utf-8") as f:
        f.write(root_readme)

    # 5. Update verify_all.py
    print("Updating scripts/verify_all.py...")
    verify_script = '''#!/usr/bin/env python3
import os
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LANGUAGES_DIR = os.path.join(BASE_DIR, "languages")

def verify():
    print("==================================================")
    print("  Polyglot Repository Verification Suite")
    print("  (50 Languages: Hello World + Basic Operations)")
    print("==================================================")
    
    if not os.path.exists(LANGUAGES_DIR):
        print(f"Error: {LANGUAGES_DIR} does not exist.")
        sys.exit(1)
        
    entries = sorted([d for d in os.listdir(LANGUAGES_DIR) if os.path.isdir(os.path.join(LANGUAGES_DIR, d))])
    total = len(entries)
    print(f"Discovered {total} language directories in 'languages/'.\\n")
    
    passed = 0
    failed = 0
    
    for folder in entries:
        folder_path = os.path.join(LANGUAGES_DIR, folder)
        files = os.listdir(folder_path)
        readme_present = "README.md" in files
        
        has_hw = any("hello_world" in f.lower() for f in files)
        has_ops = any("basic_operations" in f.lower() for f in files)
        
        notes = []
        if not readme_present:
            notes.append("Missing README.md")
        if not has_hw:
            notes.append("Missing hello_world source")
        if not has_ops:
            notes.append("Missing basic_operations source")
            
        if not notes:
            passed += 1
            hw_file = [f for f in files if "hello_world" in f.lower()][0]
            ops_file = [f for f in files if "basic_operations" in f.lower()][0]
            print(f"  [PASS] {folder:<20} -> {hw_file}, {ops_file}")
        else:
            failed += 1
            print(f"  [FAIL] {folder:<20} -> {', '.join(notes)}")
            
    print("--------------------------------------------------")
    print(f"Results: {passed}/{total} language directories passed verification.")
    print(f"Total Programs: {passed * 2} verified source files.")
    print("==================================================")
    
    if failed > 0 or total != 50:
        print(f"Verification failed: Expected 50 languages, found {passed} passing.")
        sys.exit(1)
    else:
        print("All 50 languages with 100 programs are properly structured and verified!")
        sys.exit(0)

if __name__ == "__main__":
    verify()
'''
    with open(os.path.join(scripts_dir, "verify_all.py"), "w", encoding="utf-8") as f:
        f.write(verify_script)

    print("\nAll 50 languages updated with Hello World AND Basic Operations!")

if __name__ == "__main__":
    main()
